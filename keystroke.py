import msvcrt, sys, time
import numpy as np
import scipy.io 
import string


matfile = 'test_mat1.mat'
junk = [[[0] for x in range(27)] for y in range(27)]
print(junk)
#reset matrix
if(0):
	scipy.io.savemat(matfile, mdict={'out': junk,'stuff': [0]}, oned_as='row')
	exit()


def convertmat(a):
	temp = [[[] for x in range(27)] for y in range(27)]
	for i in range(27):
		for j in range(27):
			if not a[i][j]:
				temp[i][j] = a[i][j].tolist()
			else:
				temp[i][j] = []
	return temp


data = scipy.io.loadmat(matfile)
pymat = convertmat(data['out'])
print(pymat)
letters = list(string.ascii_lowercase)
letters.append(' ')
string = ''
timing = [];
xl = chr(ord(msvcrt.getch()))
tl = time.time()
print(xl)
il = letters.index(xl)
string.join(str(xl))




for j in range(50):

	x = chr(ord(msvcrt.getch()))
	t = time.time()
	if(x == ';'):
		scipy.io.savemat(matfile, mdict={'out': pymat,'stuff': timing}, oned_as='row')
		break
	if(x == '.'):
		break
	i = letters.index(x)

	if(i == 26 or il == 26):
		tl = t
		xl = x
		il = i
		print(x)


	else:
		string.join(str(x))
		print(x)
		pymat[i][il].append(t-tl)
		timing.append(t-tl)
		tl = t
		xl = x
		il = i
	



print(pymat)

