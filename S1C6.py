import base64
from itertools import cycle,izip
import operator
import binascii
def hamming_distance_bin(x,y):
    return sum(bin(i^j).count("1") for i,j in zip(x,y))
def xor_strings(xs, ys):
    return "".join(chr(xs ^ ord(ys)))
def score(c):
	count = 0
	chars = set('eEtTaAoOiInNsShHrRdDlLcC ')
	for i in chars:
		if c.count(i)>1:
			count = count + c.count(i)
	return count

def single_byte_xor_block(x):
	
	y = []
	dlis = {}
	for i in range(256):
		z = ""
		for j in x:
			z = z + xor_strings(i,j)
		y.append(z)
	for k in y:
		dlis[k] = score(k)
	bk = max(dlis.iteritems(), key=operator.itemgetter(1))[0]
	pk = y.index(bk)

	return pk
def repeating_xor_key(x,y):
	return ''.join(chr(ord(x)^ord(y)) for x,y in izip(x,cycle(y)) )

text = open("text6.txt",'r')
t = text.read()
text = base64.b64decode(t.replace("\n", ''))
dist = {}
for i in xrange(2,41):
	nlist = []
	for j in xrange(len(text)/i):
		z = float(hamming_distance_bin(bytearray(text[i*j:i*(j+1)]),bytearray(text[i*(j+1):i*(j*2)]))) / float(i)
		nlist.append(z)
	dist[i] = (float(sum(nlist)) / float(j))

keysize = min(dist.iteritems(), key=operator.itemgetter(1))[0]
parti = len(text)/keysize 

headers = []
for i in range(0,keysize):
	pst = ""
	for j in range(0,parti):
		if(i+(j*keysize) > len(text)):
			break
		pst = pst + text[i+(keysize*j):i+(j*keysize)+1]
	headers.append(pst)

finalkey = ""
for i in headers:
	g = single_byte_xor_block(i)
	finalkey = finalkey + chr(g)
	
print finalkey
print repeating_xor_key(text,finalkey)	


	
	

	




	





















	

