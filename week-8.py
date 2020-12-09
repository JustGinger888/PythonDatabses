import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from matplotlib import pyplot
from pandas import set_option
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Declaring Headers
headerNames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
headerCount = [32,43,56,6,75,12,43,41,54]
# Load data and map it with declared headers
myData = read_csv('venv/pima_indians_diabetes.csv', names=headerNames)
print(myData.shape)

# Printing first five and last five entries
print(myData.head(5))
print("\n------------\n")
print(myData.tail(5))

# Check headers corresponding datatypes 
print(myData.dtypes)

# Check if data is bias toward a category
countClass = myData.groupby('class').size()
print(countClass)

####################################################################################

# Creating a bar graph from data
plt_fig_bar = pyplot.figure()
plt_ax_bar = plt_fig_bar.add_axes([0,0,1,1])
plt_ax_bar.bar(headerNames,headerCount)
pyplot.show()

# Creating a bar graph from data
plt_fig_pie = pyplot.figure()
plt_ax_pie = plt_fig_pie.add_axes([0,0,1,1])
plt_ax_pie.pie(headerCount, labels = headerNames,autopct='%1.2f%%')
pyplot.show()

# Creating a box graph from data
myData.plot(kind='box', subplots= True, layout = (2,6), sharex = False)
pyplot.show()

# Creating a Density graph from data
myData.plot(kind='density', subplots= True, layout = (3,3), sharex = False)
pyplot.show()

# Creating a Histogram from data
myData.hist()
pyplot.show()

####################################################################################

# Creating a correlation matrix 
dataCorr = myData.corr()
corr_fig = pyplot.figure()
axises = corr_fig.add_subplot(111)
axcorr = axises.matshow(dataCorr, vmin=-1, vmax=1)
corr_fig.colorbar(axcorr)
ticks = np.arange(0,9,1)

axises.set_xticks(ticks)
axises.set_yticks(ticks)
axises.set_xticklabels(headerNames)
axises.set_yticklabels(headerNames)
pyplot.show()

####################################################################################

# Generate Random data
np.random.seed(0)
x=np.random.rand(100,1)
y=3+5*x

# Init, Fit, Predictt
lrRegress = LinearRegression()
lrRegress.fit(x,y)
yPred = lrRegress.predict(x)

# Evaluate
mae = mean_absolute_error(y,yPred)
mse = mean_squared_error(y,yPred)
rmse = np.sqrt(mse)
r2 = r2_score(y, yPred)

# Print
print(lrRegress.coef_)
print(lrRegress.intercept_)
print(mae)
print(mse)
print(rmse)
print(r2)

# Plot, Predict, Display
plt.scatter(x,y,s=10)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, yPred, color='r')
plt.show()
predMyValue = lrRegress.predict([[0.5]])
print(predMyValue)