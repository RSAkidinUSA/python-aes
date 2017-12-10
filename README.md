# python-aes
A python implementation of AES

Developed by Ryan Burrow for VT MATH4175, Cryptography 1.

This program runs on python3. It may work with python2, but I haven't tested it.

The initial modules I created for this implementation used string manipulation.  
I am too stuborn to go back and change them to be more efficient and easier.  
I have many regrets.  
I may come back and change this at a later time.  

```
usage: python3 [-O] aes_main.py [-h] [-f input_file] [-o output_file] [-d] [-b] [-c]
                    key_file

Encrypt or Decrypt a file with AES128, AES192, or AES256. Run with -O flag to
enable debugging

positional arguments:
  key_file        The file storing the 128, 192, or 256 bit key as text

optional arguments:
  -h, --help      show this help message and exit
  -f input_file   The file storing the text to be (en/de)crypted.
                  If not used, input must come from stdin.
                  If a newline character is reached without the -b flag,
                  the program will treat it like an EOF
  -o output_file  The file to store the (en/de)crypted text in.
                  If not used, output will go to stdout.
  -d              Decrypt the file instead of encrypting.
  -b              Read and write files as bytes. (Not yet implemented).
                  If not set, read and write characters as hex values.
  -c              CBC mode. IV is set to zero (this may be changed
                  in the future).
                  If not used, ECB mode will be used.
```

testFiles.sh is used to verify the code works as expected.  
It expects a directory containing 4 files the following naming convention:  
1. \*plaintext\*
2. \*cipher\*-cbc\*
3. \*cipher\*-ecb\*
4. \*key\*