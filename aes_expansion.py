#/usr/bin/python3
# aes_expansion.py code for computing the key expansion for aes
from aes_inv import inverse

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
    expKeyLen = (numRounds + 1) * 16
    print("Key length: %d\nNumber of rounds %d:\nExpanded key length: %d" \
          %(keylen, numRounds, expKeyLen))
    
def main():
    print("Please don't run this as main")
    

if __name__=='__main__':
    main()
