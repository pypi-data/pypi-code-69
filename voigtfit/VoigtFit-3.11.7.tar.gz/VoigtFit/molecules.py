# -*- coding: UTF-8 -*-
"""
A compilation of molecular data and labels as well as a functions to calculate
ionization diagrams and occupation rates.
The variables `H2` and `CO` are dictionaries containing the lines associated
to each molecular band, e.g., AX(1-0) for CO or BX(0-0) for H2 Lyman band.
"""
__author__ = 'Jens-Kristian Krogager'

import numpy as np


CO_full_labels = {
    'AX(0-0)': "${\\rm CO\ A}^1\\Pi(0) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(1-0)': "${\\rm CO\ A}^1\\Pi(1) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(2-0)': "${\\rm CO\ A}^1\\Pi(2) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(3-0)': "${\\rm CO\ A}^1\\Pi(3) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(4-0)': "${\\rm CO\ A}^1\\Pi(4) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(5-0)': "${\\rm CO\ A}^1\\Pi(5) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(6-0)': "${\\rm CO\ A}^1\\Pi(6) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(7-0)': "${\\rm CO\ A}^1\\Pi(7) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(8-0)': "${\\rm CO\ A}^1\\Pi(8) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(9-0)': "${\\rm CO\ A}^1\\Pi(9) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(10-0)': "${\\rm CO\ A}^1\\Pi(10) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'AX(11-0)': "${\\rm CO\ A}^1\\Pi(11) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'CX(0-0)': "${\\rm CO\ C}^1\\Sigma(0) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'dX(5-0)': "${\\rm CO\ d}^3\\Delta(5) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$",
    'eX(1-0)': "${\\rm CO\ e}^3\\Sigma^-(1) \\leftarrow {\\rm X}^1\\Sigma^+(\\nu=0)$"
}

CO_labels = {'COJ0_1544.44': 'AX(0-0)',
             'COJ0_1509.74': 'AX(1-0)',
             'COJ0_1477.56': 'AX(2-0)',
             'COJ0_1447.35': 'AX(3-0)',
             'COJ0_1419.04': 'AX(4-0)',
             'COJ0_1392.52': 'AX(5-0)',
             'COJ0_1367.62': 'AX(6-0)',
             'COJ0_1344.18': 'AX(7-0)',
             'COJ0_1322.15': 'AX(8-0)',
             'COJ0_1301.40': 'AX(9-0)',
             'COJ0_1281.86': 'AX(10-0)',
             'COJ0_1263.43': 'AX(11-0)',
             'COJ0_1087.86': 'CX(0-0)',
             'COJ0_1510.34': 'dX(5-0)',
             'COJ0_1543.17': 'eX(1-0)',
             'COJ0_1543.00': 'eX(1-0)'
             }

H2_full_labels = {
    'BX(0-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(0) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(1-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(1) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(2-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(2) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(3-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(3) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(4-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(4) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(5-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(5) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(6-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(6) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(7-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(7) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(8-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(8) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(9-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(9) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(10-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(10) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(11-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(11) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(12-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(12) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(13-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(13) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(14-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(14) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(15-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(15) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(16-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(16) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(17-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(17) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(18-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(18) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'BX(19-0)': "${\\rm H_2\ B}^1\\Sigma_u^+(19) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'CX(0-0)': "${\\rm H_2\ C}^1\\Pi_u(0) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'CX(1-0)': "${\\rm H_2\ C}^1\\Pi_u(1) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'CX(2-0)': "${\\rm H_2\ C}^1\\Pi_u(2) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'CX(3-0)': "${\\rm H_2\ C}^1\\Pi_u(3) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'CX(4-0)': "${\\rm H_2\ C}^1\\Pi_u(4) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
    'CX(5-0)': "${\\rm H_2\ C}^1\\Pi_u(5) \\leftarrow {\\rm X}^1\\Sigma_g^+(\\nu=0)$",
}

H2_labels = {'H2J0_917.25': 'BX(18-0)',
             'H2J0_1092.20': 'BX(1-0)',
             'H2J0_929.53': 'CX(4-0)',
             'H2J0_946.17': 'BX(14-0)',
             'H2J0_971.99': 'BX(11-0)',
             'H2J0_964.98': 'CX(2-0)',
             'H2J0_1049.37': 'BX(4-0)',
             'H2J0_1012.81': 'BX(7-0)',
             'H2J0_1001.82': 'BX(8-0)',
             'H2J0_981.44': 'BX(10-0)',
             'H2J0_985.63': 'CX(1-0)',
             'H2J0_931.06': 'BX(16-0)',
             'H2J0_1077.14': 'BX(2-0)',
             'H2J0_910.82': 'BX(19-0)',
             'H2J0_938.47': 'BX(15-0)',
             'H2J0_954.41': 'BX(13-0)',
             'H2J0_914.40': 'CX(5-0)',
             'H2J0_1062.88': 'BX(3-0)',
             'H2J0_1036.55': 'BX(5-0)',
             'H2J0_946.43': 'CX(3-0)',
             'H2J0_991.38': 'BX(9-0)',
             'H2J0_1008.55': 'CX(0-0)',
             'H2J0_1108.13': 'BX(0-0)',
             'H2J0_1024.37': 'BX(6-0)',
             'H2J0_923.98': 'BX(17-0)',
             'H2J0_962.98': 'BX(12-0)'
             }


H2 = {'BX(0-0)': [['H2J0_1108.13'],
                  ['H2J1_1110.06', 'H2J1_1108.63'],
                  ['H2J2_1112.50', 'H2J2_1110.12'],
                  ['H2J3_1115.90', 'H2J3_1112.58'],
                  ['H2J4_1120.25', 'H2J4_1116.01'],
                  ['H2J5_1125.54', 'H2J5_1120.40'],
                  ['H2J6_1131.75', 'H2J6_1125.73'],
                  ['H2J7_1151.64']],

      'BX(1-0)': [['H2J0_1092.20'],
                  ['H2J1_1094.05', 'H2J1_1092.73'],
                  ['H2J2_1096.44', 'H2J2_1094.24'],
                  ['H2J3_1099.79', 'H2J3_1096.73'],
                  ['H2J4_1104.08', 'H2J4_1100.16'],
                  ['H2J5_1109.31', 'H2J5_1104.55'],
                  ['H2J6_1115.46', 'H2J6_1109.86'],
                  ['H2J7_1134.90']],

      'BX(2-0)': [['H2J0_1077.14'],
                  ['H2J1_1078.93', 'H2J1_1077.70'],
                  ['H2J2_1081.27', 'H2J2_1079.23'],
                  ['H2J3_1084.56', 'H2J3_1081.71'],
                  ['H2J4_1088.80', 'H2J4_1085.15'],
                  ['H2J5_1093.95', 'H2J5_1089.51'],
                  ['H2J6_1100.02', 'H2J6_1094.80'],
                  ['H2J7_1119.03']],

      'BX(3-0)': [['H2J0_1062.88'],
                  ['H2J1_1064.61', 'H2J1_1063.46'],
                  ['H2J2_1066.90', 'H2J2_1064.99'],
                  ['H2J3_1070.14', 'H2J3_1067.48'],
                  ['H2J4_1074.31', 'H2J4_1070.90'],
                  ['H2J5_1079.40', 'H2J5_1075.24'],
                  ['H2J6_1085.38', 'H2J6_1080.49'],
                  ['H2J7_1103.98']],

      'BX(4-0)': [['H2J0_1049.37'],
                  ['H2J1_1051.03', 'H2J1_1049.96'],
                  ['H2J2_1053.28', 'H2J2_1051.50'],
                  ['H2J3_1056.47', 'H2J3_1053.98'],
                  ['H2J4_1060.58', 'H2J4_1057.38'],
                  ['H2J5_1065.60', 'H2J5_1061.70'],
                  ['H2J6_1071.50', 'H2J6_1066.91'],
                  ['H2J7_1089.71']],

      'BX(5-0)': [['H2J0_1036.55'],
                  ['H2J1_1038.16', 'H2J1_1037.15'],
                  ['H2J2_1040.37', 'H2J2_1038.69'],
                  ['H2J3_1043.50', 'H2J3_1041.16'],
                  ['H2J4_1047.55', 'H2J4_1044.54'],
                  ['H2J5_1052.50', 'H2J5_1048.83'],
                  ['H2J6_1058.32', 'H2J6_1054.00'],
                  ['H2J7_1076.16']],

      'BX(6-0)': [['H2J0_1024.37'],
                  ['H2J1_1025.94', 'H2J1_1024.99'],
                  ['H2J2_1028.11', 'H2J2_1026.53'],
                  ['H2J3_1031.19', 'H2J3_1028.99'],
                  ['H2J4_1035.18', 'H2J4_1032.35'],
                  ['H2J5_1040.06', 'H2J5_1036.60'],
                  ['H2J6_1045.80', 'H2J6_1041.73'],
                  ['H2J7_1063.29']],

      'BX(7-0)': [['H2J0_1012.81'],
                  ['H2J1_1014.33', 'H2J1_1013.44'],
                  ['H2J2_1016.46', 'H2J2_1014.98'],
                  ['H2J3_1019.50', 'H2J3_1017.42'],
                  ['H2J4_1023.44', 'H2J4_1020.77'],
                  ['H2J5_1028.25', 'H2J5_1024.99'],
                  ['H2J6_1033.92', 'H2J6_1030.07'],
                  ['H2J7_1051.07']],

      'BX(8-0)': [['H2J0_1001.82'],
                  ['H2J1_1003.30', 'H2J1_1002.45'],
                  ['H2J2_1005.39', 'H2J2_1003.99'],
                  ['H2J3_1008.39', 'H2J3_1006.41'],
                  ['H2J4_1012.26', 'H2J4_1009.72'],
                  ['H2J5_1017.00', 'H2J5_1013.71'],
                  ['H2J6_1022.59', 'H2J6_1019.02'],
                  ['H2J7_1039.21']],

      'BX(9-0)': [['H2J0_991.38'],
                  ['H2J1_992.81', 'H2J1_992.02'],
                  ['H2J2_994.87', 'H2J2_993.55'],
                  ['H2J3_997.83', 'H2J3_995.97'],
                  ['H2J4_1001.66', 'H2J4_999.27'],
                  ['H2J5_1006.34', 'H2J5_1003.43'],
                  ['H2J6_1011.87', 'H2J6_1008.43'],
                  ['H2J7_1028.41']],

      'BX(10-0)': [['H2J0_981.44'],
                   ['H2J1_982.84', 'H2J1_982.07'],
                   ['H2J2_984.86', 'H2J2_983.59'],
                   ['H2J3_987.77', 'H2J3_985.96'],
                   ['H2J4_991.53', 'H2J4_989.56'],
                   ['H2J5_996.12', 'H2J5_993.49'],
                   ['H2J6_1001.91', 'H2J6_998.43'],
                   ['H2J7_1017.98']],

      'BX(11-0)': [['H2J0_971.99'],
                   ['H2J1_973.34', 'H2J1_972.63'],
                   ['H2J2_975.35', 'H2J2_974.16'],
                   ['H2J3_978.22', 'H2J3_976.55'],
                   ['H2J4_981.95', 'H2J4_979.81'],
                   ['H2J5_986.52', 'H2J5_983.90'],
                   ['H2J6_991.92', 'H2J6_988.81'],
                   ['H2J7_998.11']],

      'BX(12-0)': [['H2J0_962.98'],
                   ['H2J1_964.31', 'H2J1_963.61'],
                   ['H2J2_966.28', 'H2J2_965.05'],
                   ['H2J3_969.09', 'H2J3_967.68'],
                   ['H2J4_972.69', 'H2J4_970.84'],
                   ['H2J5_977.46', 'H2J5_974.89'],
                   ['H2J6_982.73', 'H2J6_979.76'],
                   ['H2J7_988.84']],

      'BX(13-0)': [['H2J0_954.41'],
                   ['H2J1_955.71', 'H2J1_955.07'],
                   ['H2J2_957.65', 'H2J2_956.58'],
                   ['H2J3_960.45', 'H2J3_958.95'],
                   ['H2J4_964.09', 'H2J4_962.15'],
                   ['H2J5_968.56', 'H2J5_966.18'],
                   ['H2J6_973.83', 'H2J6_971.00'],
                   ['H2J7_989.32']],

      'BX(14-0)': [['H2J0_946.17'],
                   ['H2J1_947.51', 'H2J1_946.98'],
                   ['H2J2_949.35', 'H2J2_948.47'],
                   ['H2J3_952.27', 'H2J3_950.82'],
                   ['H2J4_955.85', 'H2J4_954.00'],
                   ['H2J5_960.27', 'H2J5_958.01'],
                   ['H2J6_965.48', 'H2J6_962.82'],
                   ['H2J7_980.76']],

      'BX(15-0)': [['H2J0_938.47'],
                   ['H2J1_939.71', 'H2J1_939.12'],
                   ['H2J2_941.60', 'H2J2_940.63'],
                   ['H2J3_944.33', 'H2J3_942.96'],
                   ['H2J4_947.89', 'H2J4_946.12'],
                   ['H2J5_952.25', 'H2J5_950.07'],
                   ['H2J6_957.41', 'H2J6_954.70'],
                   ['H2J7_972.44']],

      'BX(16-0)': [['H2J0_931.06'],
                   ['H2J1_932.27', 'H2J1_931.73'],
                   ['H2J2_934.14', 'H2J2_933.24'],
                   ['H2J3_936.86', 'H2J3_935.58'],
                   ['H2J4_940.39', 'H2J4_938.73'],
                   ['H2J5_944.72', 'H2J5_942.69'],
                   ['H2J6_949.84', 'H2J6_947.43'],
                   ['H2J7_964.70']],

      'BX(17-0)': [['H2J0_923.98'],
                   ['H2J1_925.17', 'H2J1_924.64'],
                   ['H2J2_927.02', 'H2J2_926.13'],
                   ['H2J3_929.69', 'H2J3_928.44'],
                   ['H2J4_933.17', 'H2J4_931.54'],
                   ['H2J5_937.44', 'H2J5_935.32'],
                   ['H2J6_942.48', 'H2J6_940.49'],
                   ['H2J7_956.99']],

      'BX(18-0)': [['H2J0_917.25'],
                   ['H2J1_918.41', 'H2J1_917.92'],
                   ['H2J2_920.24', 'H2J2_919.42'],
                   ['H2J3_922.89', 'H2J3_921.73'],
                   ['H2J4_926.35', 'H2J4_924.85'],
                   ['H2J5_930.61', 'H2J5_928.76'],
                   ['H2J6_935.63', 'H2J6_933.44'],
                   ['H2J7_950.12']],

      'BX(19-0)': [['H2J0_910.82'],
                   ['H2J1_911.97', 'H2J1_911.48'],
                   ['H2J2_913.77', 'H2J2_912.95'],
                   ['H2J3_916.38', 'H2J3_915.21'],
                   ['H2J4_919.79', 'H2J4_918.15'],
                   ['H2J5_923.96', 'H2J5_922.48'],
                   ['H2J6_928.78', 'H2J6_927.05'],
                   ['H2J7_943.55']],

      'CX(0-0)': [['H2J0_1008.55'],
                  ['H2J1_1009.77', 'H2J1_1008.50'],
                  ['H2J2_1012.17', 'H2J2_1010.94', 'H2J2_1009.02'],
                  ['H2J3_1014.50', 'H2J3_1012.68', 'H2J3_1010.13'],
                  ['H2J4_1017.39', 'H2J4_1014.98', 'H2J4_1011.81'],
                  ['H2J5_1020.80', 'H2J5_1017.83', 'H2J5_1014.24'],
                  ['H2J6_1024.73', 'H2J6_1021.21', 'H2J6_1016.74'],
                  ['H2J7_1039.77', 'H2J7_1035.43']],

      'CX(1-0)': [['H2J0_985.63'],
                  ['H2J1_986.80', 'H2J1_985.64'],
                  ['H2J2_989.09', 'H2J2_987.97', 'H2J2_986.24'],
                  ['H2J3_991.38', 'H2J3_989.73', 'H2J3_987.45'],
                  ['H2J4_994.23', 'H2J4_992.05', 'H2J4_988.87'],
                  ['H2J5_997.64', 'H2J5_994.92', 'H2J5_991.37'],
                  ['H2J6_1001.21', 'H2J6_998.33', 'H2J6_994.26'],
                  ['H2J7_1015.75', 'H2J7_1012.13']],

      'CX(2-0)': [['H2J0_964.98'],
                  ['H2J1_966.10', 'H2J1_965.06'],
                  ['H2J2_968.30', 'H2J2_967.28', 'H2J2_965.80'],
                  ['H2J3_970.56', 'H2J3_969.05', 'H2J3_966.78'],
                  ['H2J4_973.45', 'H2J4_971.39', 'H2J4_968.67'],
                  ['H2J5_976.55', 'H2J5_974.29', 'H2J5_971.07'],
                  ['H2J6_980.50', 'H2J6_977.73', 'H2J6_974.05'],
                  ['H2J7_994.45', 'H2J7_991.16']],

      'CX(3-0)': [['H2J0_946.43'],
                  ['H2J1_947.42', 'H2J1_946.38'],
                  ['H2J2_949.61', 'H2J2_948.62', 'H2J2_947.11'],
                  ['H2J3_951.67', 'H2J3_950.40', 'H2J3_948.42'],
                  ['H2J4_954.47', 'H2J4_952.76', 'H2J4_950.32'],
                  ['H2J5_957.82', 'H2J5_955.68', 'H2J5_952.80'],
                  ['H2J6_961.70', 'H2J6_959.15', 'H2J6_955.98'],
                  ['H2J7_975.30', 'H2J7_972.27']],

      'CX(4-0)': [['H2J0_929.53'],
                  ['H2J1_930.58', 'H2J1_929.69'],
                  ['H2J2_932.60', 'H2J2_931.78', 'H2J2_930.45'],
                  ['H2J3_934.79', 'H2J3_933.58', 'H2J3_931.81'],
                  ['H2J4_937.55', 'H2J4_935.96', 'H2J4_933.79'],
                  ['H2J5_940.88', 'H2J5_938.91', 'H2J5_936.47'],
                  ['H2J6_944.78', 'H2J6_942.42', 'H2J6_939.11'],
                  ['H2J7_958.19', 'H2J7_955.26']],

      'CX(5-0)': [['H2J0_914.40'],
                  ['H2J1_915.40', 'H2J1_914.61'],
                  ['H2J2_917.37', 'H2J2_916.62', 'H2J2_915.43'],
                  ['H2J3_919.54', 'H2J3_918.43', 'H2J3_916.88'],
                  ['H2J4_922.31', 'H2J4_920.83', 'H2J4_919.05'],
                  ['H2J5_925.66', 'H2J5_923.82', 'H2J5_921.22'],
                  ['H2J6_929.70', 'H2J6_927.36', 'H2J6_924.50'],
                  ['H2J7_942.23', 'H2J7_939.98']]
      }

CO = {
    # Nu=0:
    'AX(0-0)': [['COJ0_1544.44'],  # J=0
                ['COJ1_1544.54', 'COJ1_1544.38'],  # J=1
                ['COJ2_1544.72', 'COJ2_1544.57', 'COJ2_1544.34'],  # J=2
                ['COJ3_1544.84', 'COJ3_1544.61', 'COJ3_1544.31'],  # J=3
                ['COJ4_1544.98', 'COJ4_1544.68', 'COJ4_1544.30'],  # J=4
                ['COJ5_1545.14', 'COJ5_1544.76', 'COJ5_1544.31']],   # J=5
    # Nu=1:
    'AX(1-0)': [['COJ0_1509.74'],
                ['COJ1_1509.83', 'COJ1_1509.69'],
                ['COJ2_1510.01', 'COJ2_1509.87', 'COJ2_1509.66'],
                ['COJ3_1510.13', 'COJ3_1509.92', 'COJ3_1509.64'],
                ['COJ4_1510.27', 'COJ4_1509.99', 'COJ4_1509.64']],
    # Nu=2:
    'AX(2-0)': [['COJ0_1477.56'],
                ['COJ1_1477.64', 'COJ1_1477.51'],
                ['COJ2_1477.81', 'COJ2_1477.68', 'COJ2_1477.47'],
                ['COJ3_1477.93', 'COJ3_1477.72', 'COJ3_1477.45'],
                ['COJ4_1478.06', 'COJ4_1477.79', 'COJ4_1477.45']],
    # Nu=3:
    'AX(3-0)': [['COJ0_1447.35'],
                ['COJ1_1447.43', 'COJ1_1447.30'],
                ['COJ2_1447.59', 'COJ2_1447.46', 'COJ2_1447.27'],
                ['COJ3_1447.70', 'COJ3_1447.51', 'COJ3_1447.25'],
                ['COJ4_1447.83', 'COJ4_1447.58', 'COJ4_1447.25']],
    # Nu=4:
    'AX(4-0)': [['COJ0_1419.04'],
                ['COJ1_1419.12', 'COJ1_1419.00'],
                ['COJ2_1419.27', 'COJ2_1419.15', 'COJ2_1418.97'],
                ['COJ3_1419.38', 'COJ3_1419.20', 'COJ3_1418.96'],
                ['COJ4_1419.51', 'COJ4_1419.27', 'COJ4_1418.97']],
    # Nu=5:
    'AX(5-0)': [['COJ0_1392.52'],
                ['COJ1_1392.60', 'COJ1_1392.48'],
                ['COJ2_1392.74', 'COJ2_1392.63', 'COJ2_1392.46'],
                ['COJ3_1392.85', 'COJ3_1392.68', 'COJ3_1392.45'],
                ['COJ4_1392.98', 'COJ4_1392.75', 'COJ4_1392.46']],
    # Nu=6:
    'AX(6-0)': [['COJ0_1367.62'],
                ['COJ1_1367.69', 'COJ1_1367.58'],
                ['COJ2_1367.83', 'COJ2_1367.73', 'COJ2_1367.56'],
                ['COJ3_1367.94', 'COJ3_1367.78', 'COJ3_1367.56'],
                ['COJ4_1368.07', 'COJ4_1367.85', 'COJ4_1367.58'],
                ['COJ5_1368.21', 'COJ5_1367.94', 'COJ5_1367.61']],
    # Nu=7:
    'AX(7-0)': [['COJ0_1344.18'],
                ['COJ1_1344.25', 'COJ1_1344.15'],
                ['COJ2_1344.39', 'COJ2_1344.29', 'COJ2_1344.13'],
                ['COJ3_1344.49', 'COJ3_1344.34', 'COJ3_1344.13'],
                ['COJ4_1344.62', 'COJ4_1344.41', 'COJ4_1344.15'],
                ['COJ5_1344.76', 'COJ5_1344.49', 'COJ5_1344.18']],
    # Nu=8:
    'AX(8-0)': [['COJ0_1322.15'],
                ['COJ1_1322.21', 'COJ1_1322.11'],
                ['COJ2_1322.35', 'COJ2_1322.25', 'COJ2_1322.10'],
                ['COJ3_1322.45', 'COJ3_1322.30', 'COJ3_1322.10'],
                ['COJ4_1322.57', 'COJ4_1322.37', 'COJ4_1322.13'],
                ['COJ5_1322.71', 'COJ5_1322.46', 'COJ5_1322.17']],
    # Nu=9:
    'AX(9-0)': [['COJ0_1301.40'],
                ['COJ1_1301.46', 'COJ1_1301.37'],
                ['COJ2_1301.59', 'COJ2_1301.50', 'COJ2_1301.36'],
                ['COJ3_1301.70', 'COJ3_1301.55', 'COJ3_1301.37'],
                ['COJ4_1301.82', 'COJ4_1301.63', 'COJ4_1301.39'],
                ['COJ5_1301.95', 'COJ5_1301.72', 'COJ5_1301.43']],
    # Nu=10:
    'AX(10-0)': [['COJ0_1281.86'],
                 ['COJ1_1281.92', 'COJ1_1281.83'],
                 ['COJ2_1282.05', 'COJ2_1281.96', 'COJ2_1281.83'],
                 ['COJ3_1282.15', 'COJ3_1282.02', 'COJ3_1281.84'],
                 ['COJ4_1282.27', 'COJ4_1282.09', 'COJ4_1281.84'],
                 ['COJ5_1282.40', 'COJ5_1282.18', 'COJ5_1281.91']],
    # Nu=11:
    'AX(11-0)': [['COJ0_1263.43'],
                 ['COJ1_1263.49', 'COJ1_1263.40'],
                 ['COJ2_1263.61', 'COJ2_1263.53', 'COJ2_1263.40'],
                 ['COJ3_1263.71', 'COJ3_1263.58', 'COJ3_1263.41'],
                 ['COJ4_1263.83', 'COJ4_1263.66', 'COJ4_1263.44'],
                 ['COJ5_1263.96', 'COJ5_1263.75', 'COJ5_1263.49']],

    'eX(1-0)': [['COJ0_1543.17', 'COJ0_1543.00'],
                ['COJ1_1543.20', 'COJ1_1542.91', 'COJ1_1543.17'],
                ['COJ2_1543.26', 'COJ2_1543.44', 'COJ2_1542.85', 'COJ2_1543.27', 'COJ2_1543.23'],
                ['COJ3_1543.35', 'COJ3_1543.66', 'COJ3_1542.83', 'COJ3_1543.37', 'COJ3_1543.33'],
                ['COJ4_1543.48', 'COJ4_1543.90', 'COJ4_1542.83', 'COJ4_1543.49', 'COJ4_1543.45']],

    'CX(0-0)': [['COJ0_1087.86'],
                ['COJ1_1087.95', 'COJ1_1087.82'],
                ['COJ2_1088.00', 'COJ2_1087.77'],
                ['COJ3_1088.04', 'COJ3_1087.72'],
                ['COJ4_1088.09', 'COJ4_1087.67']],

    'dX(5-0)': [['COJ0_1510.34'],
                ['COJ1_1510.42', 'COJ1_1510.30'],
                ['COJ2_1510.60', 'COJ2_1510.48', 'COJ2_1510.29'],
                ['COJ3_1510.74', 'COJ3_1510.56', 'COJ3_1510.31'],
                ['COJ4_1510.91', 'COJ4_1510.66', 'COJ4_1510.36']]
}


# --- Rotatinal Constants in units of cm^-1
#     E = hc * B * J(J + 1)
rotational_constant = {'H2': 60.853,
                       'CO': 1.9313,
                       'HD': 45.655
                       }

# Centrifugal constants in units of cm^-1:
centrifugal_constant = {'H2': 4.71e-2,
                        'CO': 6.12e-6
                        }

hc = 1.2398e-4         # eV.cm
k_B = 8.6173e-5        # eV/K


def energy_of_level(element, J):
    """
    Calculate the energy of a given rotational level, `J`
    for the given molecule with correction for centrigual
    expansion.
    E(J) = B_e * J * (J+1)

    Returns
    =======
    E : float
        The energy of the given level in units of K.
    """
    B_e = rotational_constant[element]
    D_e = centrifugal_constant[element]
    E = B_e * hc/k_B * J * (J+1) - hc*D_e * J**2 * (J+1)**2
    return E


def population_of_level(element, T, J):
    """
    Calculate the population of the Jth level relative to the J=0 level.
    The distribution is assumed to be an isothermal Boltzmann distribution:

    n(J) \\propto g(J) e^(-E(J) / kT)
    """
    if element not in rotational_constant.keys():
        print(" Element is not in database! ")
        print(" All elements in database are: " + ", ".join(rotational_constant.keys()))
        return None

    if element == 'H2':
        def g(J):
            Ij = J % 2
            return (2*J + 1)*(2*Ij + 1)
    elif element == 'CO':
        def g(J):
            return 2*J + 1

    E = energy_of_level(element, J)
    n_J = g(J) * np.exp(-E/T)
    return n_J


def calculate_T(element, logN1, logN2, J1, J2):
    """
    Calculate the isothermal temperature for two given column densities.
    """
    if element == 'H2':
        def g(J):
            Ij = J % 2
            return (2*J + 1)*(2*Ij + 1)
    elif element == 'CO':
        def g(J):
            return 2*J + 1

    E1 = energy_of_level(element, J1)
    E2 = energy_of_level(element, J2)
    E12 = E2-E1
    T = -E12/(np.log(10**(logN2 - logN1) * g(J1)/g(J2)))
    return T
