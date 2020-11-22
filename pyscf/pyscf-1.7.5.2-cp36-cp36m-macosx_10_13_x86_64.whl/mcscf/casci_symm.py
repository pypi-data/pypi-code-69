#!/usr/bin/env python
# Copyright 2014-2020 The PySCF Developers. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author: Qiming Sun <osirpt.sun@gmail.com>
#

from functools import reduce
import numpy
from pyscf import lib
from pyscf.lib import logger
from pyscf import scf
from pyscf import symm
from pyscf import fci
from pyscf.mcscf import casci
from pyscf.mcscf import addons


class SymAdaptedCASCI(casci.CASCI):
    def __init__(self, mf_or_mol, ncas, nelecas, ncore=None):
        casci.CASCI.__init__(self, mf_or_mol, ncas, nelecas, ncore)

        assert(self.mol.symmetry)
        fcisolver = self.fcisolver
        if isinstance(fcisolver, fci.direct_spin0.FCISolver):
            self.fcisolver = fci.direct_spin0_symm.FCISolver(self.mol)
        else:
            self.fcisolver = fci.direct_spin1_symm.FCISolver(self.mol)
        self.fcisolver.__dict__.update(fcisolver.__dict__)

    @property
    def wfnsym(self):
        return self.fcisolver.wfnsym
    @wfnsym.setter
    def wfnsym(self, wfnsym):
        self.fcisolver.wfnsym = wfnsym

    def kernel(self, mo_coeff=None, ci0=None, verbose=None):
        if mo_coeff is None:
            mo_coeff = self.mo_coeff
        if ci0 is None:
            ci0 = self.ci

        # Initialize/overwrite self.fcisolver.orbsym and self.fcisolver.wfnsym
        mo_coeff = self.mo_coeff = label_symmetry_(self, mo_coeff, ci0)
        return casci.CASCI.kernel(self, mo_coeff, ci0, verbose)

    def _eig(self, mat, b0, b1, orbsym=None):
        # self.mo_coeff.orbsym is initialized in kernel function
        if orbsym is None:
            orbsym = self.mo_coeff.orbsym[b0:b1]
        return eig(mat, orbsym)

    def sort_mo_by_irrep(self, cas_irrep_nocc,
                         cas_irrep_ncore=None, mo_coeff=None, s=None):
        '''Select active space based on symmetry information.
        See also :func:`pyscf.mcscf.addons.sort_mo_by_irrep`
        '''
        if mo_coeff is None: mo_coeff = self.mo_coeff
        return addons.sort_mo_by_irrep(self, mo_coeff, cas_irrep_nocc,
                                       cas_irrep_ncore, s)

CASCI = SymAdaptedCASCI

def eig(mat, orbsym):
    orbsym = numpy.asarray(orbsym)
    norb = mat.shape[0]
    e = numpy.zeros(norb)
    c = numpy.zeros((norb,norb))
    for ir in set(orbsym):
        lst = numpy.where(orbsym == ir)[0]
        if len(lst) > 0:
            w, v = scf.hf.eig(mat[lst[:,None],lst], None)
            e[lst] = w
            c[lst[:,None],lst] = v
    return e, c

def label_symmetry_(mc, mo_coeff, ci0=None):
    log = logger.Logger(mc.stdout, mc.verbose)
    #irrep_name = mc.mol.irrep_name
    irrep_name = mc.mol.irrep_id
    s = mc._scf.get_ovlp()
    ncore = mc.ncore
    nocc = ncore + mc.ncas
    try:
        orbsym = scf.hf_symm.get_orbsym(mc._scf.mol, mo_coeff, s, True)
    except ValueError:
        log.warn('mc1step_symm symmetrizes input orbitals')
        mo_cor = symm.symmetrize_space(mc.mol, mo_coeff[:,    :ncore], s=s, check=False)
        mo_act = symm.symmetrize_space(mc.mol, mo_coeff[:,ncore:nocc], s=s, check=False)
        mo_vir = symm.symmetrize_space(mc.mol, mo_coeff[:,nocc:     ], s=s, check=False)
        mo_coeff = numpy.hstack((mo_cor,mo_act,mo_vir))
        orbsym = symm.label_orb_symm(mc.mol, irrep_name,
                                     mc.mol.symm_orb, mo_coeff, s=s)
    mo_coeff_with_orbsym = lib.tag_array(mo_coeff, orbsym=orbsym)

    active_orbsym = getattr(mc.fcisolver, 'orbsym', [])
    if (not getattr(active_orbsym, '__len__', None)) or len(active_orbsym) == 0:
        mc.fcisolver.orbsym = orbsym[ncore:nocc]
    log.debug('Active space irreps %s', str(mc.fcisolver.orbsym))

    wfnsym = 0
    if getattr(mc.fcisolver, 'wfnsym', None) is not None:
        wfnsym = mc.fcisolver.wfnsym

    elif ci0 is None:
        # Guess wfnsym based on HF determinant.  mo_coeff may not be HF
        # canonical orbitals.  Some checks are needed to ensure that mo_coeff
        # are derived from the symmetry adapted SCF calculations.
        if mo_coeff is mc._scf.mo_coeff:
            wfnsym = 0
            orbsym_in_d2h = numpy.asarray(orbsym) % 10  # convert to D2h irreps
            for ir in orbsym_in_d2h[mc._scf.mo_occ == 1]:
                wfnsym ^= ir
            mc.fcisolver.wfnsym = wfnsym
            log.debug('Set CASCI wfnsym %s based on HF determinant', wfnsym)
        elif getattr(mo_coeff, 'orbsym', None) is not None:  # It may be reordered SCF orbitals
            cas_orb = mo_coeff[:,ncore:nocc]
            s = reduce(numpy.dot, (cas_orb.conj().T, mc._scf.get_ovlp(), mc._scf.mo_coeff))
            if numpy.all(numpy.max(s, axis=1) > 1-1e-9):
                idx = numpy.argmax(s, axis=1)
                cas_orbsym_in_d2h = numpy.asarray(orbsym[ncore:nocc]) % 10
                cas_occ = mc._scf.mo_occ[idx]
                wfnsym = 0
                for ir in cas_orbsym_in_d2h[cas_occ == 1]:
                    wfnsym ^= ir
                mc.fcisolver.wfnsym = wfnsym
                log.debug('Active space are constructed from canonical SCF '
                          'orbitals %s', idx)
                log.debug('Set CASCI wfnsym %s based on HF determinant', wfnsym)

    elif getattr(mc.fcisolver, 'guess_wfnsym', None):
        wfnsym = mc.fcisolver.guess_wfnsym(mc.ncas, mc.nelecas, ci0, verbose=log)
        log.debug('CASCI wfnsym %s (based on CI initial guess)', wfnsym)

    if isinstance(wfnsym, (int, numpy.integer)):
        wfnsym = symm.irrep_id2name(mc.mol.groupname, wfnsym)

    log.info('Active space CI wfn symmetry = %s', wfnsym)

    return mo_coeff_with_orbsym

scf.hf_symm.RHF.CASCI = scf.hf_symm.ROHF.CASCI = lib.class_as_method(SymAdaptedCASCI)
scf.uhf_symm.UHF.CASCI = None


if __name__ == '__main__':
    from pyscf import gto
    mol = gto.Mole()
    mol.verbose = 0
    mol.output = None#"out_h2o"
    mol.atom = [
        ['O', ( 0., 0.    , 0.   )],
        ['H', ( 0., -0.757, 0.587)],
        ['H', ( 0., 0.757 , 0.587)],]

    mol.basis = {'H': 'sto-3g',
                 'O': '6-31g',}
    mol.symmetry = 1
    mol.build()

    m = scf.RHF(mol)
    ehf = m.scf()
    mc = CASCI(m, 4, 4)
    emc = mc.casci()[0]
    print(ehf, emc, emc-ehf)
    #-75.9577817425 -75.9624554777 -0.00467373522233
    print(emc+75.9624554777)

    mc = CASCI(m, 4, (3,1))
    mc.fcisolver = fci.direct_spin1
    emc = mc.casci()[0]
    print(emc - -75.439016172976)

    mol.spin = 2
    m = scf.RHF(mol).run()
    mc = CASCI(m, 4, 4).run()
    print(mc.e_tot - -75.46992364325132)
