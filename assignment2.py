# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 19:37:29 2023

@author: godwi
"""


import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm
import seaborn as sns
import scipy.stats as stats


def reading_f(fname,Countries,Years):
    g0=pd.read_csv(fname,skiprows=4)
    g0.drop(columns=["Country Code"],axis=1,inplace=True)
    g0.set_index(["Country Name"],inplace=True)
    g1=g0.iloc[Countries,Years]
    g2=g1.T
   
    return g1,g2

def heat_map(fname,Countries,Indicators):
    g0=pd.read_csv(fname,skiprows=4)
    g0.drop(columns=["Country Code","Indicator Code"],axis=1,inplace=True)
    g0.set_index(["Country Name","Indicator Name"],inplace=True)
    g1=g0.loc[Countries].fillna(0).T
    g=g1.loc[['2013','2014','2015','2016','2017','2018','2019'],Indicators]
    plt.figure(figsize=(10,5))
    sns.heatmap(g.corr(),vmin=-1,annot=True,cmap='BrBG')
    return

Countries=[109,35,40,119,180,202,116,77,55,20,81,251]
Years=[55,56,57,58,59,60,61]
co2_gj1,co2_gj2=reading_f("C:/Users/godwi/Downloads/co2/API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5358347.csv", Countries, Years)
methane_gj1,methane_gj2=reading_f("C:/Users/godwi/Downloads/methane/API_EN.ATM.METH.KT.CE_DS2_en_csv_v2_5362908.csv", Countries, Years)
urbanpop_gj1,urbanpop_gj2=reading_f("C:/Users\godwi\Downloads\API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5359159\API_SP.URB.TOTL.IN.ZS_DS2_en_csv_v2_5359159.csv", Countries, Years)
ruralpop_gj1,ruralpop_gj2=reading_f("C:/Users/godwi/Downloads/rural/API_SP.RUR.TOTL.ZS_DS2_en_csv_v2_5359276.csv", Countries, Years)

co2_gj1.plot(kind="bar")
plt.title("CO2 emission by various Countries",fontweight='bold')
plt.xlabel('Countries', fontweight='bold')
plt.ylabel('% of co2 emmission',fontweight='bold')

urbanpop_gj1.plot(kind="bar")
plt.title(" urban population ",fontweight='bold')
plt.xlabel('Countries', fontweight='bold')
plt.ylabel(' % of urban population',fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.5,1))

methane_gj2.plot(kind="line")
plt.title("Methane emission  ",fontweight='bold')
plt.xlabel('Years', fontweight='bold')
plt.ylabel('% of methane emission',fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.5,1))




ruralpop_gj1.plot(kind="bar")
plt.title("rural population",fontweight='bold')
plt.xlabel('Countries',fontweight='bold')
plt.ylabel('% of total population',fontweight='bold')
plt.legend(loc='upper right', bbox_to_anchor=(1.5,1))



print("Skew:", stats.skew(co2_gj1["2019"]))
print("Kurtosis", stats.kurtosis(co2_gj1["2019"]))

Indicators=["Urban population","CO2 emissions (kt)","Methane emissions (kt of CO2 equivalent)","Rural population living in areas where elevation is below 5 meters (% of total population)"]
heatmap=heat_map("C:/Users/godwi/Downloads/API_19_DS2_en_csv_v2_5361599/API_19_DS2_en_csv_v2_5361599.csv","Japan",Indicators)
heatmap=heat_map("C:/Users/godwi/Downloads/API_19_DS2_en_csv_v2_5361599/API_19_DS2_en_csv_v2_5361599.csv","India",Indicators)
