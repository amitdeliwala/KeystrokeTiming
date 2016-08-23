import numpy
mat = [[0 for i in range(26)] for j in range(26)]
data=""
with open("/usr/share/dict/words") as myfile:
    data="".join(line.rstrip() for line in myfile)
def analyze(s):
	prev = None
	for x in s:
		if x.isalpha():
			if prev:
				print prev,x
				mat[ord(prev.lower()) -97][ord(x.lower()) -97] +=1
			prev=x
		else:
			prev=None
analyze(data)
numpy.savetxt("matrix.csv",numpy.matrix(mat),fmt='%d',delimiter=",")
