from binascii import hexlify
from itertools import izip, cycle
s = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
key = 'ICE'
def repating_xor_key(x,y):
	return ''.join(chr(ord(x)^ord(y)) for x,y in izip(x,cycle(y)) )
print hexlify(repating_xor_key(s,key))
	


