# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:38:51 2020

@author: Steve
"""

# Plot Planner Tool is here (for multiplots)
#    https://qed0711.github.io/plot-planner/
#
# and description is here
#   https://towardsdatascience.com/subplots-in-matplotlib-a-guide-and-tool-for-planning-your-plots-7d63fa632857 
#

import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime, timedelta
import pandas as pd
import numpy as np # needed for getting hours out of timedelta
#import numpy as np # used only for trendline
mpl.rcParams['figure.dpi'] = 300 #needed to increase resolution

"""
  Test started 26-Jun-20
  This was my very first Python program.
  At end of program are many commented lines manually dealing with time for each data point, 
    which I did for too long until I got sick of it.
  I learned from doing Violumas from data a text file, but it didn't deal with date/time
    in that I simply had days>31 after first month.
  Took that concept and used dataframes with columns for year, month...minute, made datetime
    from those for each row, subtracted start value, and also subtracted an "offset" to allow
    for time setup was off. Just add hours when it's been off to last value in txt file.
  The following values p,t,Ta,Tf,V,I were from original method.
  After data point 245, I switched to text file so I just append.
"""



# Add a trendline - didn't work first try, see ax1 section


##################################
# Making tuples of t, p, T, V, I #
##################################

p=[34.31,33.62,32.59,32.85,32.93,32.93,32.93,32.93,32.93,32.93,
33.19,33.19,33.19,33.28,33.11,33.19,33.45,33.36,33.45,33.19,
33.02,33.02,32.28,33.19,33.45,33.40,33.36,33.11,32.93,33.02,
33.02,33.19,33.02,32.93,32.93,32.93,33.11,33.28,33.11,32.93,
33.11,33.19,33.11,33.02,32.85,32.85,33.11,33.02,34.25,33.36,
32.76,32.93,32.76,32.68,32.59,32.68,32.93,32.85,32.76,32.68,
32.76,32.93,33.36,32.76,32.59,32.68,32.93,32.68,32.59,32.68,
32.42,32.68,32.24,32.33,32.59,32.24,32.07,32.33,32.24,31.81,
31.81,32.33,31.90,31.90,32.24,32.16,32.07,32.24,32.42,32.24,
32.16,32.33,32.24,32.24,32.24,32.16,31.99,31.99,32.33,32.07,
31.99,32.07,31.90,31.73,31.81,32.07,31.90,31.81,32.07,32.07,
31.90,31.81,31.90,32.07,31.99,31.73,31.99,31.81,31.73,31.99,
31.81,31.55,31.73,31.99,31.90,31.55,31.81,31.90,31.64,31.47,
31.73,31.38,31.38,31.64,31.47,31.64,31.47,31.30,31.55,31.47,
31.12,31.47,31.47,31.21,31.47,31.21,31.12,31.38,31.30,31.21,
31.38,30.95,31.30,31.04,31.12,31.04,31.04,31.21,31.21,31.30,
30.95,31.21,30.69,30.95,30.52,30.86,30.52,30.69,30.52,30.78,
30.61,30.78,30.35,30.69,30.35,30.43,30.26,30.35,29.92,30.09,
29.92,30.09,29.83,30.00,29.83,30.00,29.74,30.09,29.83,30.09,
29.83,29.74,29.66,30.09,29.83,29.92,29.74,29.92,29.66,29.92,
29.83,29.83,30.00,29.66,29.83,29.66,29.92,29.92,29.48,29.83,
29.83,29.66,29.48,29.05,29.48,29.31,28.88,29.40,29.14,29.31,
29.40,29.31,29.57,29.14,29.40,29.23,29.31,28.97,29.14,29.05,
29.05,29.05,29.14,29.05,29.48,28.97,28.88,28.79,28.88,28.54,
28.45,28.36,28.71,28.45,28.45]

TOffsetSec2H=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
0.0,0.0,0.0,0.0,1.38,1.38,1.38,1.38,1.38,1.38,
1.38,1.38,1.38,1.38,1.38,1.38,1.38,1.38,1.38,1.38,
1.38,1.38,1.38,1.38,1.38,1.38,1.38,1.38,5.92,5.92,
5.93,5.93,5.93,5.93,5.93,5.93,5.93,5.93,5.93,5.93,
5.93,5.93,9.3,9.3,9.3,9.3,9.3,9.3,9.3,9.3,
9.3,9.3,9.3,9.3,9.3,9.3,9.3,9.3,9.3,9.3,
9.3,9.3,9.3,9.3,9.3,9.3,9.3,9.3,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,13.58,
13.58,13.58,13.58,13.58,13.58]

ts = datetime(2020,6,26, 17, 30, 00)

t=[0,0.8,5.766666666666667,13.666666666666666,15.4,
 18.933333333333334,20.983333333333334,22.566666666666666,23.6,28.966666666666665,
 40.55,42.733333333333334,45.06666666666667,46.56666666666667,50.3,
 54.9,61.9,65.4,66.2,69.06666666666666,
 72.73333333333333,76.75,90.23333333333333,92.06666666666666,92.08333333333333,
 92.11666666666666,92.21666666666667,93.9,95.88333333333334,97.21666666666667,
 99.55,114.21666666666667,117.55,119.21666666666667,120.7,
 122.21666666666667,126.71666666666667,135.28333333333333,139.21666666666667,146.16666666666666,
 149.95,157.66666666666666,160.66666666666666,163.21666666666667,167.11666666666667,
 172.43333333333334,183.11666666666667,185.28333333333333,185.3,185.30277777777778,
 191.31666666666666,201.01666666666668,207.35,208.98333333333332,211.65,
 214.0,224.6,228.83333333333334,230.81666666666666,233.88333333333333,
 238.48333333333332,248.6,248.6,252.33333333333334,253.88333333333333,
 258.51666666666665,269.2,270.3666666666667,272.85,275.1166666666667,
 284.51666666666665,296.03333333333336,304.73333333333335,307.28333333333336,317.53333333333336,
 324.95,330.5,342.15,344.21666666666664,353.96666666666664,
 355.3833333333333,366.4,374.0833333333333,379.68333333333334,389.05,
 393.1666666666667,395.2,402.7,411.25,416.9,
 423.0833333333333,431.0,442.23333333333335,458.1333333333333,459.68333333333334,
 461.76666666666665,464.4166666666667,471.8666666666667,481.65,489.18333333333334,
 494.53333333333336,507.9,512.6833333333333,517.7166666666667,519.1833333333333,
 530.0666666666667,535.1333333333333,537.6833333333333,552.2833333333333,557.8333333333334,
 562.05,563.5333333333333,569.1333333333333,576.4833333333333,582.95,
 588.8,601.9,607.0333333333333,613.5166666666667,624.7833333333333,
 630.6666666666666,635.5666666666667,641.0833333333334,649.4333333333333,653.1166666666667,
 659.3833333333333,663.0666666666667,672.4166666666666,679.4833333333333,682.1,
 697.5833333333334,704.9833333333333,710.4333333333333,721.25,727.65,
 746.0166666666667,752.2333333333333,755.7666666666667,769.9833333333333,774.9,
 779.9833333333333,793.7166666666667,798.95,807.3833333333333,817.7333333333333,
 825.1666666666666,830.1166666666667,844.7166666666667,847.7333333333333,855.1166666666667,
 868.2166666666667,875.5833333333334,888.6833333333333,896.35,912.3666666666667,
 920.9,926.1833333333333,937.5833333333334,949.7333333333333,960.9166666666666,
 970.2,984.8833333333333,994.8833333333333,1009.05,1022.6666666666666,
 1034.3,1041.25,1058.0833333333333,1068.7,1082.3333333333333,
 1094.6166666666666,1106.1,1117.3833333333334,1129.45,1138.1666666666667,
 1155.2666666666667,1159.1166666666666,1177.95,1184.7666666666667,1202.5166666666667,
 1208.1666666666667,1223.9333333333334,1234.6666666666667,1249.3166666666666,1256.5,
 1277.2166666666667,1283.5,1298.6833333333334,1306.6833333333334,1322.0,
 1330.25,1351.2,1355.7333333333333,1371.5166666666667,1382.5333333333333,
 1392.95,1403.4166666666667,1416.8666666666666,1427.9,1464.8166666666666,
 1474.2333333333333,1476.1833333333334,1489.45,1489.45,1517.3,
 1524.0166666666667,1540.75,1562.5333333333333,1572.3833333333334,1586.4166666666667,
 1613.3833333333334,1662.7833333333333,1686.1333333333334,1695.8166666666666,1706.5666666666666,
 1729.6333333333334,1738.1166666666666,1753.05,1765.55,1780.8666666666666,
 1789.8333333333333,1804.75,1824.75,1858.9666666666667,1876.1833333333334,
 1903.5833333333333,1925.05,1952.4,1972.55,1995.3166666666666,
 2021.2166666666667,2046.6333333333334,2068.116666666667,2089.9666666666667,2113.95,
 2140.8,2167.733333333333,2192.0666666666666,2212.0666666666666,2240.5,
 2269.616666666667,2291.266666666667,2309.3333333333335,2337.15,2338.4666666666667]


Ta=[30.9,31.3,29.5,26.3,25.7,26.0,29.1,29.0,29.5,26.6,
    23.9,24.6,25.4,26.0,26.3,24.5,22.5,24.6,25.2,27.7,
    30.3,29.9,27.5,29.8,30.3,30.6,30.3,31.2,31.4,30.6,
    29.0,28.0,30.0,31.0,30.3,30.2,27.2,25.6,27.7,27.9,
    25.9,24.4,25.6,27.9,30.5,28.5,25.6,27.6,29.9,29.9,
    26.5,26.5,30.8,31.7,31.7,30.8,25.3,27.1,27.0,28.5,
    27.6,24.2,23.3,29.4,30.6,29.5,25.6,26.0,27.9,29.8,
    29.7,26.7,31.9,30.8,26.5,32.4,32.0,27.8,29.8,35.0,
    34.0,28.3,34.4,32.4,27.6,28.0,29.3,28.4,25.6,28.9,
    28.2,26.0,30.5,25.3,26.1,27.0,29.9,28.3,24.4,28.9,
    28.0,26.6,30.4,30.5,29.6,25.9,28.5,29.6,24.6,25.7,
    28.5,28.6,26.5,24.4,26.1,27.9,24.5,28.0,27.7,24.6,
    27.1,30.2,27.5,24.9,25.9,28.9,23.3,22.9,28.3,30.1,
    24.3,30.1,29.5,26.3,29.6,25.7,29.3,30.4,25.8,28.5,
    32.2,26.2,27.0,29.4,25.7,30.5,29.6,26.6,28.5,28.4,
    26.1,30.9,25.7,30.6,26.1,29.2,26.3,23.7,24.0,23.6,
    28.9,24.4,31.5,26.9,31.3,27.6,32.2,28.7,30.9,26.2,
    28.9,25.8,31.3,26.9,33.2,29.2,33.3,30.0,36.4,31.3,
    34.2,30.1,34.5,30.6,34.3,30.9,34.4,27.9,32.8,27.7,
    33.0,32.1,33.0,35.4,39.1,28.4,31.4,27.6,30.9,27.0,
    28.9,29.6,25.4,29.6,27.5,30.1,26.3,25.6,30.6,25.7,
    25.9,27.6,30.3,37.0,28.7,28.6,35.1,27.9,31.0,27.3,
    26.5,25.0,23.3,29.9,26.0,27.9,25.5,30.3,26.8,26.4,
    26.3,27.4,25.8,25.8,19.5,26.5,27.7,29.2,25.4,32.6,
    30.3,32.5,27.9,30.5,30.7]

Tf=[28.2,34.6,39.3,36.3,35.2,35.7,37.2,37.9,38.1,36.5,
    32.8,33.1,33.9,34.4,35.3,34.1,32.4,32.6,31.7,35.0,
    37.8,39.0,35.5,37.2,31.8,33.4,33.9,38.5,40.0,39.8,
    38.9,35.6,38.4,39.1,39.8,40.1,37.2,34.4,35.5,37.6,
    36.0,33.7,34.3,35.6,38.7,38.2,34.4,35.8,30.6,30.6,
    35.9,35.9,38.6,39.8,40.5,40.2,35.0,35.8,36.0,37.3,
    37.5,33.8,25.6,35.9,38.1,38.9,35.0,34.9,36.0,37.4,
    39.3,34.9,40.4,40.1,36.0,39.9,41.7,36.8,37.6,44.2,
    43.3,37.4,41.8,42.0,37.3,36.8,37.5,37.9,34.0,36.9,
    37.6,35.1,39.1,34.5,34.8,35.5,37.4,38.1,33.7,36.9,
    37.7,35.0,38.0,39.7,39.2,35.2,36.5,37.8,34.2,34.1,
    36.9,37.3,36.2,33.9,35.3,37.4,34.0,36.1,37.0,34.0,
    35.4,38.8,37.4,34.3,34.5,37.5,35.3,32.2,35.9,38.0,
    33.7,37.7,39.1,35.6,37.5,34.8,37.0,38.7,35.0,36.3,
    40.6,35.5,36.0,39.0,35.2,37.9,39.5,35.2,26.5,37.6,
    34.8,39.5,35.2,38.0,35.6,37.3,36.6,33.0,33.1,32.7,
    36.8,33.9,39.3,36.2,40.9,36.6,39.8,37.8,40.0,35.4,
    38.2,34.8,40.7,36.2,40.9,37.9,40.1,38.9,43.8,40.9,
    42.2,39.6,42.5,40.0,41.8,39.6,43.0,37.9,41.1,36.9,
    40.9,39.5,41.6,35.4,39.1,37.8,40.1,37.3,39.8,36.5,
    37.8,38.1,34.8,38.8,36.1,39.2,34.9,34.9,39.5,35.0,
    34.3,34.8,37.0,42.9,37.2,37.8,42.9,37.3,40.0,36.6,
    35.8,34.0,32.8,37.9,34.9,35.6,34.0,37.8,35.2,35.5,
    34.8,35.4,34.7,35.0,28.2,35.0,29.2,36.6,34.1,39.5,
    39.6,41.0,36.1,38.5,37.3]

V=[27.219,27.219,27.114,27.166,27.181,27.166,27.145,27.133,27.128,27.155,
   27.236,27.225,27.211,27.203,27.183,27.203,27.248,27.24,27.258,27.189,
   27.128,27.106,27.179,27.144,27.144,27.144,27.144,27.117,27.091,27.092,
   27.112,27.161,27.119,27.096,27.085,27.093,27.143,27.2,27.168,27.134,
   27.168,27.216,27.203,27.177,27.112,27.122,27.201,27.172,27.29,27.29,
   27.168,27.168,27.117,27.095,27.080,27.086,27.189,27.174,27.160,27.139,
   27.141,27.216,27.338,27.165,27.126,27.111,27.191,27.192,27.17,27.136,
   27.136,27.098,27.077,27.084,27.171,27.087,27.051,27.151,27.134,26.999,
   27.017,27.140,27.048,27.044,27.142,27.152,27.137,27.133,27.217,27.154,
   27.139,27.188,27.105,27.203,27.197,27.182,27.142,27.129,27.222,27.154,
   27.139,27.193,27.130,27.096,27.107,27.192,27.165,27.136,27.213,27.213,
   27.156,27.146,27.169,27.219,27.189,27.139,27.217,27.173,27.154,27.219,
   27.188,27.177,27.149,27.214,27.210,27.148,27.195,27.256,27.180,27.135,
   27.228,27.138,27.112,27.129,27.149,27.208,27.161,27.124,27.205,27.174,
   27.085,27.194,27.183,27.120,27.200,27.141,27.111,27.200,27.173,27.149,
   27.210,27.110,27.202,27.138,27.192,27.157,27.173,27.249,27.248,27.257,
   27.167,27.230,27.116,27.181,27.083,27.173,27.104,27.147,27.102,27.198,
   27.141,27.213,27.090,27.184,27.083,27.147,27.100,27.127,27.020,27.085,
   27.055,27.112,27.049,27.101,27.064,27.111,27.040,27.149,27.078,27.168,
   27.084,27.114,27.069,27.204,27.122,27.151,27.101,27.162,27.109,27.178,
   27.152,27.146,27.216,27.131,27.189,27.123,27.214,27.217,27.117,27.214,
   27.229,27.216,27.164,27.045,27.167,27.154,27.046,27.167,27.108,27.178,
   27.199,27.237,27.264,27.154,27.221,27.204,27.238,27.157,27.213,27.207,
   27.222,27.209,27.225,27.219,27.369,27.220,27.209,27.185,27.240,27.123,
   27.122,27.090,27.194,27.146,27.173]

I=[.475,.474,.474,.475,.475,.475,.474,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.474,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.474,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.4745,
   .475,.475,.475,.474,.475,.474,.474,.475,.475,.474,
   .474,.475,.474,.474,.475,.475,.475,.475,.475,.475,
   .475,.475,.474,.475,.475,.475,.474,.475,.475,.474,
   .475,.475,.474,.474,.474,.475,.475,.474,.475,.475,
   .4745,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.474,.475,.475,.475,.475,.475,.475,.475,.474,
   .475,.474,.4745,.475,.475,.475,.475,.475,.475,.475,   
   .4745,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.474,.475,.475,.475,
   .475,.475,.475,.475,.4745,.475,.474,.475,.474,.475,
   .474,.475,.474,.475,.474,.4745,.474,.475,.474,.475,
   .474,.474,.474,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.474,.475,.475,.474,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.475,
   .475,.475,.475,.475,.475,.475,.475,.475,.475,.474,
   .475,.475,.475,.475,.4745]


# arranged: index,year,month,day,hour,min,Ta,Tf,V,I,OP
#vals245_On=[['index','year','month','day','hour','minutes','Ta','Tf','V','I','OP'],
#            [246,2020,10,3,13,50,28.6,35.6,27.206,.475,28.54]]


dataN = pd.read_csv('EotronDataAferPoint245.txt', delimiter=',')

datalen=len(dataN)
print('info on dataframe of text file:')
print('Number of Non-Heading Rows', datalen)
dataN.info()
print('\ncontents of dataframe:\n',dataN)

# df of new values, all
dfN = pd.DataFrame(dataN,columns=['itemNo','year','month','day','hour','minutes','Ta','Tf','V','I','OP','OffsetH'])

# Time
dfT=dfN[['year','month','day','hour','minutes']]
print('\ndataframe of time in year, month,day,hour,minutes:\n',dfT)
dfTP=pd.to_datetime(dfT)
print('\n-----------------------------\ndataframe of time in datetime format:\n',dfTP)
dfN['dateTime']=dfTP
#ts = datetime(2020,6,26, 17, 30, 00)
dfN['start']=pd.Timestamp('2020-06-26T1730') # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Timestamp.html
dfN['deltaT']=dfN['dateTime']-dfN['start']
dfN['dTT']=dfN['deltaT']/np.timedelta64(1,'h') # https://www.datasciencemadesimple.com/difference-two-timestamps-seconds-minutes-hours-pandas-python-2/
dfN['dTTh']=dfN['dTT']-dfN['OffsetH']
t.extend(dfN['dTTh'])
print('\n-----------------------------\ntime incl new values:\n',t)

# power
pN=dfN['OP'].values.tolist()
p.extend(pN)

# ambient T
TaN=dfN['Ta'].values.tolist()
Ta.extend(TaN)

print('\n-----------------------------\nTa with added values:\n',Ta)

# fab T
TfN=dfN['Tf'].values.tolist()
Tf.extend(TfN)

# Voltage
VN=dfN['V'].values.tolist()
V.extend(VN)

# Current
IN=dfN['I'].values.tolist()
I.extend(IN)


##############################
#          Plotting          #
##############################
fig = plt.figure(figsize=(11,9), linewidth=6,edgecolor="#322288")
fig.patch.set_facecolor('#cccccc')
fig.subplots_adjust(left=None, bottom=.1, right=None, top=.9, wspace=0.2, hspace=None)

############### FIRST FIG, Optical Power ###############
ax1 = plt.subplot2grid((5, 3), (0, 0), rowspan=2, colspan=3, fc="#c0c0c0",)
ax1.grid(color='#818181')
import matplotlib.ticker #used in subsequent plots too, with axX.minorticks_on()
class MyLocator(matplotlib.ticker.AutoMinorLocator):
    def __init__(self, n=5): # n changes # of tickes. Drawn = n-1, spaces =n
        super().__init__(n=n)
matplotlib.ticker.AutoMinorLocator = MyLocator   
ax1.minorticks_on()
ax1r=ax1.twinx()
ax1.set_title('$\mathbf{Eotron}$ 1x1 LEDs, 2 Parallel Strings of 5 in series, $\mathit{I=.475A}$   ', pad=21)
plt.suptitle('probe at fixed distance ~426 mm from LEDs', fontsize='8',y=.957)
# Bottom of acrylic sheet is 446 from metal heat sink
# Eotron's drawing indicated 3.35 mm tall from fab bottom to top of LED cover glass
# acrylic is .125" thick so 446 - 3.35+.125*25.4 =425.825 is distance from LED top to probe
ax1.set_xlabel('Time (hours)')
ax1.set_ylabel('Optical Power ($\u03BC$W)',color='#2255ac')
ax1.plot(t,p)


#lp=list([p])
lp=[]
prel=[]
for lp in p:
    prel.append(lp/p[0])
# prel=lp.copy
ax1r.grid(color='#409540',linestyle='-.') # For light grey instead #dfdfdf
ax1r.set_ylabel('Optical Power relative to Starting Power',color='#006500')
ax1r.plot(t,prel,marker='.', markeredgecolor='#006500')

# Adding text box with decay over time
deltaRelPow = -.145 # Change me every time you add a point. All the others should fix themselves.
ax1r.arrow(0,.97,max(t),deltaRelPow,linestyle=':',color='#ee5522')
boxValueEO=(deltaRelPow)/(max(t)/100)
boxTextEO='decay rate = ~' + str("%.4f" % boxValueEO) +' % per hour'
propsEO = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
###############################################################################
# Placement of text box:                                                      #
#   x: centered at .7*(total hrs)                                             #
#   y: taking the span of prel (right vert axis), 90% of that, added to min.  #
#     (Should stay put.)                                                      #
###############################################################################
ax1r.text((0.75*max(t)),(min(prel)+0.95*(1-min(prel))),boxTextEO,bbox=propsEO) 


"""
A broken attempt to make a trend line. Try this on something simpler first
Lt=len(t)
#tLast=t[Lt]
z=np.polyfit(t,prel,1)
px=np.poly1d(z)
TlineX=[t[0],t[Lt-1]]
#ax1r.plot(TlineX,px)
"""

#Graph inset for Cold Power On power
from mpl_toolkits.axes_grid.inset_locator import inset_axes,InsetPosition,mark_inset
axins=inset_axes(ax1, width="30%", height="25%", bbox_to_anchor=(.72,.525,.8,.95),bbox_transform=(ax1.transAxes),loc=3)
axins.set_title('Cold Pwr On Detail',fontsize=10)
axins.set_xlim(3376,3380)
axins.set_ylim(.82,.84)
axins.plot(t,prel)

#########################################################################################
# For annotations, this is helpful:                                                     #
# https://matplotlib.org/3.1.1/gallery/text_labels_and_annotations/annotation_demo.html #
#########################################################################################
#from matplotlib.patches import Ellipse
#from matplotlib.patches import FancyArrowPatch
#from matplotlib.text import OffsetFrom

# The annotations start from the xy point in first line and will move as plot changes.
# the arrow will be between that point and the point defined by the xytext (xval, yval)
#   so if want arrow from graph point to note to go up and left, xytext's x is negative (left), 
#   y is positive. Is want arrow to go down and right, x is positive, y is negative
# AngleA is the one coming out of the box
# AngleB is the line from the arrowhead to the box and its the same whether it's
#   up and left or down and right, etc, just flips about the origin with the vector from point to box

ax1r.annotate('Power off \nfor 84 min',color='#006500', ha='center',
            xy=(92, .976), xycoords='data',
            xytext=(10, -85), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#dfdfdf"),
            arrowprops=dict(arrowstyle="->", color='#f98638',
                            connectionstyle="angle,angleA=0,angleB=250,rad=25"))

ax1r.annotate('Power off inadvertently for 356 min',color='#006500', ha='center',
            xy=(185.3, .998), xycoords='data',
            xytext=(125, -8), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#dfdfdf"),
            arrowprops=dict(arrowstyle="->", color='#f98638',
                            connectionstyle="angle,angleA=0,angleB=140,rad=25"))

ax1r.annotate('Off for 220 min',color='#006500', ha='center',
            xy=(248.6, .973), xycoords='data',
            xytext=(65, 1), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#dfdfdf"),
            arrowprops=dict(arrowstyle="->", color='#f98638',
                            connectionstyle="angle,angleA=0,angleB=60,rad=25"))

ax1r.annotate('Off for 257 min',color='#006500', ha='center',
            xy=(405, .942), xycoords='data',
            xytext=(65, 15), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#dfdfdf"),
            arrowprops=dict(arrowstyle="->", color='#f98638',
                            connectionstyle="angle,angleA=0,angleB=55,rad=25"))

ax1r.annotate('521 hrs, \n5yrs heavy use',color='#eea5ee', ha='center',
            xy=(521, .928), xycoords='data',
            xytext=(35, -65), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#228822"),
            arrowprops=dict(arrowstyle="->", color='yellow',
                            connectionstyle="angle,angleA=0,angleB=90,rad=25"))

# Annotations for start/end of other tests
ax1r.annotate('Violumas 1 Start\n450.52',color='#991509', ha='center',
            xy=(450, .928), xycoords='data',
            xytext=(0, -105), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#a9a9c8"),
            arrowprops=dict(arrowstyle="-", color='#8f19d4',
                            connectionstyle="angle,angleA=0,angleB=90,rad=25"))

#ax1r.text(1141.45,.928,'Violumas 1 End, 1141.45',ha="left",va="bottom",rotation=90,size=12)

ax1r.annotate('Violumas 1 End\n1141.45',color='#991509', ha='center',
            xy=(1141.45, .928), xycoords='data',
            xytext=(0, -105), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#a9a9c8"),
            arrowprops=dict(arrowstyle="-", color='#8f19d4',
                            connectionstyle="angle,angleA=0,angleB=90,rad=25"))

ax1r.annotate('Violumas 2 Start\n1171.92',color='#322288', ha='center',
            xy=(1171.92, .855), xycoords='data',
            xytext=(50, 92), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#ffdcfc"),
            arrowprops=dict(arrowstyle="-", color='#fc08f4',
                            connectionstyle="angle,angleA=0,angleB=270,rad=25"))

ax1r.annotate('Violumas 2 End\n2322.97',color='#322288', ha='center',
            xy=(2322.97, .825), xycoords='data',
            xytext=(0, 85), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#ffdcfc"),
            arrowprops=dict(arrowstyle="-", color='#fc08f4',
                            connectionstyle="angle,angleA=0,angleB=270,rad=25"))

ax1r.annotate('Violumas TriColor\nStart 2732.58',color='#322288', ha='center',
            xy=(2732.58, .825), xycoords='data',
            xytext=(80, 50), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#bfecfc"),
            arrowprops=dict(arrowstyle="-", color='#08d0fc',
                            connectionstyle="angle,angleA=0,angleB=270,rad=25"))


############### SECOND FIG,Temp Data ###############

ax2 = plt.subplot2grid((5, 3), (2, 0), rowspan=1, colspan=3, xticklabels=[], fc="#aaaaff") #to hide x ax ticks and numbers xticklabels=[], 
#ax2.text(0.5, 0.5, "ax2", horizontalalignment='center', verticalalignment='center')
ax2.grid(color='#dfdfdf')
ax2.minorticks_on()
ax2.grid(which='minor', linestyle=':', color='#dfdfdf')
ax2.set_ylabel('Temp (C)')
ax2.set_ylim(15,45)
ax2.plot(t,Ta,label='Ambient',marker="+",markeredgecolor="#f98638")
ax2.plot(t,Tf,label='Fab',marker=".",markeredgecolor="#2255ac")
ax2.legend(bbox_to_anchor=[.957,.92],fontsize='small',facecolor="#fac96e",edgecolor="black")

############### THIRD FIG, V and I ###############
ax3 = plt.subplot2grid((5, 3), (3, 0), rowspan=1, colspan=3, xticklabels=[], fc="#fac96e",) #xticks=[], to hide x axis ticks
ax3.grid(color='#aaaaff')

ax3.minorticks_on()
ax3.grid(which='minor', linestyle=':', color='#aaaaff')
ax3.set_ylabel('Voltage (V)',color="#2255ac")
ax3.set_ylim(26.95,28.7)
ax3r=ax3.twinx()
ax3r.set_ylabel('Current (A)',color="green")
ax3r.set_ylim(.4738,.4752)
ax3.plot(t,V,marker=".",markeredgecolor="red")
ax3r.plot(t,I,color='#009500',marker=".",markeredgecolor="#2255ac",linewidth='1') #f98638


""" Total Time note on Fig
  prefix the text with f, then variable in {}. f denotes formatted string literal
    sig figs done by #.2f
    x and y are from bottom left and using figtext, are in figure coords, not ax coords.
"""
EotronElT=float("%.2f" % max(t))
EotronElD=float("%.1f" % (max(t)/24))
plt.figtext(.04,.95,f"Total days = {EotronElD}",fontstyle='italic',backgroundcolor="#aabbff")
plt.figtext(.96,.95,f"Total hrs = {EotronElT}",fontstyle='italic',backgroundcolor="#aabbff",horizontalalignment="right")

############### Fourth Fig, Early Spectra #################
ax4 = plt.subplot2grid((5, 3), (4, 0), rowspan=1, colspan=1, fc="purple")
ax4.set_title('Beginning (0 hr)')
# ax4.text(0.5,0.6, "ax4", horizontalalignment='center', verticalalignment='center')
data = pd.read_table('Spectral Scan, 1-Jul-20,270-290.txt', delimiter='\t')
df = pd.DataFrame(data,columns=['Wavelength (nm)','AbsIrrad'])
#df.plot (next line) grew the plot too tall and prevented x axis labels and name in first plot from showing up
#ax4.plot(ax=ax4, kind='line',x='Wavelength (nm)', y='AbsIrrad', xlim=(270,290), linewidth=2, legend=None)
#so convert the 2 columns to lists and graph those instead
wv=df['Wavelength (nm)'].values.tolist()
ai=df['AbsIrrad'].values.tolist()
ax4.set_yticklabels([])
ax4.set_xlim(270,290)
ax4.plot(wv,ai,linewidth=2)

# Info to console
print('\n-----------------------------\nStarting LED Spectra:')
data.info()

# print(data)
print("\nTotal Time Elapsed: ", max(t), "hrs.", len(t), "data points, last datapoint", len(t)-1)




############### Fifth "Fig", spaces used for text. Turn off frames, ticks, labels, yatta ##########
ax5 = plt.subplot2grid((5, 3), (4, 1), rowspan=1, colspan=1, fc="grey",xticks=[],yticks=[],frameon=False)
ax5.text(0.5,0.5, "LED \nSpectra \n(nm)",fontsize="14", horizontalalignment='center')
ax5.text(0.5,0.2, "cosine corrector \n at beginning", fontsize='8', horizontalalignment='center') #, verticalalignment='center'

############### Sixth Fig, the spectra at last data point #################
ax6 = plt.subplot2grid((5, 3), (4, 2), rowspan=1, colspan=1, fc="purple")
ax6.set_title('End (657 hrs)')
#ax6.text(0.5,0.5, "I open \nat the\nclose", horizontalalignment='center',color="orange")
data640 = pd.read_csv('Fiber Spec Scan After 640 Hrs, 1 sec.txt', skiprows=17, delimiter='\t')
data640.columns=["nm", "T"]
nm=pd.DataFrame(data640,columns=['nm'])
T=pd.DataFrame(data640,columns=['T'])
ax6.minorticks_on()
ax6.grid(which='major', linestyle='-',color="#bb8888")
ax6.grid(which='minor', linestyle=':',color="#bb7777")
ax6.set_yticklabels([])
ax6.set_xlim(260,295)
ax6.plot(nm,T,linewidth=2)


plt.tight_layout()
plt.show()


###############################################
#   Ancient Time/Power data copied to lists   #
#   ... see an older version of the file      #
###############################################
