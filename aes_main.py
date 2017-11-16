#/usr/bin/python3
# aes_main.py: code for reading in a file and calling the proper AES functions
from aes_expansion import expand
import argparse

def get_key(fileName):
    return '000102030405060708090a0b0c0d0e0f'

def parse():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt a file'\
                                     ' with AES128, AES192, or AES256.')
    parser.add_argument('key', metavar='key', type=str, nargs=1,
                        help='The file storing the 128, '\
                        '192, or 256 bit key as text')
    parser.add_argument('-f', metavar='input', type=str, nargs=1,
                        help='The file storing the text to be '\
                        '(en/de)crypted')
    args = parser.parse_args()

def main():
    #arg parse
    parse()
    key = get_key('file.txt')
    roundKeys = expand(key)
    if (type(roundKeys) != list):
        print("Error #%d" % (roundKeys,))

if __name__ == '__main__':
    main()
