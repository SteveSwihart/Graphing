# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 09:09:46 2020

@author: Steve
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid.inset_locator import inset_axes,InsetPosition,mark_inset
mpl.rcParams['figure.dpi'] = 300 #needed to increase resolution

dataV31 = pd.read_csv('ViolumasTriColorV3.1Data.txt', delimiter=',')

datalen=len(dataV31)
print('Number of Non-Heading Rows', datalen)
print(dataV31)

print('\n------------------\ninfo on data:\n')
dataV31.info()

dfBig = pd.DataFrame(dataV31,columns=['itemNo','year','month','day','hour','minutes','seconds','Ta','Tf','V1','V2','I','OP','OffsetH'])

# Time
dfT=dfBig[['year','month','day','hour','minutes','seconds']]
#dfT=dfBig[['itemNo','year','month','day','hour','minutes','Ta','Tf','V','I','OP','OffsetH']]
print('\ndataframe of time in year, month,day,hour,minutes,seconds:\n',dfT)
dfTP=pd.to_datetime(dfT)
print('\n-----------------------------\ndataframe of time in datetime format:\n',dfTP)
dfBig['dateTime']=dfTP
#ts = datetime(2020,6,26, 17, 30, 00)
dfBig['start']=pd.Timestamp('2020-10-18T141700')
dfBig['deltaT']=dfBig['dateTime']-dfBig['start']
dfBig['dTT']=dfBig['deltaT']/np.timedelta64(1,'h')
dfBig['dTTh']=dfBig['dTT']-dfBig['OffsetH']
TimeHours=dfBig['dTTh']
print('\n-----------------------------\ntime in hours - Offset:\n',TimeHours)

# Creating The Dataframes for everything not Time-related
OP=pd.DataFrame(dataV31,columns=['OP'])
Ta=pd.DataFrame(dataV31,columns=['Ta'])
Tf=pd.DataFrame(dataV31,columns=['Tf'])
V1=pd.DataFrame(dataV31,columns=['V1'])
V2=pd.DataFrame(dataV31,columns=['V2'])
Vsum=dfBig['V1']+dfBig['V2']
dfBig['V']=Vsum
I=pd.DataFrame(dataV31,columns=['I'])

# Electrical Power
#EP=V.mul(I.values) #This works too. Tried both df and np
#EP=np.multiply(V,I)
EP=dfBig['V']*dfBig['I']
dfBig['EP']=EP

print('\n----------------------------\n',dfBig)

# Plotting Setup
fig = plt.figure(figsize=(5,8),linewidth=6,edgecolor="#322288")
heights=[4,2,1.5]
import matplotlib.gridspec as gridspec
gs=gridspec.GridSpec(3,1,height_ratios=heights,figure=fig)
fig.patch.set_facecolor('#bfecfc') # ffdcfc Violumas 1x12 #2
fig.subplots_adjust(left=None, bottom=.1, right=None, top=.9, wspace=0.2, hspace=None)

"""
Text boxes to show total elapsed days (on left) hours (on right)
   need to float so that don't have [ and ] displayed around value
   formatting to 2 decimal places - %.2f ... or 3f if wanted 3 dec plcs, 
      then % outside quotes then calc value.
"""
ElT=float("%.2f" % TimeHours[datalen-1])
ElDFloat=ElT/24
ElD=float("%.1f" % ElDFloat)
plt.figtext(.001,.95,f"Total days = {ElD}",fontstyle='italic',color="#eeeeee",backgroundcolor="#8888cc")
plt.figtext(.88,.95,f"Total hrs = {ElT}",fontstyle='italic',color="#eeeeee",backgroundcolor="#8888cc")


# Plotting Traces
from matplotlib import ticker
#import matplotlib.ticker #used in subsequent plots too, with axX.minorticks_on()
# class MyLocator(matplotlib.ticker.AutoMinorLocator):
#     def __init__(self, n=5): # n changes # of tickes. Drawn = n-1, spaces =n
#         super().__init__(n=n)
# matplotlib.ticker.AutoMinorLocator = MyLocator   

n=5
xticks=ticker.MaxNLocator(n)

ax1=fig.add_subplot(gs[0,:],fc="#dcf1f5")
ax1.minorticks_on()
ax1.grid(which='major', linestyle='--', color='#828282')
ax1.grid(which='minor', linestyle=':', color='#c2c2c2')
#ax1.tick_params(axis="x",top=True) #makes ticks appear on top also
ax1.tick_params(axis="x",labeltop=True,labelbottom=False)
ax1.set_title('         '+r'$\bf{Violumas}$'+ ' TriColor V3.1 (UV) \n         4 Parallel Strings, 6 ea, ~33V, 2A', pad=8)
ax1.set_xlabel('Time (hours)', fontsize=10)
ax1.set_ylabel('Total Optical Power, nW', color="#074f82")
ax1.plot(TimeHours,OP,label="Optical Power, Total",marker='.', markeredgecolor='#006500')

ax1r=ax1.twinx()
OPrel=OP/OP.iloc[0]
ax1r.set_ylabel('Optical Power Relative to Start',color="#006500")
ax1r.plot(TimeHours,OPrel,label="Optical Power, Relative",marker='.', markeredgecolor='#006500')

#Trend Line
deltaPow=-.078
ax1r.arrow(0,.948,max(TimeHours),deltaPow,linestyle='-.',color='#ee5522')

#Trend Line for Eotron (starting at 2732.58,.826, val=28.4, bet pts 263 and 264 @ 28.45 and 28.28, use 28.4) over same period
# Eotron test ended to cool 16-Nov-20,17:05 @ 3376.45 hrs (=28.28), off ~9 days (212.25 hrs), 
# since Violumas TriColor start = 643.87 as of Eotron data point 291
deltaEO=-0.0019
ax1r.arrow(0,.948,max(TimeHours)-212.5+30.583,deltaEO,color='green')


#Box with decay rate - calculating the #s
boxValue=deltaPow/(max(TimeHours)/100)
boxText='decay rate = ~' + str("%.3f" % boxValue) +' % per hour'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

###############################################################################
# Placement of text box:                                                      #
#   x: at .3*(total hrs)                                                      #
#   y: taking the span of prel (right vert axis), 33% of that, added to min.  #
#     (Should stay put.)                                                      #
###############################################################################
ax1r.text((0.01*max(TimeHours)),(OPrel.min()+.01*(1-OPrel.min())),boxText,bbox=props)

#box labeling the Eotron line
ax1r.annotate('Eotron Decay\nduring same time',fontsize='9',color='#322288', ha='center',
            xy=(400, .947), xycoords='data',
            xytext=(85, -25), textcoords='offset points',
            bbox=dict(boxstyle="round4", fc="#bfecfc"),
            arrowprops=dict(arrowstyle="-", color='#08d0fc',
                            connectionstyle="angle,angleA=0,angleB=270,rad=25"))

#box at 521 hrs (heavy use time complete)
ax1r.annotate('521 hrs, \n5yrs heavy use',color='#eea5ee', ha='center',
            xy=(521, .92), xycoords='data',
            xytext=(-20, -45), textcoords='offset points',
            bbox=dict(boxstyle="roundtooth", fc="#228822"),
            arrowprops=dict(arrowstyle="->", color='yellow',
                            connectionstyle="angle,angleA=0,angleB=90,rad=25"))

#inset plot - LED spectra
#axins = inset_axes(ax1, width="34%", height="32%",borderpad=3) #works, but same pad x and y
axins = inset_axes(ax1, width="32%", height="29%",bbox_to_anchor=(.62,.63,.9,.93),bbox_transform=(ax1.transAxes),loc=3)
axins.set_title('LED Spectra @ 836 hrs',fontsize=10)
axins.patch.set_facecolor('purple')
# axins.text(275,0.5, "Take my \ndata \nalready!", horizontalalignment='center', verticalalignment='center',c='#dddddd') #x and y first terms are in plot coords
df = pd.read_csv('Violumas3_1_LED_Spectral_Data.txt',delimiter='\t',skiprows=17)
df.columns=["nm", "Intensity"]
w=df['nm'].tolist()
Intens=df['Intensity'].tolist()
xticks=ticker.MaxNLocator(3)
axins.minorticks_on()
axins.set_xlim(255,305)
axins.grid(which='major', linestyle='-',color="#bb8888")
axins.grid(which='minor', linestyle=':',color="#bb7777")
axins.set_yticklabels([])
axins.plot(w,Intens)

# Cold Power On Graph
axins2=inset_axes(ax1, width="26%", height="25%", bbox_to_anchor=(.113,.66,.8,.95),bbox_transform=(ax1.transAxes),loc=3)
axins2.set_title('Cold Pwr On Detail',fontsize=10)
axins2.set_xlim(593,598)
axins2.plot(TimeHours,OPrel)

# Temp Plot, Ambient and Fab, blue curve, left ax labels
ax2=fig.add_subplot(gs[1,0], xticklabels=[],fc="#f7f2dc")
ax2.grid(which='major', linestyle='-', color='#b699a2')
ax2.minorticks_on()
ax2.grid(which='minor', linestyle=':', color='#b699a2')
ax2.set_ylabel('Temp ($^\circ$C), amb', color="#074f82")
ax2.set_ylim(17,45)
ax2.tick_params(axis="y",labelrotation=20,color="#074f82",labelcolor="#074f82")
ax2.plot(TimeHours,Ta,marker='d', markersize='4',markerfacecolor='#aa6500',markeredgecolor='red')

ax2r=ax2.twinx()
ax2r.set_ylim(23,50)
ax2r.set_ylabel('Temp ($^\circ$C), fab',color="#c74204")
ax2r.tick_params(axis="y",labelrotation=-20,color="#c74204",labelcolor="#c74204")
ax2r.plot(TimeHours,Tf, color="orange", marker='|',markerfacecolor='#aa6500',markeredgecolor='red')
#ax2.legend(fontsize='small',facecolor="#fde77e",edgecolor="black") #bbox_to_anchor=[.5,.5],

# Plot V, I, Watts
from mpl_toolkits.axes_grid1 import host_subplot
ax3=host_subplot(gs[2,0],fc="#fca8f8")
ax3.set_ylabel('Voltage (V)', color="#074f82")
ax3.tick_params(axis="y",labelrotation=20,color="#074f82",labelcolor="#074f82")
ax3.grid(which='major', linestyle=':', color='#eeeeee')
ax3.plot(TimeHours,dfBig['V'],marker='1',markeredgecolor='cyan')
ax3par1=ax3.twinx()
ax3par1.set_ylim(1.9,2.1)
from matplotlib.ticker import FormatStrFormatter
ax3par1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
ax3par1.tick_params(axis="y",labelrotation=20,color="#074f82",labelcolor="#074f82")
ax3par1.set_ylabel('Current (A)',color="#006500")
ax3par1.tick_params(axis="y",labelrotation=-20,color="#006500",labelcolor="#006500")
ax3par1.plot(TimeHours,I, color="#009500",marker='.',markeredgecolor="orange")

#ax3=plt.subplot2grid((5,4),(3,0),colspan=3, xticklabels=[])
#ax3.grid(which='major')
#ax3.minorticks_on()
#ax3.grid(which='minor', linestyle=':')
#ax3.set_ylabel('Power (AC Watts)', color="#074f82")
ax3par2=ax3.twinx()
ax3par2.spines["right"].set_position(("axes",1.172))
ax3par2.set_ylabel('Power (W)',color='#c74204')
ax3par2.tick_params(axis="y",labelrotation=0,labelcolor="#c74204") #for tick line color color="#ffd953", was too bright
ax3par2.plot(TimeHours,EP,color="#c96224")

#plt.legend(bbox_to_anchor=(1,1))

#plt.tight_layout()
plt.show()