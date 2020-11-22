#!/usr/bin/env python3
# -*- coding", t)
"""
Created on Fri Apr 10 14:22:36 2020

@author", t)
"""


import timeit
from ansitable import ANSITable, Column

N = 1000

table = ANSITable(
    Column("Operation", headalign="^"),
    Column("Time (μs)", headalign="^", fmt="{:.2f}"),
    border="thick")

def result(op, t):
    global table

    table.row(op, t/N*1e6)
# ------------------------------------------------------------------------- #

transforms_setup = '''
from spatialmath import SE3
from spatialmath import base

import numpy as np
from collections import namedtuple
Rt = namedtuple('Rt', 'R t')
X1 = SE3.Rand()
X2 = SE3.Rand()
T1 = X1.A
T2 = X2.A
R1 = base.t2r(T1)
R2 = base.t2r(T2)
t1 = base.transl(T1)
t2 = base.transl(T2)
Rt1 = Rt(R1, t1)
Rt2 = Rt(R2, t2)
v = np.r_[1,2,3]
v2 = np.r_[1,2,3, 1]
'''
t = timeit.timeit(stmt='base.getvector(0.2)', setup=transforms_setup, number=N)
result("getvector(x)", t)

t = timeit.timeit(stmt='base.rotx(0.2, unit="rad")', setup=transforms_setup, number=N)
result("base.rotx", t)

t = timeit.timeit(stmt='base.trotx(0.2, unit="rad")', setup=transforms_setup, number=N)
result("base.trotx", t)

t = timeit.timeit(stmt='base.t2r(T1)', setup=transforms_setup, number=N)
result("base.t2r", t)

t = timeit.timeit(stmt='base.r2t(R1)', setup=transforms_setup, number=N)
result("base.r2t", t)

t = timeit.timeit(stmt='T1 @ T2', setup=transforms_setup, number=N)
result("4x4 @", t)

t = timeit.timeit(stmt='T1[:3,:3] @ T2[:3,:3] + T1[:3,:3] @ T2[:3,3]', setup=transforms_setup, number=N)
result("R1*R2, R1*t", t)

t = timeit.timeit(stmt='(Rt1.R @ Rt2.R, Rt1.R @ Rt2.t)', setup=transforms_setup, number=N)
result("T1 * T2 (R, t)", t)

t = timeit.timeit(stmt='base.trinv(T1)', setup=transforms_setup, number=N)
result("base.trinv", t)

t = timeit.timeit(stmt='(Rt1.R.T, -Rt1.R.T @ Rt1.t)', setup=transforms_setup, number=N)
result("base.trinv (R,t)", t)

t = timeit.timeit(stmt='np.linalg.inv(T1)', setup=transforms_setup, number=N)
result("np.linalg.inv", t)

t = timeit.timeit(stmt='T1 @ v2', setup=transforms_setup, number=N)
result("(4,4) * (4,)", t)

# ------------------------------------------------------------------------- #
table.rule()

t = timeit.timeit(stmt='SE3()', setup=transforms_setup, number=N)
result("SE3()", t)

t = timeit.timeit(stmt='SE3.Rx(0.2)', setup=transforms_setup, number=N)
result("SE3.Rx()", t)

t = timeit.timeit(stmt='T1[:3,:3]', setup=transforms_setup, number=N)
result("T1[:3,:3]", t)

t = timeit.timeit(stmt='X1.A', setup=transforms_setup, number=N)
result("SE3.A", t)

t = timeit.timeit(stmt='SE3(T1)', setup=transforms_setup, number=N)
result("SE3(T1)", t)

t = timeit.timeit(stmt='SE3(T1, check=False)', setup=transforms_setup, number=N)
result("SE3(T1 check=False)", t)

t = timeit.timeit(stmt='SE3([T1], check=False)', setup=transforms_setup, number=N)
result("SE3([T1])", t)

t = timeit.timeit(stmt='X1 * X2', setup=transforms_setup, number=N)
result("SE3 * SE3", t)

t = timeit.timeit(stmt='X1.inv()', setup=transforms_setup, number=N)
result("SE3.inv", t)

t = timeit.timeit(stmt='X1 * v', setup=transforms_setup, number=N)
result("SE3 * v", t)

t = timeit.timeit(stmt='a = X1.log()', setup=transforms_setup, number=N)
result("SE3.log()", t)

# ------------------------------------------------------------------------- #
quat_setup = '''
from spatialmath import base
from spatialmath import UnitQuaternion
import numpy as np
q1 = base.rand()
q2 = base.rand()
v = np.r_[1,2,3]
Q1 = UnitQuaternion.Rx(0.2)
Q2 = UnitQuaternion.Ry(0.3)
'''
table.rule()

t = timeit.timeit(stmt='a = UnitQuaternion()', setup=quat_setup, number=N)
result("UnitQuaternion() ", t)

t = timeit.timeit(stmt='a = UnitQuaternion.Rx(0.2)', setup=quat_setup, number=N)
result("UnitQuaternion.Rx ", t)

t = timeit.timeit(stmt='a = Q1 * Q2', setup=quat_setup, number=N)
result("UnitQuaternion * UnitQuaternion", t)

t = timeit.timeit(stmt='a = Q1 * v', setup=quat_setup, number=N)
result("UnitQuaternion * v", t)

t = timeit.timeit(stmt='a = base.qqmul(q1,q2)', setup=quat_setup, number=N)
result("base.qqmul", t)

t = timeit.timeit(stmt='a = base.qvmul(q1,v)', setup=quat_setup, number=N)
result("base.qvmul", t)



# ------------------------------------------------------------------------- #
twist_setup = '''
from spatialmath import SE3, Twist3
from spatialmath import base
import numpy as np
t1 = SE3.Rand().Twist3()
t2 = SE3.Rand().Twist3()
T1 = SE3.Rand()
s = [1,2,3,4,5,6]
v = [1,2,3]
'''
table.rule()
t = timeit.timeit(stmt='a = Twist3()', setup=twist_setup, number=N)
result("Twist3()", t)

t = timeit.timeit(stmt='a = T1.Twist3()', setup=twist_setup, number=N)
result("SE3.Twist3()", t)

t = timeit.timeit(stmt='a = t1 * t2', setup=twist_setup, number=N)
result("Twist3 * Twist3", t)

t = timeit.timeit(stmt='a = t1.inv()', setup=twist_setup, number=N)
result("Twist3.inv()", t)

t = timeit.timeit(stmt='a = t1.Ad()', setup=twist_setup, number=N)
result("Twist3.Ad()", t)

t = timeit.timeit(stmt='a = t1.exp(1)', setup=twist_setup, number=N)
result("Twist3.Exp()", t)

t = timeit.timeit(stmt='a = base.skewa(v)', setup=twist_setup, number=N)
result("skew", t)

t = timeit.timeit(stmt='a = base.skewa(s)', setup=twist_setup, number=N)
result("skewa", t)



table.print()