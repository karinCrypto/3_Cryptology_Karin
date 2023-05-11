from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256 as SHA


def readPEM_ECC(pemfile):
    with open(pemfile, 'r') as h:
        key = ECC.import_key(h.read())

    return key


def ecdsa_sign(msg):
    privateKey = readPEM_ECC('privkey_ecdsa.pem')    
    sha = SHA.new(msg)
    signer = DSS.new(privateKey, 'fips-186-3')
    signature = signer.sign(sha)

    return signature


def ecdsa_verify(msg, signature):
    sha = SHA.new(msg)
    publicKey = readPEM_ECC('pubkey_ecdsa.pem')
    verifier = DSS.new(publicKey, 'fips-186-3')
    try:
        verifier.verify(sha, signature)
        print('+++ The message is authentic')
    except ValueError:
        print('--- The message is not authentic')


def main():    
    msg = 'My name is samsjang'
    signature = ecdsa_sign(msg.encode('utf-8'))
    ecdsa_verify(msg.encode('utf-8'), signature)


main()

