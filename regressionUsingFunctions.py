import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Area = np.array([594,833,842,903,996,1296,1536,1622,1696,1769,1996,2046,2196,3868]).reshape((-1,1))
Price = np.array([122.1,119.85,123,125.22,128,126,148.56,141.5,141,166,163,161,198,221])

model = LinearRegression().fit(Area,Price)

print ("Regression using OLS method using Linear Regression Function")

print "\nSlope, m      : ",model.coef_
print "\nIntercept, c  : ",model.intercept_
print "\n(i)\nRegression Equation,\ny=",model.coef_,"x +",model.intercept_

newArea = np.array([1000]).reshape((-1, 1))
newY = model.predict(newArea)
print "\n(ii)\nBuilt up area price for 1000 sq.ft is ", newY ,"(in lakhs)"


max_x = np.max(Area) + 100
min_x = np.min(Price) - 100
rx = np.linspace(min_x, max_x, 1000)
ry = model.intercept_ + model.coef_ * rx 
plt.plot(rx, ry, color='#00FFFF', label='Regression Line')
plt.scatter(Area, Price, c='#FFFF00', label='Scatter Plot')
plt.xlabel('Area')
plt.ylabel('Price')
plt.legend()
plt.show()
