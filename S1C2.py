import binascii
import base64
import sys
x = raw_input("1:")
y = raw_input("2:")
if len(x) != len(y):
	print "Strings of unequal length!!"
	sys.exit(1)
else :
	pass
x = binascii.unhexlify(x)
y = binascii.unhexlify(y)
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

xored = xor_strings(x,y).encode("hex")
print xored
