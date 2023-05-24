from Crypto.Cipher import ARC4
from Crypto.Hash import SHA256 as SHA

class myARC4():
	def __init__(self, keytext):		
		self.key = keytext.encode()
		

	def enc(self, plaintext):
		arc4 = ARC4.new(self.key)		
		encmsg = arc4.encrypt(plaintext.encode())
		return encmsg
		
		
	def dec(self, ciphertext):
		arc4 = ARC4.new(self.key)
		decmsg = arc4.decrypt(ciphertext)
		return decmsg


def main():
	keytext = 'samsjang'	
	msg = 'python35'
	#msg = 'I love python'
	
	myCipher = myARC4(keytext)	
	ciphered = myCipher.enc(msg)
	deciphered = myCipher.dec(ciphered)	
	print('ORIGINAL:\t%s' %msg)
	print('CIPHERED:\t%s' %ciphered)
	print('DECIPHERED:\t%s' %deciphered)


if __name__ == '__main__':
	main()
