import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('/home/pandit/Downloads/Udemy/Multiple_Linear_Regression/50_Startups.csv')
X=dataset.iloc[:, :-1].values
y=dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features =[3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the Dummy variable Trap
X=X[:, 1:]

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#Fitting multiple linear Regression to the Training
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the Test set results
y_pred = regressor.predict(X_test)

#Building the optimal model using Backward Elimination
import statsmodels.formula.api as sn
X=np.append(arr=X, values=np.ones((50,1)).astype(int),axis=1)
X_opt =X[:,[0,1,2,3,4,5]]
regressor_OLS =sn.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt =X[:,[0,1,3,4,5]]
regressor_OLS=sn.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3,4,5]]
regressor_OLS=sn.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3,5]]
regressor_OLS=sn.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()
X_opt=X[:,[0,3]]
regressor_OLS=sn.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()