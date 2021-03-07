"""
Criteria computation 
R2: Coefficient of Determination
NSE: Nash-Sutcliffe Efficiency
PBIAS: Percent bias

"""
# class Criteria:
#     def __init__(self, sim, obs):
#         self.sim = sim
#         self.obs = obs

#     def R2(self):

import numpy as np
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter
import matplotlib.pyplot as pt
import seaborn as sns

# Calculate the criteria for model perfomance evaluation 
def NSE(obs: list, sim: list) -> float:
    denominator = np.sum((obs-np.mean(obs))**2)
    numerator = np.sum((obs-sim)**2)
    if denominator == 0:
        print("Error: denominator is '0'.")
    else:
        NSE = 1 - (numerator/denominator)
        NSE = round(NSE,3)
    print("NSE")
    return NSE

def PBIAS(obs: list, sim: list) -> float:
    denominator = np.sum(obs)
    numerator = np.sum(sim-obs)
    if denominator == 0:
        print("Error: denominator is '0'.")
    else:
        pbias = 100*(numerator/denominator)
        pbias = round(pbias,3)
    print("PBIAS")
    return pbias


def R2(obs: list, sim: list) -> float:
    corr = np.corrcoef(obs,sim)
    corr = corr[0,1]
    R2 = round(corr**2,3)
    print("R2")
    return R2

def RMSE(obs: list, sim: list) -> float:
    RMSE = np.sqrt(((sim-obs)**2).mean())
    RMSE = round(RMSE,3)
    print("RMSE:")
    return RMSE



# Read data file (excel)
data =  pd.read_excel('streamflow_andong.xlsx',sheet_name='Sheet1', engine='openpyxl')
obs = data['obs']
sim = data['sim']

#Function check
print(NSE(obs, sim))
print(PBIAS(obs,sim))
print(R2(obs,sim))
print(RMSE(obs,sim))


# Scatter plot comparison
pt.figure(figsize= (6,6))
pt.grid()
pt.gca().set_aspect("equal")

pt.scatter(obs,sim, color='g')
pt.plot(obs,obs,label = '1:1')

z = np.polyfit(obs,sim,1)
p = np.poly1d(z)
pt.plot(obs,p(obs),"r--",label='trend line')

pt.xlabel("Observation", fontsize='large')
pt.ylabel("Simulation", fontsize='large')
pt.legend(loc='best')

pt.legend(loc='best',shadow=True, fontsize='large')
pt.xticks(fontsize=14)
pt.yticks(fontsize=14)
pt.show()


#Line plot
sample_data =  pd.read_excel('streamflow_andong.xlsx',sheet_name='Sheet1', engine='openpyxl')
sample_data['Date'] = pd.to_datetime(sample_data['Date'])

pt.figure(figsize= (12,8))
sns.lineplot(x='Date',y='obs',data=sample_data,label = "Observation",linewidth=3)
sns.lineplot(x='Date',y='sim',data=sample_data, label = 'Simulation',linewidth=3)
pt.xlabel("")
pt.ylabel("Streamflow(m$^3$/s)", fontsize='x-large')
pt.legend(loc='best',shadow=True, fontsize='large')
pt.xticks(fontsize=14)
pt.yticks(fontsize=14)
pt.show()