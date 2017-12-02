#/usr/bin/python3
# aes_crypt.py: code for encrypting and decrypting
from aes_sbox import sub
from aes_matrix import shift_rows, mix_cols, hex

# add a round key to data and convert back to the string format we like
def add_key(key, data):
    iKey = int(key, 16)
    iData = int(data,16)
    iTmp = iKey ^ iData
    sTmp = hex(iTmp)
    sTmp = '0' * (32 - len(sTmp)) + sTmp
    return sTmp

# function to encrypt data with a given set of keys
# input is 128 bytes or less
# data is a string of hex values
def encrypt(roundKeys, data):
    if len(data) < 32:
        data = data + '0' * (32 - len(data))
    elif len(data) > 32:
        print("Too much data given...")
        return -1
    numRounds = len(roundKeys) - 1
    # Begin algorithm
    data = add_key(roundKeys[0], data)
    # debugging info
    if not __debug__:
        print("Data at round %d:\t%s" % (0, data))
    # main loop
    for i in range(1, numRounds):
        data = sub(data, True)
        data = shift_rows(data, True)
        data = mix_cols(data, True)
        data = add_key(roundKeys[i], data)
        if not __debug__:
            print("Data at round %d:\t%s" % (i, data))
    # final step
    data = sub(data, True)
    data = shift_rows(data, True)
    data = add_key(roundKeys[numRounds], data)
    if not __debug__:
        print("Data at round %d:\t%s" % (numRounds, data))
    # end debugging
    return data

# function to decrypt data with a given set of keys
# input is 128 bytes or less
# data is a string of hex values
# keys should be reversed
def decrypt(roundKeys, data):
    if len(data) < 32:
        data = data + '0' * (32 - len(data))
    elif len(data) > 32:
        print("Too much data given...")
        return -1
    numRounds = len(roundKeys) - 1
    # Begin algorithm
    data = add_key(roundKeys[0], data)
    data = shift_rows(data, False)
    data = sub(data, False)
    # debugging info
    if not __debug__:
        print("Data at round %d:\t%s" % (0, data))
    # main loop
    for i in range(1, numRounds):
        data = add_key(roundKeys[i], data)
        data = mix_cols(data, False)
        data = shift_rows(data, False)
        data = sub(data, False)
        if not __debug__:
            print("Data at round %d:\t%s" % (i, data))
    # final step
    data = add_key(roundKeys[numRounds], data)
    if not __debug__:
        print("Data at round %d:\t%s" % (numRounds, data))
    # end debugging
    return data


def main():
    print("Please don't run this as main")

if __name__ == '__main__':
    main()
