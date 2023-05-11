from hashlib import sha256 as sha
import codecs


# 인자 bits를 실제 16진수 값으로 리턴
def decodeBitcoinVal(bits):
    decode_hex = codecs.getdecoder('hex_codec')    
    binn = decode_hex(bits)[0]    
    ret = codecs.encode(binn[::-1], 'hex_codec')    
    return ret

def getTarget(bits):
    bits = decodeBitcoinVal(bits)
    bits = int(bits, 16)
    bit1 = bits >> 4*6
    base = bits & 0x00ffffff

    sft = (bit1 - 0x3)*8
    target = base << sft

    return target


# 아래 에는 2011년 5월에 생성된 비트코인 125,552번째 블록에 대한 작업증명이
# 성공했음을 검증하는 코드임

def validatePoW(header):
    block_version = header[0]
    hashPrevBlock = header[1]
    hashMerkleRoot = header[2]
    Time = header[3]
    Bits = header[4]
    nonce = header[5]

    # 블록 헤더의 모든 값을 더하고 이를 바이트 객체로 변경
    decode_hex = codecs.getdecoder('hex_codec')
    header_hex = block_version + hashPrevBlock + hashMerkleRoot + Time + Bits + nonce
    header_bin = decode_hex(header_hex)[0]

    # 실제 비트코인에서는 블록 헤더의 SHA256 해시에 대한 SHA256해시를 이용해서 작업증명을 함
    hash = sha(header_bin).digest()
    hash = sha(hash).digest()
    PoW = codecs.encode(hash[::-1], 'hex_codec')

    # 헤더의 Bits 값을 이용해 실제 target 값 추출
    target = getTarget(Bits)
    target = str(hex(target))
    target = '0'*(66-len(target)) + target[2:]

    print('target\t=', target)
    print('PoW\t=', PoW.decode())  
    
    # 작업 증명이 성공한 건지 체크
    if int(PoW, 16) <= int(target, 16):
        print('+++ Accept this Block')
    else:
        print('--- Reject this Block')



block_version = '01000000'
hashPrevBlock = \
        '81cd02ab7e569e8bcd9317e2fe99f2de44d49ab2b8851ba4a308000000000000'
hashMerkleRoot = \
        'e320b6c2fffc8d750423db8b1eb942ae710e951ed797f7affc8892b0f1fc122b'
Time = 'c7f5d74d'
Bits = 'f2b9441a'
nonce = '42a14695'
header = [block_version, hashPrevBlock, hashMerkleRoot, Time, Bits, nonce]
validatePoW(header)
