import pandas as pd
import numpy as np
import xgboost as xgb

train_data_df = pd.read_csv('/home/pandit/Downloads/AnalyticsVidhya/LoanPrediction/train.csv',delimiter=',',header = None)
test_data_df = pd.read_csv('/home/pandit/Downloads/AnalyticsVidhya/LoanPrediction/test.csv',header = None ,delimiter=",")

train_data_df.columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area','Loan_Status']
test_data_df.columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']

myResults = train_data_df['Loan_Status'] 
myResults = np.array(myResults)

labels_numeric = pd.Series(train_data_df['Loan_Status'],dtype = "float")
labels_numeric = labels_numeric.astype(np.float)
#print labels_numeric
train_data_df = train_data_df.drop('Loan_Status',1)

train_data_df = np.array(train_data_df)

test_data_df = np.array(test_data_df)

xg_train = xgb.DMatrix(train_data_df,label=labels_numeric)
xg_test = xgb.DMatrix(test_data_df)

param = {}
param['objective'] = 'binary:logistic'
param['eta'] = 0.1
param['gamma'] = 1
#param['n_estimators'] = 500
param['min_child_weight'] = 4
param['max_depth'] = 5
param['subsample'] = 0.85
param['colsample_bytree'] = 0.5
param['max_delta_step'] = 20
#param['lambda'] = 10
num_round = 800

gbm = xgb.train(param,xg_train,num_round)
test_pred = gbm.predict(xg_test,output_margin = True)

f1 = open('id.csv')
id_list = []
for i in f1 :
	j = i.strip()
	id_list.append(j)

f = open('results2.csv','w')
f.write("Loan_ID,Loan_Status\n")
a = 0
for i in range(len(test_pred)) :
	j = str(test_pred[i]).strip()
	k = list(j)
	if k[0] == '-':
		j = 'N'
	else :
		j = 'Y'
	f.write(str(id_list[i])+","+str(j)+"\n")
	a += 1
		
