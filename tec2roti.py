import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def tec2ROT(tec,timeL):
    rot = []
    i=1
    while i < len(tec):
        rot.append((tec[i]-tec[i-1])/(timeL[i].timestamp()-timeL[i-1].timestamp()))
        i+=1

    return np.array(rot)

def ROT2ROTI(rot, length):
    roti = []    
    for i in range(len(rot)-length):
        roti.append(np.std(rot[i:i+length]))
    
    return np.array(roti)

df = pd.read_csv("ISTA00TUR_20230805.txt", sep=" ", na_values=['999.99'])
df["Time"] = pd.to_datetime(df["Time"], format="%Y%m%dT%H%M%S")
tec_list = df["VTEC"].interpolate('linear').to_list()
time_list = df["Time"].to_list()


rot = tec2ROT(tec_list,time_list)
roti = ROT2ROTI(rot,10) # RINEX sampling rate was 30sec so i choosed 10 to get ROTI of every 5 min 

plt.plot(np.arange(0,len(roti),1),roti)
plt.show()
