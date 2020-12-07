import numpy as np
import pandas as pd
from pandas import read_csv

from sklearn.impute import SimpleImputer

# Declaring Headers
headerNames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

# Load data and map it with declared headers
myData = read_csv('venv/pima_indians_diabetes.csv', names=headerNames)

# Calculating mean
myData.mean()
# Calculating median
myData.median()
# Calculating mode
myData.mode()
# Describing The data
myData.describe()

# Print the Original dimensions
print('\nInitial Data Dimensions\n', myData.shape)

# Option 1: Drop rows with empty Values
myData = myData.dropna()
# Option 2: Replace rows with empty Values using simpleImputer
imputer = SimpleImputer(strategy='median') # replaces with most frequent median
imputer.fit(myData)
myData = pd.DataFrame(myData)

# Print New Dimensions
print('\nNew Data Dimensions\n', myData.shape)
myData.mean(skipna=False)
