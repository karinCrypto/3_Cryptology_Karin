import os
import hashlib
from hashlib import sha256 as sha
from base58check import b58encode
import ecdsa

def ripemd160(x):
    ret = hashlib.new('ripemd160')
    ret.update(x)
    return ret


def generateBitcoinAddress():
    # 개인키 생성
    privkey = os.urandom(32)
    fullkey = '80' + privkey.hex()

    a = bytes.fromhex(fullkey)
    sha_a = sha(a).digest()
    sha_b = sha(sha_a).hexdigest()    
    c = bytes.fromhex(fullkey+sha_b[:8])    

    # WIF = Wallet Import Format -> 비트코인 거래를 위한 약식 개인키
    WIF = b58encode(c)    

    # 1단계 ECDSA 공개키 획득
    signing_key = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()
    pubkey = (verifying_key.to_string()).hex()    

    # 2단계
    pubkey = '04' + pubkey

    # 3단계    
    pub_sha = sha(bytes.fromhex(pubkey)).digest()
    encPubkey = ripemd160(pub_sha).digest()

    # 4단계
    encPubkey = b'\x00' + encPubkey

    # 5단계
    chunk = sha(sha(encPubkey).digest()).digest()

    # 6단계
    checksum = chunk[:4]

    # 7단계
    hex_address = encPubkey + checksum

    # 8단계
    bitcoinAddress = b58encode(hex_address)

    # WIF와 생성된 비트코인 주소 출력
    print('+++WIF = ', WIF.decode())
    print('+++Bitcoin Address = ', bitcoinAddress.decode())    

generateBitcoinAddress()
