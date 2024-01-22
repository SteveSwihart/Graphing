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
fig = plt.figure(figsize=(10,9), linewidth=6,edgecolor="#322288")
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
deltaRelPow = -.147 # Change me every time you add a point. All the others should fix themselves.
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
ax1r.text((0.7*max(t)),(min(prel)+0.92*(1-min(prel))),boxTextEO,bbox=propsEO) 


"""
A broken attempt to make a trend line. Try this on something simpler first
Lt=len(t)
#tLast=t[Lt]
z=np.polyfit(t,prel,1)
px=np.poly1d(z)
TlineX=[t[0],t[Lt-1]]
#ax1r.plot(TlineX,px)
"""

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
            xytext=(65, 2), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#dfdfdf"),
            arrowprops=dict(arrowstyle="->", color='#f98638',
                            connectionstyle="angle,angleA=0,angleB=60,rad=25"))

ax1r.annotate('Off for \n257 min',color='#006500', ha='center',
            xy=(405, .942), xycoords='data',
            xytext=(55, 8), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#dfdfdf"),
            arrowprops=dict(arrowstyle="->", color='#f98638',
                            connectionstyle="angle,angleA=0,angleB=55,rad=25"))

ax1r.annotate('640 hrs, \n5yrs heavy use',color='#eea5ee', ha='center',
            xy=(640, .928), xycoords='data',
            xytext=(20, -72), textcoords='offset points',
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
            xytext=(0, 90), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#ffdcfc"),
            arrowprops=dict(arrowstyle="-", color='#fc08f4',
                            connectionstyle="angle,angleA=0,angleB=270,rad=25"))

ax1r.annotate('Violumas 2 End\n2322.97',color='#322288', ha='center',
            xy=(2322.97, .825), xycoords='data',
            xytext=(0, 120), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#ffdcfc"),
            arrowprops=dict(arrowstyle="-", color='#fc08f4',
                            connectionstyle="angle,angleA=0,angleB=270,rad=25"))

ax1r.annotate('Violumas TriColor\nStart 2322.97',color='#322288', ha='center',
            xy=(2732.58, .825), xycoords='data',
            xytext=(0, 70), textcoords='offset points',
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
ax2.set_ylim(19,45)
ax2.plot(t,Ta,label='Ambient',marker="+",markeredgecolor="#f98638")
ax2.plot(t,Tf,label='Fab',marker=".",markeredgecolor="#2255ac")
ax2.legend(bbox_to_anchor=[.957,.7],fontsize='small',facecolor="#fac96e",edgecolor="black")

############### THIRD FIG, V and I ###############
ax3 = plt.subplot2grid((5, 3), (3, 0), rowspan=1, colspan=3, xticklabels=[], fc="#fac96e",) #xticks=[], to hide x axis ticks
ax3.grid(color='#aaaaff')

ax3.minorticks_on()
ax3.grid(which='minor', linestyle=':', color='#aaaaff')
ax3.set_ylabel('Voltage (V)',color="#2255ac")
ax3.set_ylim(26.95,27.4)
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
###############################################
"""
##############################
#         26-Jun-20          #
##############################


p0=34.31

t1=datetime(2020,6,26,18,18,00)
t1d=t1-ts
p1=33.62

t2=datetime(2020,6,26,23,16,00)
t2d=t2-ts
p2=32.59

##############################
#         27-Jun-20          #
##############################

t3=datetime(2020,6,27,7,10,00)
t3d=t3-ts
t3dh=t3d.seconds/3600
p3=32.85

t4=datetime(2020,6,27,8,54,00)
t4d=t4-ts
p4=32.93

t5=datetime(2020,6,27,12,26,00)
t5d=t5-ts
p5=32.93

t6=datetime(2020,6,27,14,29,00)
t6d=t6-ts
p6=32.93

t7=datetime(2020,6,27,16,4,00)
t7d=t7-ts
p7=32.93

t8=datetime(2020,6,27,17,6,00)
t8d=t8-ts
t8dh=(t8d.days*24*3600+t8d.seconds)/3600 # existing method broke when days >0
p8=32.93                                 # so converted days to seconds, added
                                         # seconds, then used in t without dividing /3600
                                         # Copied concept to t3, it works.
t9=datetime(2020,6,27,22,28,00)
t9d=t9-ts
t9dh=(t9d.days*24*3600+t9d.seconds)/3600 
p9=32.93

##############################
#         28-Jun-20          #
##############################

t10=datetime(2020,6,28,10,3,00)
t10d=t10-ts
t10dh=(t10d.days*24*3600+t10d.seconds)/3600 
p10=33.19

t11=datetime(2020,6,28,12,14,00)
t11d=t11-ts
t11dh=(t11d.days*24*3600+t11d.seconds)/3600 
p11=33.19

t12=datetime(2020,6,28,14,34,00)
t12d=t12-ts
t12dh=(t12d.days*24*3600+t12d.seconds)/3600 
p12=33.19

t13=datetime(2020,6,28,16,4,00) #one missing image here because supply was off
                                #while switching glass in/out.
t13d=t13-ts
t13dh=(t13d.days*24*3600+t13d.seconds)/3600 
p13=33.28

t14=datetime(2020,6,28,19,48,00)
t14d=t14-ts
t14dh=(t14d.days*24*3600+t14d.seconds)/3600 
p14=33.11

##############################
#         29-Jun-20          #
##############################

t15=datetime(2020,6,29,0,24,00) 
t15d=t15-ts
t15dh=(t15d.days*24*3600+t15d.seconds)/3600 
p15=33.19

t16=datetime(2020,6,29,7,24,00) 
t16d=t16-ts
t16dh=(t16d.days*24*3600+t16d.seconds)/3600 
p16=33.45

t17=datetime(2020,6,29,10,54,00) 
t17d=t17-ts
t17dh=(t17d.days*24*3600+t17d.seconds)/3600 
p17=33.36

t18=datetime(2020,6,29,11,42,00) 
t18d=t18-ts
t18dh=(t18d.days*24*3600+t18d.seconds)/3600 
p18=33.45

t19=datetime(2020,6,29,14,34,00) 
t19d=t19-ts
t19dh=(t19d.days*24*3600+t19d.seconds)/3600 
p19=33.19

t20=datetime(2020,6,29,18,14,00) 
t20d=t20-ts
t20dh=(t20d.days*24*3600+t20d.seconds)/3600 
p20=33.02

t21=datetime(2020,6,29,22,15,00) 
t21d=t21-ts
t21dh=(t21d.days*24*3600+t21d.seconds)/3600 
p21=33.02

##############################
#         30-Jun-20          #
##############################
t22=datetime(2020,6,30,11,44,00) 
t22d=t22-ts
t22dh=(t22d.days*24*3600+t22d.seconds)/3600 
p22=32.28

t23=datetime(2020,6,30,13,34,00) 
t23d=t23-ts
t23dh=(t23d.days*24*3600+t23d.seconds)/3600 
p23=33.19

#################################################################
# Accidentally didn't turn power back on from previous to next. #
# That's the following in time (seconds)                        #
# t24-t23                                                       #
# Out[9]: datetime.timedelta(seconds=5040)                      #
# Subtract that from now on, but leave 60 sec off so distinct   #
# points are visible                                            #
#################################################################

t24=datetime(2020,6,30,14,58,00) 
t24d=t24-ts
t24dh=(t24d.days*24*3600+t24d.seconds-4980)/3600
p24=33.45

t25=datetime(2020,6,30,15,00,00) 
t25d=t25-ts
t25dh=(t25d.days*24*3600+t25d.seconds-4980)/3600
p25=33.40

t26=datetime(2020,6,30,15,6,00) 
t26d=t26-ts
t26dh=(t26d.days*24*3600+t26d.seconds-4980)/3600
p26=33.36

t27=datetime(2020,6,30,16,47,00) 
t27d=t27-ts
t27dh=(t27d.days*24*3600+t27d.seconds-4980)/3600
p27=33.11

t28=datetime(2020,6,30,18,46,00) 
t28d=t28-ts
t28dh=(t28d.days*24*3600+t28d.seconds-4980)/3600
p28=32.93

t29=datetime(2020,6,30,20,6,00) 
t29d=t29-ts
t29dh=(t29d.days*24*3600+t29d.seconds-4980)/3600
p29=33.02

t30=datetime(2020,6,30,22,26,00) 
t30d=t30-ts
t30dh=(t30d.days*24*3600+t30d.seconds-4980)/3600
p30=33.02

##############################
#          1-Jul-20          #
##############################
t31=datetime(2020,7,1,13,6,00) 
t31d=t31-ts
t31dh=(t31d.days*24*3600+t31d.seconds-4980)/3600
p31=33.19

t32=datetime(2020,7,1,16,26,00) 
t32d=t32-ts
t32dh=(t32d.days*24*3600+t32d.seconds-4980)/3600
p32=33.02

t33=datetime(2020,7,1,18,6,00) 
t33d=t33-ts
t33dh=(t33d.days*24*3600+t33d.seconds-4980)/3600
p33=32.93

t34=datetime(2020,7,1,19,35,00) 
t34d=t34-ts
t34dh=(t34d.days*24*3600+t34d.seconds-4980)/3600
p34=32.93

t35=datetime(2020,7,1,21,6,00) 
t35d=t35-ts
t35dh=(t35d.days*24*3600+t35d.seconds-4980)/3600
p35=32.93

##############################
#          2-Jul-20          #
##############################
t36=datetime(2020,7,2,1,36,00) 
t36d=t36-ts
t36dh=(t36d.days*24*3600+t36d.seconds-4980)/3600
p36=33.11

t37=datetime(2020,7,2,10,10,00) 
t37d=t37-ts
t37dh=(t37d.days*24*3600+t37d.seconds-4980)/3600
p37=33.28

t38=datetime(2020,7,2,14,6,00) 
t38d=t38-ts
t38dh=(t38d.days*24*3600+t38d.seconds-4980)/3600
p38=33.11

t39=datetime(2020,7,2,21,3,00) 
t39d=t39-ts
t39dh=(t39d.days*24*3600+t39d.seconds-4980)/3600
p39=32.93

##############################
#          3-Jul-20          #
##############################
t40=datetime(2020,7,3,0,50,00) 
t40d=t40-ts
t40dh=(t40d.days*24*3600+t40d.seconds-4980)/3600
p40=33.11

t41=datetime(2020,7,3,8,33,00) 
t41d=t41-ts
t41dh=(t41d.days*24*3600+t41d.seconds-4980)/3600
p41=33.19

t42=datetime(2020,7,3,11,33,00) 
t42d=t42-ts
t42dh=(t42d.days*24*3600+t42d.seconds-4980)/3600
p42=33.11

t43=datetime(2020,7,3,14,6,00) 
t43d=t43-ts
t43dh=(t43d.days*24*3600+t43d.seconds-4980)/3600
p43=33.02

t44=datetime(2020,7,3,18,0,00) 
t44d=t44-ts
t44dh=(t44d.days*24*3600+t44d.seconds-4980)/3600
p44=32.85

t45=datetime(2020,7,3,23,19,00) 
t45d=t45-ts
t45dh=(t45d.days*24*3600+t45d.seconds-4980)/3600
p45=32.85

##############################
#          4-Jul-20          #
##############################
t46=datetime(2020,7,4,10,0,00) 
t46d=t46-ts
t46dh=(t46d.days*24*3600+t46d.seconds-4980)/3600
p46=33.11

t47=datetime(2020,7,4,12,10,00) 
t47d=t47-ts
t47dh=(t47d.days*24*3600+t47d.seconds-4980)/3600
p47=33.02

t48=datetime(2020,7,4,16,43,00) 
t48d=t48-ts
t48dh=(t48d.days*24*3600+t48d.seconds-21300)/3600
p48=34.25
####################################################################
# Power accidentally off from 12:10 to 16:45 = 16380 sec           #
# Adding in previous 4900 sec off time = 21360 sec                 #
# Take that value off all future values, bot for this point, leave #
# 60 sec so it isn't op top of previous point.                     #
####################################################################
t49=datetime(2020,7,4,16,43,10) 
t49d=t49-ts
t49dh=(t49d.days*24*3600+t49d.seconds-21300)/3600
p49=33.36

t50=datetime(2020,7,4,22,45,00) 
t50d=t50-ts
t50dh=(t50d.days*24*3600+t50d.seconds-21360)/3600
p50=32.76

##############################
#          5-Jul-20          #
##############################
t51=datetime(2020,7,5,8,27,00) 
t51d=t51-ts
t51dh=(t51d.days*24*3600+t51d.seconds-21360)/3600
p51=32.93

t52=datetime(2020,7,5,14,47,00) 
t52d=t52-ts
t52dh=(t52d.days*24*3600+t52d.seconds-21360)/3600
p52=32.76

t53=datetime(2020,7,5,16,25,00) 
t53d=t53-ts
t53dh=(t53d.days*24*3600+t53d.seconds-21360)/3600
p53=32.68

t54=datetime(2020,7,5,19,5,00) 
t54d=t54-ts
t54dh=(t54d.days*24*3600+t54d.seconds-21360)/3600
p54=32.59

t55=datetime(2020,7,5,21,26,00) 
t55d=t55-ts
t55dh=(t55d.days*24*3600+t55d.seconds-21360)/3600
p55=32.68

##############################
#          6-Jul-20          #
##############################
t56=datetime(2020,7,6,8,2,00) 
t56d=t56-ts
t56dh=(t56d.days*24*3600+t56d.seconds-21360)/3600
p56=32.93

t57=datetime(2020,7,6,12,16,00) 
t57d=t57-ts
t57dh=(t57d.days*24*3600+t57d.seconds-21360)/3600
p57=32.85

t58=datetime(2020,7,6,14,15,00) 
t58d=t58-ts
t58dh=(t58d.days*24*3600+t58d.seconds-21360)/3600
p58=32.76

t59=datetime(2020,7,6,17,19,00) 
t59d=t59-ts
t59dh=(t59d.days*24*3600+t59d.seconds-21360)/3600
p59=32.68

t60=datetime(2020,7,6,21,55,00) 
t60d=t60-ts
t60dh=(t60d.days*24*3600+t60d.seconds-21360)/3600
p60=32.76

##############################
#          7-Jul-20          #
##############################
t61=datetime(2020,7,7,8,2,00) 
t61d=t61-ts
t61dh=(t61d.days*24*3600+t61d.seconds-21360)/3600
p61=32.93

#########################
# Off fr 08:05 to 11:24 #
#########################
t62=datetime(2020,7,7,11,24,00) 
t62d=t62-ts
t62dh=(t62d.days*24*3600+t62d.seconds-33480)/3600
p62=33.36

t63=datetime(2020,7,7,15,8,00) 
t63d=t63-ts
t63dh=(t63d.days*24*3600+t63d.seconds-33480)/3600
p63=32.76

t64=datetime(2020,7,7,16,41,00) 
t64d=t64-ts
t64dh=(t64d.days*24*3600+t64d.seconds-33480)/3600
p64=32.59

t65=datetime(2020,7,7,21,19,00) 
t65d=t65-ts
t65dh=(t65d.days*24*3600+t65d.seconds-33480)/3600
p65=32.68

##############################
#          8-Jul-20          #
##############################
t66=datetime(2020,7,8,8,0,00) 
t66d=t66-ts
t66dh=(t66d.days*24*3600+t66d.seconds-33480)/3600
p66=32.93

t67=datetime(2020,7,8,9,10,00) 
t67d=t67-ts
t67dh=(t67d.days*24*3600+t67d.seconds-33480)/3600
p67=32.68

t68=datetime(2020,7,8,11,39,00) 
t68d=t68-ts
t68dh=(t68d.days*24*3600+t68d.seconds-33480)/3600
p68=32.59

t69=datetime(2020,7,8,13,55,00) 
t69d=t69-ts
t69dh=(t69d.days*24*3600+t69d.seconds-33480)/3600
p69=32.68

t70=datetime(2020,7,8,23,19,00) 
t70d=t70-ts
t70dh=(t70d.days*24*3600+t70d.seconds-33480)/3600
p70=32.42

##############################
#          9-Jul-20          #
##############################
t71=datetime(2020,7,9,10,50,00) 
t71d=t71-ts
t71dh=(t71d.days*24*3600+t71d.seconds-33480)/3600
p71=32.68

t72=datetime(2020,7,9,19,32,00) 
t72d=t72-ts
t72dh=(t72d.days*24*3600+t72d.seconds-33480)/3600
p72=32.24

t73=datetime(2020,7,9,22,5,00) 
t73d=t73-ts
t73dh=(t73d.days*24*3600+t73d.seconds-33480)/3600
p73=32.33

##############################
#         10-Jul-20          #
##############################
t74=datetime(2020,7,10,8,20,00) 
t74d=t74-ts
t74dh=(t74d.days*24*3600+t74d.seconds-33480)/3600
p74=32.59

t75=datetime(2020,7,10,15,45,00) 
t75d=t75-ts
t75dh=(t75d.days*24*3600+t75d.seconds-33480)/3600
p75=32.24

t76=datetime(2020,7,10,21,18,00) 
t76d=t76-ts
t76dh=(t76d.days*24*3600+t76d.seconds-33480)/3600
p76=32.07

##############################
#         11-Jul-20          #
##############################
t77=datetime(2020,7,11,8,57,00) 
t77d=t77-ts
t77dh=(t77d.days*24*3600+t77d.seconds-33480)/3600
p77=32.33

t78=datetime(2020,7,11,11,1,00) 
t78d=t78-ts
t78dh=(t78d.days*24*3600+t78d.seconds-33480)/3600
p78=32.24

t79=datetime(2020,7,11,20,46,00) 
t79d=t79-ts
t79dh=(t79d.days*24*3600+t79d.seconds-33480)/3600
p79=31.81

t80=datetime(2020,7,11,22,11,00) 
t80d=t80-ts
t80dh=(t80d.days*24*3600+t80d.seconds-33480)/3600
p80=31.81

##############################
#         12-Jul-20          #
##############################
t81=datetime(2020,7,12,9,12,00) 
t81d=t81-ts
t81dh=(t81d.days*24*3600+t81d.seconds-33480)/3600
p81=32.33

t82=datetime(2020,7,12,16,53,00) 
t82d=t82-ts
t82dh=(t82d.days*24*3600+t82d.seconds-33480)/3600
p82=31.90

t83=datetime(2020,7,12,22,29,00) 
t83d=t83-ts
t83dh=(t83d.days*24*3600+t83d.seconds-33480)/3600
p83=31.90

##############################
#         13-Jul-20          #
##############################
t84=datetime(2020,7,13,7,51,00) 
t84d=t84-ts
t84dh=(t84d.days*24*3600+t84d.seconds-33480)/3600
p84=32.24

t85=datetime(2020,7,13,11,58,00) 
t85d=t85-ts
t85dh=(t85d.days*24*3600+t85d.seconds-33480)/3600
p85=32.16

t86=datetime(2020,7,13,14,00,00) 
t86d=t86-ts
t86dh=(t86d.days*24*3600+t86d.seconds-33480)/3600
p86=32.07

t87=datetime(2020,7,13,21,30,00) 
t87d=t87-ts
t87dh=(t87d.days*24*3600+t87d.seconds-33480)/3600
p87=32.24

##############################
#         14-Jul-20          #
##############################
"""
"""
Power off from last data point to 04:17, when I happened to leave to see comet
NEOWISE. 4 hrs 17 min = 4.2833 hrs = 15420 sec
... added to previous value of 33480 = 48900
"""
"""
t88=datetime(2020,7,14,10,20,00) 
t88d=t88-ts
t88dh=(t88d.days*24*3600+t88d.seconds-48900)/3600
p88=32.42

t89=datetime(2020,7,14,15,59,00) 
t89d=t89-ts
t89dh=(t89d.days*24*3600+t89d.seconds-48900)/3600
p89=32.24

t90=datetime(2020,7,14,22,10,00) 
t90d=t90-ts
t90dh=(t90d.days*24*3600+t90d.seconds-48900)/3600
p90=32.16

##############################
#         15-Jul-20          #
##############################
t91=datetime(2020,7,15,6,5,00) 
t91d=t91-ts
t91dh=(t91d.days*24*3600+t91d.seconds-48900)/3600
p91=32.33

t92=datetime(2020,7,15,17,19,00) 
t92d=t92-ts
t92dh=(t92d.days*24*3600+t92d.seconds-48900)/3600
p92=32.24

##############################
#         16-Jul-20          #
##############################
t93=datetime(2020,7,16,9,13,00) 
t93d=t93-ts
t93dh=(t93d.days*24*3600+t93d.seconds-48900)/3600
p93=32.24

t94=datetime(2020,7,16,10,46,00) 
t94d=t94-ts
t94dh=(t94d.days*24*3600+t94d.seconds-48900)/3600
p94=32.24

t95=datetime(2020,7,16,12,51,00) 
t95d=t95-ts
t95dh=(t95d.days*24*3600+t95d.seconds-48900)/3600
p95=32.16

t96=datetime(2020,7,16,15,30,00) 
t96d=t96-ts
t96dh=(t96d.days*24*3600+t96d.seconds-48900)/3600
p96=31.99

t97=datetime(2020,7,16,22,57,00) 
t97d=t97-ts
t97dh=(t97d.days*24*3600+t97d.seconds-48900)/3600
p97=31.99

##############################
#         17-Jul-20          #
##############################
t98=datetime(2020,7,17,8,44,00) 
t98d=t98-ts
t98dh=(t98d.days*24*3600+t98d.seconds-48900)/3600
p98=32.33

t99=datetime(2020,7,17,16,16,00) 
t99d=t99-ts
t99dh=(t99d.days*24*3600+t99d.seconds-48900)/3600
p99=32.07

t100=datetime(2020,7,17,21,37,00) 
t100d=t100-ts
t100dh=(t100d.days*24*3600+t100d.seconds-48900)/3600
p100=31.99

##############################
#         18-Jul-20          #
##############################
t101=datetime(2020,7,18,10,59,00) 
t101d=t101-ts
t101dh=(t101d.days*24*3600+t101d.seconds-48900)/3600
p101=32.07

t102=datetime(2020,7,18,15,46,00) 
t102d=t102-ts
t102dh=(t102d.days*24*3600+t102d.seconds-48900)/3600
p102=31.90

t103=datetime(2020,7,18,20,48,00) 
t103d=t103-ts
t103dh=(t103d.days*24*3600+t103d.seconds-48900)/3600
p103=31.73

t104=datetime(2020,7,18,22,16,00) 
t104d=t104-ts
t104dh=(t104d.days*24*3600+t104d.seconds-48900)/3600
p104=31.81

##############################
#         19-Jul-20          #
##############################
t105=datetime(2020,7,19,9,9,00) 
t105d=t105-ts
t105dh=(t105d.days*24*3600+t105d.seconds-48900)/3600
p105=32.07

t106=datetime(2020,7,19,14,13,00) 
t106d=t106-ts
t106dh=(t106d.days*24*3600+t106d.seconds-48900)/3600
p106=31.90

t107=datetime(2020,7,19,16,46,00) 
t107d=t107-ts
t107dh=(t107d.days*24*3600+t107d.seconds-48900)/3600
p107=31.81

##############################
#         20-Jul-20          #
##############################
t108=datetime(2020,7,20,7,22,00) 
t108d=t108-ts
t108dh=(t108d.days*24*3600+t108d.seconds-48900)/3600
p108=32.07

t109=datetime(2020,7,20,12,55,00) 
t109d=t109-ts
t109dh=(t109d.days*24*3600+t109d.seconds-48900)/3600
p109=32.07

t110=datetime(2020,7,20,17,8,00) 
t110d=t110-ts
t110dh=(t110d.days*24*3600+t110d.seconds-48900)/3600
p110=31.90

t111=datetime(2020,7,20,18,37,00) 
t111d=t111-ts
t111dh=(t111d.days*24*3600+t111d.seconds-48900)/3600
p111=31.81

##############################
#         21-Jul-20          #
##############################
t112=datetime(2020,7,21,0,13,00) 
t112d=t112-ts
t112dh=(t112d.days*24*3600+t112d.seconds-48900)/3600
p112=31.90

t113=datetime(2020,7,21,7,34,00) 
t113d=t113-ts
t113dh=(t113d.days*24*3600+t113d.seconds-48900)/3600
p113=32.07

t114=datetime(2020,7,21,14,2,00) 
t114d=t114-ts
t114dh=(t114d.days*24*3600+t114d.seconds-48900)/3600
p114=31.99

t115=datetime(2020,7,21,19,53,00) 
t115d=t115-ts
t115dh=(t115d.days*24*3600+t115d.seconds-48900)/3600
p115=31.73

##############################
#         22-Jul-20          #
##############################
t116=datetime(2020,7,22,8,59,00) 
t116d=t116-ts
t116dh=(t116d.days*24*3600+t116d.seconds-48900)/3600
p116=31.99

t117=datetime(2020,7,22,14,7,00) 
t117d=t117-ts
t117dh=(t117d.days*24*3600+t117d.seconds-48900)/3600
p117=31.81

t118=datetime(2020,7,22,20,36,00) 
t118d=t118-ts
t118dh=(t118d.days*24*3600+t118d.seconds-48900)/3600
p118=31.73

##############################
#         23-Jul-20          #
##############################
t119=datetime(2020,7,23,7,52,00) 
t119d=t119-ts
t119dh=(t119d.days*24*3600+t119d.seconds-48900)/3600
p119=31.99

t120=datetime(2020,7,23,13,45,00) 
t120d=t120-ts
t120dh=(t120d.days*24*3600+t120d.seconds-48900)/3600
p120=31.81

t121=datetime(2020,7,23,18,39,00) 
t121d=t121-ts
t121dh=(t121d.days*24*3600+t121d.seconds-48900)/3600
p121=31.55

##############################
#         24-Jul-20          #
##############################

t122=datetime(2020,7,24,0,10,00) 
t122d=t122-ts
t122dh=(t122d.days*24*3600+t122d.seconds-48900)/3600
p122=31.73

t123=datetime(2020,7,24,8,31,00) 
t123d=t123-ts
t123dh=(t123d.days*24*3600+t123d.seconds-48900)/3600
p123=31.99

t124=datetime(2020,7,24,12,12,00) 
t124d=t124-ts
t124dh=(t124d.days*24*3600+t124d.seconds-48900)/3600
p124=31.90

t125=datetime(2020,7,24,18,28,00) 
t125d=t125-ts
t125dh=(t125d.days*24*3600+t125d.seconds-48900)/3600
p125=31.55

t126=datetime(2020,7,24,22,9,00) 
t126d=t126-ts
t126dh=(t126d.days*24*3600+t126d.seconds-48900)/3600
p126=31.81

##############################
#         25-Jul-20          #
##############################

t127=datetime(2020,7,25,7,30,00) 
t127d=t127-ts
t127dh=(t127d.days*24*3600+t127d.seconds-48900)/3600
p127=31.90

t128=datetime(2020,7,25,14,34,00) 
t128d=t128-ts
t128dh=(t128d.days*24*3600+t128d.seconds-48900)/3600
p128=31.64

t129=datetime(2020,7,25,17,11,00) 
t129d=t129-ts
t129dh=(t129d.days*24*3600+t129d.seconds-48900)/3600
p129=31.47

##############################
#         26-Jul-20          #
##############################

t130=datetime(2020,7,26,8,40,00) 
t130d=t130-ts
t130dh=(t130d.days*24*3600+t130d.seconds-48900)/3600
p130=31.73

t131=datetime(2020,7,26,16,4,00) 
t131d=t131-ts
t131dh=(t131d.days*24*3600+t131d.seconds-48900)/3600
p131=31.38

t132=datetime(2020,7,26,21,31,00) 
t132d=t132-ts
t132dh=(t132d.days*24*3600+t132d.seconds-48900)/3600
p132=31.38

##############################
#         27-Jul-20          #
##############################

t133=datetime(2020,7,27,8,20,00) 
t133d=t133-ts
t133dh=(t133d.days*24*3600+t133d.seconds-48900)/3600
p133=31.64

t134=datetime(2020,7,27,14,44,00) 
t134d=t134-ts
t134dh=(t134d.days*24*3600+t134d.seconds-48900)/3600
p134=31.47

##############################
#         28-Jul-20          #
##############################

t135=datetime(2020,7,28,9,6,00) 
t135d=t135-ts
t135dh=(t135d.days*24*3600+t135d.seconds-48900)/3600
p135=31.64

t136=datetime(2020,7,28,15,19,00) 
t136d=t136-ts
t136dh=(t136d.days*24*3600+t136d.seconds-48900)/3600
p136=31.47

t137=datetime(2020,7,28,18,51,00) 
t137d=t137-ts
t137dh=(t137d.days*24*3600+t137d.seconds-48900)/3600
p137=31.30

##############################
#         29-Jul-20          #
##############################

t138=datetime(2020,7,29,9,4,00) 
t138d=t138-ts
t138dh=(t138d.days*24*3600+t138d.seconds-48900)/3600
p138=31.55

t139=datetime(2020,7,29,13,59,00) 
t139d=t139-ts
t139dh=(t139d.days*24*3600+t139d.seconds-48900)/3600
p139=31.47

t140=datetime(2020,7,29,19,4,00) 
t140d=t140-ts
t140dh=(t140d.days*24*3600+t140d.seconds-48900)/3600
p140=31.12

##############################
#         30-Jul-20          #
##############################

t141=datetime(2020,7,30,8,48,00) 
t141d=t141-ts
t141dh=(t141d.days*24*3600+t141d.seconds-48900)/3600
p141=31.47

t142=datetime(2020,7,30,14,2,00) 
t142d=t142-ts
t142dh=(t142d.days*24*3600+t142d.seconds-48900)/3600
p142=31.47

t143=datetime(2020,7,30,22,28,00) 
t143d=t143-ts
t143dh=(t143d.days*24*3600+t143d.seconds-48900)/3600
p143=31.21

##############################
#         31-Jul-20          #
##############################
t144=datetime(2020,7,31,8,49,00) 
t144d=t144-ts
t144dh=(t144d.days*24*3600+t144d.seconds-48900)/3600
p144=31.47

t145=datetime(2020,7,31,16,15,00) 
t145d=t145-ts
t145dh=(t145d.days*24*3600+t145d.seconds-48900)/3600
p145=31.21

t146=datetime(2020,7,31,21,12,00) 
t146d=t146-ts
t146dh=(t146d.days*24*3600+t146d.seconds-48900)/3600
p146=31.12

##############################
#          1-Aug-20          #
##############################
t147=datetime(2020,8,1,11,48,00) 
t147d=t147-ts
t147dh=(t147d.days*24*3600+t147d.seconds-48900)/3600
p147=31.38

t148=datetime(2020,8,1,14,49,00) 
t148d=t148-ts
t148dh=(t148d.days*24*3600+t148d.seconds-48900)/3600
p148=31.30

t149=datetime(2020,8,1,22,12,00) 
t149d=t149-ts
t149dh=(t149d.days*24*3600+t149d.seconds-48900)/3600
p149=31.21

##############################
#          2-Aug-20          #
##############################
t150=datetime(2020,8,2,11,18,00) 
t150d=t150-ts
t150dh=(t150d.days*24*3600+t150d.seconds-48900)/3600
p150=31.38

t151=datetime(2020,8,2,18,40,00) 
t151d=t151-ts
t151dh=(t151d.days*24*3600+t151d.seconds-48900)/3600
p151=30.95

##############################
#          3-Aug-20          #
##############################
t152=datetime(2020,8,3,7,46,00) 
t152d=t152-ts
t152dh=(t152d.days*24*3600+t152d.seconds-48900)/3600
p152=31.30

t153=datetime(2020,8,3,15,26,00) 
t153d=t153-ts
t153dh=(t153d.days*24*3600+t153d.seconds-48900)/3600
p153=31.04

##############################
#          4-Aug-20          #
##############################
t154=datetime(2020,8,4,7,27,00) 
t154d=t154-ts
t154dh=(t154d.days*24*3600+t154d.seconds-48900)/3600
p154=31.12

t155=datetime(2020,8,4,15,59,00) 
t155d=t155-ts
t155dh=(t155d.days*24*3600+t155d.seconds-48900)/3600
p155=31.04

t156=datetime(2020,8,4,21,16,00) 
t156d=t156-ts
t156dh=(t156d.days*24*3600+t156d.seconds-48900)/3600
p156=31.04

##############################
#          5-Aug-20          #
##############################
t157=datetime(2020,8,5,8,40,00) 
t157d=t157-ts
t157dh=(t157d.days*24*3600+t157d.seconds-48900)/3600
p157=31.21

t158=datetime(2020,8,5,20,49,00) 
t158d=t158-ts
t158dh=(t158d.days*24*3600+t158d.seconds-48900)/3600
p158=31.21

##############################
#          6-Aug-20          #
##############################
t159=datetime(2020,8,6,8,0,00) 
t159d=t159-ts
t159dh=(t159d.days*24*3600+t159d.seconds-48900)/3600
p159=31.30

t160=datetime(2020,8,6,17,17,00) 
t160d=t160-ts
t160dh=(t160d.days*24*3600+t160d.seconds-48900)/3600
p160=30.95

##############################
#          7-Aug-20          #
##############################
t161=datetime(2020,8,7,7,58,00) 
t161d=t161-ts
t161dh=(t161d.days*24*3600+t161d.seconds-48900)/3600
p161=31.21

t162=datetime(2020,8,7,17,58,00) 
t162d=t162-ts
t162dh=(t162d.days*24*3600+t162d.seconds-48900)/3600
p162=30.69

##############################
#          8-Aug-20          #
##############################
t163=datetime(2020,8,8,8,8,00) 
t163d=t163-ts
t163dh=(t163d.days*24*3600+t163d.seconds-48900)/3600
p163=30.95

t164=datetime(2020,8,8,21,45,00) 
t164d=t164-ts
t164dh=(t164d.days*24*3600+t164d.seconds-48900)/3600
p164=30.52

##############################
#          9-Aug-20          #
##############################
t165=datetime(2020,8,9,9,23,00) 
t165d=t165-ts
t165dh=(t165d.days*24*3600+t165d.seconds-48900)/3600
p165=30.86

t166=datetime(2020,8,9,16,20,00) 
t166d=t166-ts
t166dh=(t166d.days*24*3600+t166d.seconds-48900)/3600
p166=30.52

##############################
#         10-Aug-20          #
##############################
t167=datetime(2020,8,10,9,10,00) 
t167d=t167-ts
t167dh=(t167d.days*24*3600+t167d.seconds-48900)/3600
p167=30.69

t168=datetime(2020,8,10,19,47,00) 
t168d=t168-ts
t168dh=(t168d.days*24*3600+t168d.seconds-48900)/3600
p168=30.52

##############################
#         11-Aug-20          #
##############################
t169=datetime(2020,8,11,9,25,00) 
t169d=t169-ts
t169dh=(t169d.days*24*3600+t169d.seconds-48900)/3600
p169=30.78

t170=datetime(2020,8,11,21,42,00) 
t170d=t170-ts
t170dh=(t170d.days*24*3600+t170d.seconds-48900)/3600
p170=30.61

##############################
#         12-Aug-20          #
##############################
t171=datetime(2020,8,12,9,11,00) 
t171d=t171-ts
t171dh=(t171d.days*24*3600+t171d.seconds-48900)/3600
p171=30.78

t172=datetime(2020,8,12,20,28,00) 
t172d=t172-ts
t172dh=(t172d.days*24*3600+t172d.seconds-48900)/3600
p172=30.35

##############################
#         13-Aug-20          #
##############################
t173=datetime(2020,8,13,8,32,00) 
t173d=t173-ts
t173dh=(t173d.days*24*3600+t173d.seconds-48900)/3600
p173=30.69

t174=datetime(2020,8,13,17,15,00) 
t174d=t174-ts
t174dh=(t174d.days*24*3600+t174d.seconds-48900)/3600
p174=30.35

##############################
#         14-Aug-20          #
##############################
t175=datetime(2020,8,14,10,21,00) 
t175d=t175-ts
t175dh=(t175d.days*24*3600+t175d.seconds-48900)/3600
p175=30.43

t176=datetime(2020,8,14,14,12,00) 
t176d=t176-ts
t176dh=(t176d.days*24*3600+t176d.seconds-48900)/3600
p176=30.26

##############################
#         15-Aug-20          #
##############################
t177=datetime(2020,8,15,9,2,00) 
t177d=t177-ts
t177dh=(t177d.days*24*3600+t177d.seconds-48900)/3600
p177=30.35

t178=datetime(2020,8,15,15,51,00) 
t178d=t178-ts
t178dh=(t178d.days*24*3600+t178d.seconds-48900)/3600
p178=29.92

##############################
#         16-Aug-20          #
##############################
t179=datetime(2020,8,16,9,36,00) 
t179d=t179-ts
t179dh=(t179d.days*24*3600+t179d.seconds-48900)/3600
p179=30.09

t180=datetime(2020,8,16,15,15,00) 
t180d=t180-ts
t180dh=(t180d.days*24*3600+t180d.seconds-48900)/3600
p180=29.92

##############################
#         17-Aug-20          #
##############################
t181=datetime(2020,8,17,7,1,00) 
t181d=t181-ts
t181dh=(t181d.days*24*3600+t181d.seconds-48900)/3600
p181=30.09

t182=datetime(2020,8,17,17,45,00) 
t182d=t182-ts
t182dh=(t182d.days*24*3600+t182d.seconds-48900)/3600
p182=29.83

##############################
#         18-Aug-20          #
##############################
t183=datetime(2020,8,18,8,24,00) 
t183d=t183-ts
t183dh=(t183d.days*24*3600+t183d.seconds-48900)/3600
p183=30.00

t184=datetime(2020,8,18,15,35,00) 
t184d=t184-ts
t184dh=(t184d.days*24*3600+t184d.seconds-48900)/3600
p184=29.83

##############################
#         19-Aug-20          #
##############################
t185=datetime(2020,8,19,12,18,00) 
t185d=t185-ts
t185dh=(t185d.days*24*3600+t185d.seconds-48900)/3600
p185=30.00

t186=datetime(2020,8,19,18,35,00) 
t186d=t186-ts
t186dh=(t186d.days*24*3600+t186d.seconds-48900)/3600
p186=29.74

##############################
#         20-Aug-20          #
##############################
t187=datetime(2020,8,20,9,46,00) 
t187d=t187-ts
t187dh=(t187d.days*24*3600+t187d.seconds-48900)/3600
p187=30.09

t188=datetime(2020,8,20,17,46,00) 
t188d=t188-ts
t188dh=(t188d.days*24*3600+t188d.seconds-48900)/3600
p188=29.83

##############################
#         21-Aug-20          #
##############################
t189=datetime(2020,8,21,9,5,00) 
t189d=t189-ts
t189dh=(t189d.days*24*3600+t189d.seconds-48900)/3600
p189=30.09

t190=datetime(2020,8,21,17,20,00) 
t190d=t190-ts
t190dh=(t190d.days*24*3600+t190d.seconds-48900)/3600
p190=29.83

##############################
#         22-Aug-20          #
##############################
t191=datetime(2020,8,22,14,17,00) 
t191d=t191-ts
t191dh=(t191d.days*24*3600+t191d.seconds-48900)/3600
p191=29.74

t192=datetime(2020,8,22,18,49,00) 
t192d=t192-ts
t192dh=(t192d.days*24*3600+t192d.seconds-48900)/3600
p192=29.66

##############################
#         23-Aug-20          #
##############################
t193=datetime(2020,8,23,10,36,00) 
t193d=t193-ts
t193dh=(t193d.days*24*3600+t193d.seconds-48900)/3600
p193=30.09

t194=datetime(2020,8,23,21,37,00) 
t194d=t194-ts
t194dh=(t194d.days*24*3600+t194d.seconds-48900)/3600
p194=29.83

##############################
#         24-Aug-20          #
##############################
t195=datetime(2020,8,24,8,2,00) 
t195d=t195-ts
t195dh=(t195d.days*24*3600+t195d.seconds-48900)/3600
p195=29.92

t196=datetime(2020,8,24,18,30,00) 
t196d=t196-ts
t196dh=(t196d.days*24*3600+t196d.seconds-48900)/3600
p196=29.74

##############################
#         25-Aug-20          #
##############################
t197=datetime(2020,8,25,7,57,00) 
t197d=t197-ts
t197dh=(t197d.days*24*3600+t197d.seconds-48900)/3600
p197=29.92

t198=datetime(2020,8,25,18,59,00) 
t198d=t198-ts
t198dh=(t198d.days*24*3600+t198d.seconds-48900)/3600
p198=29.66

##############################
#         27-Aug-20          #
##############################
t199=datetime(2020,8,27,7,54,00) 
t199d=t199-ts
t199dh=(t199d.days*24*3600+t199d.seconds-48900)/3600
p199=29.92

t200=datetime(2020,8,27,17,19,00) 
t200d=t200-ts
t200dh=(t200d.days*24*3600+t200d.seconds-48900)/3600
p200=29.83

t201=datetime(2020,8,27,19,16,00) 
t201d=t201-ts
t201dh=(t201d.days*24*3600+t201d.seconds-48900)/3600
p201=29.83

##############################
#         28-Aug-20          #
##############################
t202=datetime(2020,8,28,8,32,00) 
t202d=t202-ts
t202dh=(t202d.days*24*3600+t202d.seconds-48900)/3600
p202=30.0

t203=datetime(2020,8,28,8,32,00) 
t203d=t203-ts
t203dh=(t203d.days*24*3600+t203d.seconds-48900)/3600
p203=29.66

##############################
#         29-Aug-20          #
##############################
t204=datetime(2020,8,29,12,23,00) 
t204d=t204-ts
t204dh=(t204d.days*24*3600+t204d.seconds-48900)/3600
p204=29.83

t205=datetime(2020,8,29,19,6,00) 
t205d=t205-ts
t205dh=(t205d.days*24*3600+t205d.seconds-48900)/3600
p205=29.66

##############################
#         30-Aug-20          #
##############################
t206=datetime(2020,8,30,11,50,00) 
t206d=t206-ts
t206dh=(t206d.days*24*3600+t206d.seconds-48900)/3600
p206=29.92

##############################
#         31-Aug-20          #
##############################

t207=datetime(2020,8,31,9,37,00) 
t207d=t207-ts
t207dh=(t207d.days*24*3600+t207d.seconds-48900)/3600
p207=29.92

t208=datetime(2020,8,31,19,28,00) 
t208d=t208-ts
t208dh=(t208d.days*24*3600+t208d.seconds-48900)/3600
p208=29.48

##############################
#          1-Sep-20          #
##############################

t209=datetime(2020,9,1,9,30,00) 
t209d=t209-ts
t209dh=(t209d.days*24*3600+t209d.seconds-48900)/3600
p209=29.83

##############################
#          2-Sep-20          #
##############################

t210=datetime(2020,9,2,12,28,00) 
t210d=t210-ts
t210dh=(t210d.days*24*3600+t210d.seconds-48900)/3600
p210=29.83

##############################
#          4-Sep-20          #
##############################

t211=datetime(2020,9,4,13,52,00) 
t211d=t211-ts
t211dh=(t211d.days*24*3600+t211d.seconds-48900)/3600
p211=29.66

##############################
#          5-Sep-20          #
##############################

t212=datetime(2020,9,5,13,13,00) 
t212d=t212-ts
t212dh=(t212d.days*24*3600+t212d.seconds-48900)/3600
p212=29.48

t213=datetime(2020,9,5,22,54,00) 
t213d=t213-ts
t213dh=(t213d.days*24*3600+t213d.seconds-48900)/3600
p213=29.05

##############################
#          6-Sep-20          #
##############################

t214=datetime(2020,9,6,9,39,00) 
t214d=t214-ts
t214dh=(t214d.days*24*3600+t214d.seconds-48900)/3600
p214=29.48

##############################
#          7-Sep-20          #
##############################

t215=datetime(2020,9,7,8,43,00) 
t215d=t215-ts
t215dh=(t215d.days*24*3600+t215d.seconds-48900)/3600
p215=29.31

t216=datetime(2020,9,7,17,12,00) 
t216d=t216-ts
t216dh=(t216d.days*24*3600+t216d.seconds-48900)/3600
p216=28.88

##############################
#          8-Sep-20          #
##############################

t217=datetime(2020,9,8,8,8,00) 
t217d=t217-ts
t217dh=(t217d.days*24*3600+t217d.seconds-48900)/3600
p217=29.40

t218=datetime(2020,9,8,20,38,00) 
t218d=t218-ts
t218dh=(t218d.days*24*3600+t218d.seconds-48900)/3600
p218=29.14

##############################
#          9-Sep-20          #
##############################

t219=datetime(2020,9,9,11,57,00) 
t219d=t219-ts
t219dh=(t219d.days*24*3600+t219d.seconds-48900)/3600
p219=29.31

t220=datetime(2020,9,9,20,55,00) 
t220d=t220-ts
t220dh=(t220d.days*24*3600+t220d.seconds-48900)/3600
p220=29.40

##############################
#         10-Sep-20          #
##############################

t221=datetime(2020,9,10,11,50,00) 
t221d=t221-ts
t221dh=(t221d.days*24*3600+t221d.seconds-48900)/3600
p221=29.31

##############################
#         11-Sep-20          #
##############################

t222=datetime(2020,9,11,7,50,00) 
t222d=t222-ts
t222dh=(t222d.days*24*3600+t222d.seconds-48900)/3600
p222=29.57

##############################
#         12-Sep-20          #
##############################

t223=datetime(2020,9,12,18,3,00) 
t223d=t223-ts
t223dh=(t223d.days*24*3600+t223d.seconds-48900)/3600
p223=29.14

##############################
#         13-Sep-20          #
##############################

t224=datetime(2020,9,13,11,16,00) 
t224d=t224-ts
t224dh=(t224d.days*24*3600+t224d.seconds-48900)/3600
p224=29.40

##############################
#         14-Sep-20          #
##############################

t225=datetime(2020,9,14,14,40,00) 
t225d=t225-ts
t225dh=(t225d.days*24*3600+t225d.seconds-48900)/3600
p225=29.23

##############################
#         15-Sep-20          #
##############################

t226=datetime(2020,9,15,12,8,00) 
t226d=t226-ts
t226dh=(t226d.days*24*3600+t226d.seconds-48900)/3600
p226=29.31

##############################
#         16-Sep-20          #
##############################

t227=datetime(2020,9,16,15,29,00) 
t227d=t227-ts
t227dh=(t227d.days*24*3600+t227d.seconds-48900)/3600
p227=28.97

##############################
#         17-Sep-20          #
##############################

t228=datetime(2020,9,17,11,38,00) 
t228d=t228-ts
t228dh=(t228d.days*24*3600+t228d.seconds-48900)/3600
p228=29.14

##############################
#         18-Sep-20          #
##############################

t229=datetime(2020,9,18,10,24,00) 
t229d=t229-ts
t229dh=(t229d.days*24*3600+t229d.seconds-48900)/3600
p229=29.05

##############################
#         19-Sep-20          #
##############################

t230=datetime(2020,9,19,12,18,00) 
t230d=t230-ts
t230dh=(t230d.days*24*3600+t230d.seconds-48900)/3600
p230=29.05

##############################
#         20-Sep-20          #
##############################

t231=datetime(2020,9,20,13,43,00) 
t231d=t231-ts
t231dh=(t231d.days*24*3600+t231d.seconds-48900)/3600
p231=29.05

##############################
#         21-Sep-20          #
##############################

t232=datetime(2020,9,21,11,12,00) 
t232d=t232-ts
t232dh=(t232d.days*24*3600+t232d.seconds-48900)/3600
p232=29.14

##############################
#         22-Sep-20          #
##############################

t233=datetime(2020,9,22,9,3,00) 
t233d=t233-ts
t233dh=(t233d.days*24*3600+t233d.seconds-48900)/3600
p233=29.05

##############################
#         23-Sep-20          #
##############################

t234=datetime(2020,9,23,9,2,00) 
t234d=t234-ts
t234dh=(t234d.days*24*3600+t234d.seconds-48900)/3600
p234=29.48

##############################
#         24-Sep-20          #
##############################

t235=datetime(2020,9,24,11,53,00) 
t235d=t235-ts
t235dh=(t235d.days*24*3600+t235d.seconds-48900)/3600
p235=28.97

##############################
#         25-Sep-20          #
##############################

t236=datetime(2020,9,25,14,49,00) 
t236d=t236-ts
t236dh=(t236d.days*24*3600+t236d.seconds-48900)/3600
p236=28.88

##############################
#         26-Sep-20          #
##############################

t237=datetime(2020,9,26,15,9,00) 
t237d=t237-ts
t237dh=(t237d.days*24*3600+t237d.seconds-48900)/3600
p237=28.79

##############################
#         27-Sep-20          #
##############################

t238=datetime(2020,9,27,11,9,00) 
t238d=t238-ts
t238dh=(t238d.days*24*3600+t238d.seconds-48900)/3600
p238=28.88

##############################
#         28-Sep-20          #
##############################

t239=datetime(2020,9,28,15,35,00) 
t239d=t239-ts
t239dh=(t239d.days*24*3600+t239d.seconds-48900)/3600
p239=28.54

##############################
#         29-Sep-20          #
##############################

t240=datetime(2020,9,29,20,42,00) 
t240d=t240-ts
t240dh=(t240d.days*24*3600+t240d.seconds-48900)/3600
p240=28.45

##############################
#         30-Sep-20          #
##############################

t241=datetime(2020,9,30,18,21,00) 
t241d=t241-ts
t241dh=(t241d.days*24*3600+t241d.seconds-48900)/3600
p241=28.36

##############################
#          1-Oct-20          #
##############################

t242=datetime(2020,10,1,12,25,00) 
t242d=t242-ts
t242dh=(t242d.days*24*3600+t242d.seconds-48900)/3600
p242=28.36

##############################
#          2-Oct-20          #
##############################

t243=datetime(2020,10,2,16,14,00) 
t243d=t243-ts
t243dh=(t243d.days*24*3600+t243d.seconds-48900)/3600
p243=28.45

t244=datetime(2020,10,2,17,33,00) 
t244d=t244-ts
t244dh=(t244d.days*24*3600+t244d.seconds-48900)/3600
p244=28.45
"""