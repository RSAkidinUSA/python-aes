#/usr/bin/python3
# aes_expansion.py code for computing the key expansion for aes
from aes_inv import inverse
from aes_mult import modz
from aes_sbox import sub

# key expansion core for 4byte string (hex)
# round num increments each call, starting at 00000010
roundNum = 0
def core(val):
    global roundNum
    RCon = modz(1 << roundNum)
    val = val[2:] + val[:2]
    ret = sub(val)
    swap = hex(int(ret[:2], 16) ^ RCon).upper()[2:]
    ret = swap + ret[2:]
    roundNum = roundNum + 1
    return ret

# Take an input key of a 128, 192, or 256 bits and return an array of round keys
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
    if not __debug__:
        print("Key length: %d\nNumber of rounds: %d" \
              %(keylen, numRounds))
    
    expKey = key
    global roundNum
    roundNum = 0
    # max value of j from key expansion loop
    iterMax = 4 + (numRounds - 10)
    while len(expKey) < expKeyLen:
        # 4,6,8 for 128, 192, 256 bit keys
        for i in range (iterMax):
            temp1 = expKey[len(expKey) - 8:]
            if i == 0:
                temp1 = core(temp1)
            if (i == 4) and (iterMax == 8):
                temp1 = sub(temp1)
            temp2 = expKey[len(expKey) - (8 * iterMax):]
            temp2 = temp2[:8]
            xor = hex(int(temp1, 16) ^ int(temp2, 16))[2:]
            xor = '0' * (8 - len(xor)) + xor
            expKey = expKey + xor
    expKey = expKey[:expKeyLen]
    # debugging info
    if not __debug__:
        print("Expanded key length: %d" % (len(expKey) / 2,))
    roundKeys = []
    if not __debug__:
        print("Keys:")
    for i in range(numRounds + 1):
        roundKeys.append(expKey[i*32:(i+1)*32])
        if not __debug__:
            print("Round %d:\t%s" % (i, roundKeys[i]))
    # end debugging info
    return roundKeys
    
    
def main():
    expand('000102030405060708090a0b0c0d0e0f')
    expand('000102030405060708090a0b0c0d0e0f1011121314151617')
    expand('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f')
    

if __name__=='__main__':
    main()
