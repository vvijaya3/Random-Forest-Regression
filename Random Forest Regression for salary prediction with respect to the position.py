#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Random Forest Regression

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import the dataset

datasets = pd.read_csv('Position_Salaries.csv')
X = datasets.iloc[:, 1:2].values
Y = datasets.iloc[:, 2].values

# Fit the Regression model to the dataset

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 300, random_state = 0)
regressor.fit(X,Y)

# Prediction of new result with the Random Forest Regression

Y_Pred = regressor.predict(5.5)

# Visualize the Random Forest Regression results in higher resolution and smoother curve
X_Grid = np.arange(min(X), max(X), 0.01)
X_Grid = X_Grid.reshape((len(X_Grid), 1))
plt.scatter(X,Y, color = 'red')
plt.plot(X_Grid, regressor.predict(X_Grid), color = 'yellow')
plt.title('Random Forest Regression Results')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# In[2]:





# In[ ]:




