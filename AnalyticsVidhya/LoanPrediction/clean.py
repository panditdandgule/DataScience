#f = open('train.csv')
f1 = open('/home/pandit/Downloads/AnalyticsVidhya/LoanPrediction/train.csv')
f2 = open('/home/pandit/Downloads/AnalyticsVidhya/LoanPrediction/train1.csv','w')

for i in f1 :
	j = i.strip().split(',')
	
	if j[0] == "Male" :
		j[0] = '1'
	else :
		j[0] = '0'

	if j[1] == 'Yes' :
		j[1] = '1'
	else :
		j[1] = '0'

	j[2] = j[2].replace('+','')#.replace('','0')

	if j[3] == 'Graduate' :
		j[3] = '1'
	else :
		j[3] = '0'	 

	if j[4] == 'Yes' :
		j[4] = '1'
	else :
		j[4] = '0'
	"""	
	j[5] = j[5].replace('','0')
	j[6] = j[6].replace('','0')
	j[7] = j[7].replace('','0')
	j[8] = j[8].replace('','0')
	j[9] = j[9].replace('','0')
	"""
	if j[10] == 'Urban' :	
		j[10] = '1'	
	elif j[10] == 'Semiurban' :	
		j[10] = '2'
	else :
		j[10] = '0'

	if j[11] == 'Y' :
		j[11] = '1'
	else :
		j[11] = '0'

	k = ','.join(j)
	f2.write(k+'\n')