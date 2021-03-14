"""
Criteria computation codes
R2: Coefficient of Determination
NSE: Nash-Sutcliffe Efficiency
NNSE: Normalized NSE
PBIAS: Percent bias

"""
import numpy as np
import matplotlib.pyplot as pt
import seaborn as sns


# Calculation fuction: the criteria for model perfomance evaluation 
class BasicStat:
    def __init__(self, obs: list, sim: list):
        self.obs = obs
        self.sim = sim

# NSE: Nash–Sutcliffe model efficiency coefficient ranges from 
    def NSE(self) -> float:                                   
        denominator = np.sum((self.obs-np.mean(self.obs))**2)
        numerator = np.sum((self.obs-self.sim)**2)
        if denominator == 0:
            print("Error: denominator is '0'.")
        else:
            NSE = 1 - (numerator/denominator)
            NSE = round(NSE,3)

# Normalized NSE: NSE=1 corresponds to NNSE=1, NSE=0 corresponds to NNSE=0.5, and NSE=-∞ corresponds to NNSE=0.
        NNSE = round(1/(2-NSE),3)        

        print("NSE: ", NSE)
        print("NNSE: ", NNSE)
        # return NSE

# Percent Bias between sim and obs
    def PBIAS(self) -> float:
        denominator = np.sum(self.obs)
        numerator = np.sum(self.sim-self.obs)
        if denominator == 0:
            print("Error: denominator is '0'.")
        else:
            pbias = 100*(numerator/denominator)
            pbias = round(pbias,3)
        print("PBIAS: ", pbias)
        # return pbias

# determination coefficient
    def R2(self) -> float:
        corr = np.corrcoef(self.obs,self.sim)
        corr = corr[0,1]
        R2 = round(corr**2,3)
        print("R2: ", R2)
        # return R2

# root mean square error
    def RMSE(self) -> float:
        RMSE = np.sqrt(((self.sim-self.obs)**2).mean())
        RMSE = round(RMSE,3)
        print("RMSE:", RMSE)
        # return RMSE
