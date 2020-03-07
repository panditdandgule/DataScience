#f = open('train.csv')
f1 = open('test1.csv')
f2 = open('test2.csv','w')

for i in f1 :
	j = i.strip().split(',')
	for i in range(len(j)) :
		if j[i] == '' :
			j[i] = '0'

	k = ','.join(j)
	f2.write(k+'\n')
			