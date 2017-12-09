import binascii
import string
import operator
x = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
d = dict.fromkeys(string.letters,0)
y = []
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))
def score(c):
	count = 0
	chars = set('eEtTaAoOiInNsShHrRdDlLcC ')
	for i in chars:
		if c.count(i)>1:
			count = count + c.count(i)
	return count
scorelist = {}
for i in d.keys():
	z = ""
	for j in x:
		z = z + xor_strings(i,j)
	y.append(z)
	scorelist[z] = score(z)

print max(scorelist.iteritems(), key=operator.itemgetter(1))[0]






	
