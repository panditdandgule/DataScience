import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('/home/pandit/Downloads/Udemy/Polynomial_Regression/Position_Salaries.csv')
X=dataset.iloc[:, 1:2].values
y=dataset.iloc[:, 2].values

#Fitting the decision tree regression to the dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X, y)

#predicting a new result
y_pred = regressor.predict(6.5)

#Visualising the Linear Regression results
X_grid =np.arange(min(X),max(X),0.1)
X_grid =X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color='red')
plt.plot(X_grid,regressor.predict(X_grdi), color ='blue')
plt.title('Truth or Bluff(Random Forest Regression)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()
