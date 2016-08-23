import msvcrt, sys, time
import numpy as np
import scipy.io 
import string
#mat = [[[0] for x in range(27)] for y in range(27)] 
matfile = 'test_mat1.mat'
mat = scipy.io.loadmat(matfile)
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
		scipy.io.savemat(matfile, mdict={'out': mat,'stuff': timing}, oned_as='row')
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
		#mat['out'][i][il] = np.insert(mat['out'][i][il],0,t-tl)
		mat[i][il].append(t-tl)
		timing.append(t-tl)
		tl = t
		xl = x
		il = i
	
	



print(timing)

