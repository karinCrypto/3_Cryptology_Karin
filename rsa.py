from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

def rsa_enc(msg):
    # 개인키 생성
    private_key = RSA.generate(1024)
    with open('privatekey.pem', 'wb+') as f:
        f.write(private_key.exportKey('PEM'))

    public_key = private_key.publickey()
    with open('publickey.pem', 'wb+') as f:
        f.write(public_key.exportKey('PEM'))
    cipher = PKCS1_OAEP.new(public_key)
    encdata = cipher.encrypt(msg)
    print (encdata)

    cipher = PKCS1_OAEP.new(private_key)
    encdata = cipher.decrypt(encdata)
    print (msg)

   	
def main():
    #createPEM()
    msg = 'karin loves python'
    rsa_enc(msg.encode('utf-8'))
   
main()
