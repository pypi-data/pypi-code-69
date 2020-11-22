"""Set-up as in Sakov's 2008 article in Tellus
"A deterministic formulation of the ensemble Kalman filter:
an alternative to ensemble square root filters",

Similar to the 1998 MWR article by E. N. Lorenz and K. A. Emanuel:
'Optimal Sites for Supplementary Weather Observations:
Simulation with a Small Model',
except that the observations are from the entire state.

This HMM is used (with small variations) in many DA papers,
some of which are mentioned below.
"""

import numpy as np
import dapper as dpr

from dapper.mods.Lorenz96 import step, dstep_dx, x0, Tplot, LPs
from dapper.tools.localization import nd_Id_localization

# Sakov uses K=300000, BurnIn=1000*0.05
t = dpr.Chronology(0.05, dkObs=1, KObs=1000, Tplot=Tplot, BurnIn=2*Tplot)

Nx = 40
x0 = x0(Nx)

Dyn = {
    'M': Nx,
    'model': step,
    'linear': dstep_dx,
    'noise': 0
}

X0 = dpr.GaussRV(mu=x0, C=0.001)

jj = np.arange(Nx)  # obs_inds
Obs = dpr.partial_Id_Obs(Nx, jj)
Obs['noise'] = 1
Obs['localizer'] = nd_Id_localization((Nx,), (2,))

HMM = dpr.HiddenMarkovModel(Dyn, Obs, t, X0)

HMM.liveplotters = LPs(jj)


####################
# Suggested tuning
####################

# Reproduce Table1 of sakov2008deterministic        # Expected rmse.a:
# --------------------------------------------------------------------------------
# xps += EnKF('PertObs'        ,N=40, infl=1.06)               # 0.22
# xps += EnKF('DEnKF'          ,N=40, infl=1.01)               # 0.18
# xps += EnKF('PertObs'        ,N=28, infl=1.08)               # 0.24
# xps += EnKF('Sqrt'           ,N=24, infl=1.013,rot=True)     # 0.18
#
# Other analysis schemes:
# xps += EnKF('Serial'         ,N=28, infl=1.02,rot=True)      # 0.18
# xps += EnKF('Serial ESOPS'   ,N=28, infl=1.02)               # 0.18
# xps += EnKF('Serial Stoch'   ,N=28, infl=1.08)               # 0.24
#
# EnKF-N
# xps += EnKF_N(N=24,rot=True)                                 # 0.21
# xps += EnKF_N(N=24,rot=True,xN=2.0)                          # 0.18
#
# Baseline methods
# xps += Climatology()                                         # 3.6
# xps += OptInterp()                                           # 0.95
# xps += Var3D(xB=0.02)                                        # 0.41
# xps += ExtKF(infl=10)                                        # 0.24

# Reproduce LETKF scores from bocquet2011ensemble fig 6:
# --------------------------------------------------------------------------------
# xps += LETKF(N=6,rot=True,infl=1.05,loc_rad=4,taper='Step')  #
# Other localized:
# xps += LETKF(         N=7,rot=True,infl=1.04,loc_rad=4)      # 0.22
# xps += SL_EAKF(       N=7,rot=True,infl=1.07,loc_rad=6)      # 0.23

# Reproduce Table 3 (IEnKF) from sakov2012iterative
# --------------------------------------------------------------------------------
# HMM.t.dkObs = 12
# xps += iEnKS('Sqrt' ,N=25,Lag=1,nIter=10,infl=1.2,rot=1)     # 0.46
# xps += iEnKS('Sqrt' ,N=25,Lag=1,nIter=10,xN=2.0  ,rot=1)     # 0.46

# Reproduce Fig 3 of Bocquet'2015 "expanding"
# --------------------------------------------------------------------------------
# xps += EnKF('Sqrt',N=20,rot=True,infl=1.04)                  # 0.20
# # use infl=1.10 with dkObs=3
# # use infl=1.40 with dkObs=5
# xps += EnKF_N(N=20)                                          # 0.24
# xps += EnKF_N(N=20,xN=2)                                     # 0.19
# # Also try quasi-linear regime:
# t = Chronology(0.01,dkObs=1,...)

# Reproduce Bocquet/Sakov'2013 "Joint...", Fig 4, i.e. dtObs=0.2:
# xps += iEnKS('Sqrt', N=20, Lag=4, xN=2) # 0.31
# xps += Var4D(Lag=1,xB=0.2)              # 0.46
# xps += Var4D(Lag=2,xB=0.1)              # 0.39
# xps += Var4D(Lag=4,xB=0.02)             # 0.37
# Cannot reproduce Fig4's reported 4D-Var scores for L>4. Example:
# xps += Var4D(Lag=6,xB=0.015)            # 0.385 Boc13 reports 0.33

# Tests with the Particle filter, with N=3000, KObs=10'000.
# da_method  NER  reg  |  rmse.a   rmv.a
# --------- ----  ---  -  ------  ------
# PartFilt  0.05  1.2  |  0.35    0.40
# PartFilt  0.05  1.6  |  0.41    0.45
# PartFilt  0.5   0.7  |  0.26    0.29
# PartFilt  0.5   0.9  |  0.30    0.34
# PartFilt  0.5   1.2  |  0.36    0.40
# Using NER=0.9 yielded rather poor results.
