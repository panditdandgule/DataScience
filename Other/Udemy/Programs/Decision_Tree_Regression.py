import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('/home/pandit/Downloads/Udemy/Polynomial_Regression/Position_Salaries.csv')
X=dataset.iloc[:, 1:2].values
y=dataset.iloc[:, 2].values

#Fitting the decision tree regression to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state=0)
regressor.fit(X, y)

#predicting a new result
y_pred = regressor.predict(6.5)

#Visualising the Linear Regression results
plt.scatter(X, y, color='red')
plt.plot(X,regressor.predict(X), color ='blue')
plt.title('Truth or Bluff(Decision Tree Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
