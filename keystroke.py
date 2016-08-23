import msvcrt, sys, time
import numpy as np
import scipy.io 

mat = [[[0] for x in range(7)] for y in range(7)] 
matfile = 'test_mat.mat'

letters = ['a','b','c','d','e','f',' '];
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
	i = letters.index(x)

	if(i == 7 or il == 7):
		tl = t
		xl = x
		il = i
		print(x)
	else:
		string.join(str(x))
		print(x)
		mat[i][il].append(t-tl)
		timing.append(t-tl)
		tl = t
		xl = x
		il = i

	
	



print(timing)

scipy.io.savemat(matfile, mdict={'out': mat,'stuff': timing}, oned_as='row')
