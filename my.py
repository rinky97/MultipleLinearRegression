# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 11:04:29 2017

@author: Rinky
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#encoding the state column into a series of dummy variables
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X= onehotencoder.fit_transform(X).toarray()

#avoiding the dummy variable trap
X= X[:, 1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

#creating a column in the beginning with all ones i.e x0 values
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int),values = X, axis=1) 

#Applying backward elimination
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog= y,exog= X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog= y,exog= X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog= y,exog= X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog= y,exog= X_opt).fit()
regressor_OLS.summary()

#this is an optional elimination as the p value of the last column was just sllghtly greater than the significance level
X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog= y,exog= X_opt).fit()
regressor_OLS.summary()
