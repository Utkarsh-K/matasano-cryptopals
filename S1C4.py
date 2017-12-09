import binascii
import string
import operator
def xor_strings(xs, ys):
    return "".join(chr(xs ^ ord(ys)))
def score(c):
	count = 0
	chars = set('eEtTaAoOiInNsShHrRdDlLcC ')
	for i in chars:
		if c.count(i)>1:
			count = count + c.count(i)
	return count
scorelist = {}
def single_byte_xor(x):
	strings = x.decode("hex")
	y = []
	for i in range(256):
		z = ""
		for j in strings:
			z = z + xor_strings(i,j)
		y.append(z)
	return y
# Need to have saved the file challenge4.txt in the working directory !
scorelist = {}
c4 = open("challenge4.txt",'r')
for line in c4.readlines():
	line = line.strip()
	p = single_byte_xor(line)
	for k in p:
		scorelist[k] = score(k)
c4.close()

print max(scorelist.iteritems(), key=operator.itemgetter(1))[0]







	
