#/usr/bin/python3
# aes_main.py: code for reading in a file and calling the proper AES functions
from aes_expansion import expand
import argparse

class SmartFormatter(argparse.HelpFormatter):

    def _split_lines(self, text, width):
        if text.startswith('R|'):
            return text[2:].splitlines()  
        # this is the RawTextHelpFormatter._split_lines
        return argparse.HelpFormatter._split_lines(self, text, width)

def get_key(fileName):
    try:
        keyFile = open(fileName, 'r')
    except:
        print("File %s does not exist" % (fileName,))
        return 1
    return keyFile.readline()

def parse():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt a file'\
                                     ' with AES128, AES192, or AES256.',
                                     formatter_class=SmartFormatter)
    parser.add_argument('key_file', type=str, nargs=1,
                        help='The file storing the 128, '\
                        '192, or 256 bit key as text')
    parser.add_argument('-f', metavar='input_file', type=str, nargs=1,
                        help='R|The file storing the text to be '\
                        '(en/de)crypted.\n'\
                        'If not used, input must come from stdin.')
    parser.add_argument('-o', metavar='output_file', type=str, nargs=1,
                        help='R|The file to store the '\
                        '(en/de)crypted text in.\n'\
                        'If not used, output will go to stdout.')
    return parser.parse_args()

def main():
    args = parse()
    key = get_key(''.join(args.key_file))
    if key == 1:
        return 1
    roundKeys = expand(key)
    if (type(roundKeys) != list):
        print("Error #%d" % (roundKeys,))

if __name__ == '__main__':
    main()
