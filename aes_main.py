#/usr/bin/python3
# aes_main.py: code for reading in a file and calling the proper AES functions
from aes_expansion import expand
from aes_crypt import crypt
import argparse
import sys

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

done = False
# get data from std in or in file
def get_data(fin, asBytes=False):
    global done
    if done:
        return ''
    data = ''
    while len(data) < 32:
        c = fin.read(1)
        if c == '' or c == '\n':
            done = True
            return data
        data = data + c
    return data
'''
# get data from std in or in file
def get_data(iName, oName, roundKeys, encrypt):
    fin = sys.stdin
    if iName:
        fin = open(iName, 'r')     
    fout = sys.stdout
    if oName:
        fout = open(oName, 'w')

    # read data until newline or EOF
    data = ''
    done = False
    count = 1
    while (not done):
        c = fin.read(1)
        count = count + 1
        if c == '' or c == '\n':
            done = True
        else:
            data = data + c
        if done or count == 32:
            print(data)
            data = crypt(roundKeys, data, encrypt)
            print(data)
            fout.write(data)
            count = 1
            data = ''
            
    if iName:
        fin.close()
    if oName:
        fout.close()
'''

def write_data(fout, data, asBytes=False):
    if (not asBytes):
        fout.write(data)
        fout.flush()

# function to parse arguments
def parse():
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt a file'\
                                     ' with AES128, AES192, or AES256.\n'\
                                     'Run with -o flag to enable debugging',
                                     formatter_class=SmartFormatter)
    parser.add_argument('key_file',
                        type=str, nargs=1,
                        help='The file storing the 128, '\
                        '192, or 256 bit key as text')
    parser.add_argument('-f', metavar='input_file',
                        type=str, nargs=1,
                        help='R|The file storing the text to be '\
                        '(en/de)crypted.\n'\
                        'If not used, input must come from stdin.\n'\
                        'If a newline character is reached without the '\
                        '-b flag,\nthe program will treat it like an EOF')
    parser.add_argument('-o', metavar='output_file',
                        type=str, nargs=1,
                        help='R|The file to store the '\
                        '(en/de)crypted text in.\n'\
                        'If not used, output will go to stdout.')
    parser.add_argument('-d', action='store_true',
                        help='Decrypt the file instead of encrypting')
    parser.add_argument('-b', action='store_true',
                        help='R|Read and write files as bytes.\n'\
                        'If not set, read and write characters as hex values.')
    
    return parser.parse_args()

# main function
def main():
    args = parse()
    fin = sys.stdin
    fout = sys.stdout
    # test input and output files
    if (args.f):
        try:
            fin = open(''.join(args.f), 'r' + ('b' if args.b else ''))
        except:
            print("Unable to open the provided input file")
            return 2
    if (args.o):
        try:
            fout = open(''.join(args.o), 'w' + ('b' if args.b else ''))
        except:
            print("Unable to open the provided output file")
            return 3
    key = get_key(''.join(args.key_file))
    if key == 1:
        return 1
    roundKeys = expand(key)
    if (type(roundKeys) != list):
        print("Error #%d" % (roundKeys,))
    global done
    done = False
    data = get_data(fin, args.b)
    while data != '':
        data = crypt(roundKeys, data, (not args.d))
        write_data(fout, data, args.b)
        data = get_data(fin, args.b)

if __name__ == '__main__':
    main()
