import random

alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha = list(alpha)
beta = alpha[0:26]

def rotate(l,n):
    return l[-n:] + l[:-n]


rot13 = rotate(beta, 13)
cesar = ['l', 'w', 'k', 'z', 'm', 's', 'i', 'x', 'e', 'b', 'y', 'v', 'h',
		'f', 't', 'd', 'o', 'r', 'u', 'q', 'p', 'c', 'g', 'j', 'a', 'n']

['l', 'w', 'k', 'z', 'm', 's', 'i', 'x', 'e', 'b', 'y', 'v', 'h', 'f', 't', 'd', 'o', 'r', 'u', 'q', 'p', 'c', 'g', 'j', 'a', 'n']

message = 'myhovercraftisfullofeels'

def cipher(mes, cip):
	work = list(mes)
	for i, char in enumerate(work):
		work[i] = cip[alpha.index(char)]
	mes = ''.join(work)
	return mes

def decipher(mes, cip):
	work = list(mes)
	for i, char in enumerate(work):
		work[i] = alpha[cip.index(char)]
	mes = ''.join(work)
	return mes

ciphed = cipher(message, rot13)
deciphed = decipher(ciphed, rot13)

print message
print ciphed
print deciphed
