"""Illustrate usage of DAPPER to benchmark multiple DA methods."""

import dapper as dpr
dpr.set_seed(3000)

##############################
# DA method configurations
##############################
xps = dpr.xpList()

from dapper.mods.Lorenz63.sakov2012 import HMM     # Expected rmse.a:
xps += dpr.Climatology()                                      # 7.6
xps += dpr.OptInterp()                                        # 1.25
xps += dpr.Var3D(xB=0.1)                                      # 1.03
xps += dpr.ExtKF(infl=90)                                     # 0.87
xps += dpr.EnKF('Sqrt',    N=3,    infl=1.30)                 # 0.82
xps += dpr.EnKF('Sqrt',    N=10,   infl=1.02, rot=True)       # 0.63
xps += dpr.EnKF('PertObs', N=500,  infl=0.95, rot=False)      # 0.56
xps += dpr.EnKF_N(         N=10,              rot=True)       # 0.54
xps += dpr.iEnKS('Sqrt',   N=10,   infl=1.02, rot=True)       # 0.31
xps += dpr.PartFilt(       N=100,  reg=2.4,   NER=0.3)        # 0.38
xps += dpr.PartFilt(       N=800,  reg=0.9,   NER=0.2)        # 0.28
# xps += dpr.PartFilt(       N=4000, reg=0.7  , NER=0.05)       # 0.27
# xps += dpr.PFxN(xN=1000,   N=30  , Qs=2     , NER=0.2)        # 0.56

# from dapper.mods.Lorenz96.sakov2008 import HMM    # Expected rmse.a:
# xps += dpr.Climatology()                                     # 3.6
# xps += dpr.OptInterp()                                       # 0.95
# xps += dpr.Var3D(xB=0.02)                                    # 0.41
# xps += dpr.ExtKF(infl=6)                                     # 0.24
# xps += dpr.EnKF('PertObs', N=40, infl=1.06)                  # 0.22
# xps += dpr.EnKF('Sqrt',    N=28, infl=1.02, rot=True)        # 0.18

# xps += dpr.EnKF_N(         N=24, rot=True)                   # 0.21
# xps += dpr.EnKF_N(         N=24, rot=True, xN=2)             # 0.18
# xps += dpr.iEnKS('Sqrt',   N=40, infl=1.01, rot=True)        # 0.17

# xps += dpr.LETKF(          N=7,  infl=1.04, rot=True, loc_rad=4)  # 0.22
# xps += dpr.SL_EAKF(        N=7,  infl=1.07, rot=True, loc_rad=6)  # 0.23

# Other models (suitable xp's listed in HMM files):
# from dapper.mods.LA           .evensen2009 import HMM
# from dapper.mods.KS           .bocquet2019 import HMM
# from dapper.mods.LotkaVolterra.settings101 import HMM

##############################
# Run experiment
##############################
# Adjust experiment duration
HMM.t.BurnIn = 2
HMM.t.T = 50

# Assimilate (for each xp in xps)
xps.launch(HMM, liveplots=False)

# Print results
print(xps.tabulate_avrgs())
