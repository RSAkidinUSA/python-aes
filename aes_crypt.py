#/usr/bin/python3
# aes_crypt.py: code for encrypting and decrypting
from aes_sbox import sub

# shift rows
def shift_rows(data):
    return data

# mix columns
def mix_cols(data):
    return data

# add a round key to data and convert back to the string format we like
def add_key(key, data):
    iKey = int(key, 16)
    iData = int(data,16)
    iTmp = iKey ^ iData
    sTmp = hex(iTmp).replace('0x','').upper()
    sTmp = '0' * (32 - len(sTmp)) + sTmp
    return sTmp

# function to encrypt and decrypt using a given set of keys
# input must be 128 bites or less
# data is a string of hex values
def crypt(roundKeys, data, encrypt=True):
    if len(data) < 32:
        data = data + '0' * (32 - len(data))
    elif len(data) > 32:
        print("Too much data given...")
        return -1
    numRounds = len(roundKeys) - 1
    # Begin algorithm
    data = add_key(roundKeys[0], data)
    print("Data at round %d:\t%s" % (0, data))
    # main loop
    for i in range(1, numRounds):
        data = sub(data)
        data = shift_rows(data)
        data = mix_cols(data)
        data = add_key(roundKeys[i], data)        
        print("Data at round %d:\t%s" % (i, data))
    # final step
    data = sub(data)
    data = shift_rows(data)
    data = add_key(roundKeys[numRounds], data)
    print("Data at round %d:\t%s" % (numRounds, data))
    return data
    

def main():
    print("Please don't run this as main")

if __name__ == '__main__':
    main()