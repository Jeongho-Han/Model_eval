"""
This codes calculate and print the statistic criteria (NSE, PBIASE, R2, RMSE) 
by importing functions in 'Basic_cal.py'.
Also, this creates a scatter and line plot based on given observation and simulation data (currently )
"""
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sns
import pandas as pd
import os
from tkinter import *
from tkinter import filedialog
from pandas import ExcelFile
from pandas import ExcelWriter
from Basic_cal import BasicStat


#Read data file(*.xlsx; *.xls; *.csv)
data_path = filedialog.askopenfilename(title='data file selection', filetype=(("Excel", "*.xlsx"), ("Excel", "*.xls"), ("CSV", "*.csv"), ("all files", "*,*")))
filename, file_extension = os.path.splitext(data_path)
if file_extension == ".xlsx":
    data =  pd.read_excel(data_path,sheet_name='Sheet1', engine='openpyxl')
elif file_extension == ".xls":
    data =  pd.read_excel(data_path)
elif file_extension == ".csv":
    data =  pd.read_csv(data_path)

data['Date'] = pd.to_datetime(data['Date'])   #Read date
date = data['Date']
obs = data['obs']
sim = data['sim']

#Print statistic criteria
criteria = BasicStat(obs, sim)  #define parameters
criteria.NSE()
criteria.PBIAS()
criteria.R2()
criteria.RMSE()

# Scatter plot 
pt.figure(figsize= (6,6))
pt.grid()
pt.gca().set_aspect("equal")
plot = pt.scatter(obs,sim, c=sim, s=5, vmin=min(obs), vmax=max(obs))
pt.colorbar(plot, shrink=0.8)
pt.plot(obs,obs,label = '1:1')

z = np.polyfit(obs,sim,1)
p = np.poly1d(z)
pt.plot(obs,p(obs),"r--",label='Trend line') #plot a trend line

pt.xlabel("Observation", fontsize='large')
pt.ylabel("Simulation", fontsize='large')
pt.legend(loc='best')

pt.legend(loc='best',shadow=True, fontsize='medium')
pt.xticks(fontsize=14)
pt.yticks(fontsize=14)
pt.show()

#Line plot
pt.figure(figsize= (12,8))
sns.lineplot(x='Date',y='obs',data=data,label = "Observation",linewidth=3)
sns.lineplot(x='Date',y='sim',data=data, label = 'Simulation',linewidth=3)
pt.xlabel("")
pt.ylabel("Streamflow(m$^3$/s)", fontsize='x-large')
pt.legend(loc='best',shadow=True, fontsize='large')
pt.xticks(fontsize=14)
pt.yticks(fontsize=14)
pt.show()