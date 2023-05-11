from hashlib import sha256 as sha
import codecs


# 인자 bits를 실제 16진수 값으로 리턴
def decodeBitcoinVal(bits):
    decode_hex = codecs.getdecoder('hex_codec')
    print(decode_hex(bits))
    binn = decode_hex(bits)[0]    
    ret = codecs.encode(binn[::-1], 'hex_codec')    
    return ret
    

def getTarget(bits):
    bits = decodeBitcoinVal(bits)
    bits = int(bits, 16)

    print('Bits = %x' %bits)    
    bit1 = bits >> 4*6
    base = bits & 0x00ffffff

    sft = (bit1 - 0x3)*8
    target = base << sft
    print('Target = %x' %target)
    

Bits = 'f2b9441a'
getTarget(Bits)
