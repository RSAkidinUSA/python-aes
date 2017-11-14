#/usr/bin/python3
# aes_expansion.py code for computing the key expansion for aes
from aes_inv import inverse
from aes_mult import modz
from aes_sbox import sub

# key expansion core for 4byte string (hex)
# round num increments each call, starting at 00000010
roundnum = 0
def core(val):
    global roundnum
    roundnum = roundnum + 1
    RCon = modz(1 << roundnum)
    val = val[2:] + val[:2]
    ret = ''
    for i in range(4):
        temp = sub(val[(i*2):(i*2)+2])
        if (i == 0):
            temp = hex(int(temp, 16) ^ RCon).upper()
            temp = temp[2:]
        temp = '0' * (2 - len(temp)) + temp
        ret = ret + temp
        
    return ret
    

# provide the user with a hex key of one of the correct lengths
def expand(key):
    try:
        test = int(key, 16)        
    except:
        print("Invalid input type. Please enter hex value.")
        return 1
    keylen = len(key) * 4
    if (keylen != 128) and (keylen != 192) and (keylen != 256):
        print("Invalid key length. Please use 128, 192, or 256 bit key.")
        return 2
    numRounds = 10 + int((keylen - 128) / 32)
    # 16 byte keys, 1 byte = 2 chars
    expKeyLen = (numRounds + 1) * 16 * 2
    
    print("Key length: %d\nNumber of rounds %d:" \
          %(keylen, numRounds))
    
    expKey = key
    global roundnum
    roundnum = 0
    # max value of j from key expansion loop
    iterMax = 4 + (numRounds - 10)
    while len(expKey) < expKeyLen:
        # 4,6,8 for 128, 192, 256 bit keys
        for i in range (iterMax):
            temp1 = expKey[len(expKey) - 8:]
            if i == 0:
                temp1 = core(temp1)
            if (i == 4) and (iterMax == 8):
                for i in range(4):
                    temp = sub(temp1[(i*2):(i*2)+2])
                    temp = '0' * (2 - len(temp)) + temp
                    temp1 = temp1[:(i*2)] + temp + temp1[(i*2)+2:]
            temp2 = expKey[len(expKey) - (8 * iterMax):]
            temp2 = temp2[:8]
            xor = hex(int(temp1, 16) ^ int(temp2, 16))[2:]
            xor = '0' * (8 - len(xor)) + xor
            expKey = expKey + xor
    print("Expanded key length: %d" % (len(expKey) / 2,))
    return expKey
    
    
def main():
    print(expand('000102030405060708090a0b0c0d0e0f'))
    print(expand('000102030405060708090a0b0c0d0e0f1011121314151617'))
    print(expand('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'))
    

if __name__=='__main__':
    main()
