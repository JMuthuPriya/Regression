import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import math

Area=[594,833,842,903,996,1296,1536,1622,1696,1769,1996,2046,2196,3868]
Price=[122.1,119.85,123,125.22,128,126,148.56,141.5,141,166,163,161,198,221]

def mean(x):
    sum = 0.0
    for i in x:
         sum+=i
    return float(sum/len(x)) 


def variance(x):
    var = 0.0
    for i in x:
         var+=(i-mean(x))**2
    return var

def covariance(x,y):
    cov = []
    for i,j in zip(x,y):
        x1 = i-mean(x)
        y1 = j-mean(y)
        cov.append(x1*y1)
    covar = sum(cov)   
    return covar


def slope(x, y):
    slope = (covariance(x,y))/(variance(x))
    return slope


def Intercept(x, y):
    c = mean(y)-(slope(x,y)*mean(x))
    return c
m=slope(Area,Price)
c=Intercept(Area,Price)

print ("Regression using OLS method manually")
print "\nBuilt-up-Area\n",Area
print "\nPrice\n",Price
print "\nMean(Built-up-Area)              : ",mean(Area)
print "\nMean(Price)                      : ",mean(Price)
print "\nCovariance (Built-up-Area,Price) : ",covariance(Area,Price)
print "\nSlope, m                         : ",m
print "\nIntercept, c                     : ",c
print "\n(i)\nRegression Equation,\ny=",m,"x +",c

x=1000
price=m*x+c
print "\n(ii)\nBuilt up area price for 1000 sq.ft is ",price,"(in Lakhs)"

max_x = np.max(Area) + 100
min_x = np.min(Price) - 100
rx = np.linspace(min_x, max_x, 1000)
ry = c + m * rx 
plt.plot(rx, ry, color='#00FFFF', label='Regression Line')
plt.scatter(Area, Price, c='#FFFF00', label='Scatter Plot')
plt.xlabel('Area')
plt.ylabel('Price')
plt.legend()
plt.show()
