#/usr/bin/python3
# bin_ascii_conv.py: code for converting binary to ascii and back again
from aes_mult import hex

def ascii_to_bin(data):
    ba = []
    for i in range(int(len(data)/2)):
        temp = data[2*i:(2*i)+2]
        ba.append(int(temp, 16))
    return bytearray(ba)

def bin_to_ascii(ba):
    ba = bytearray(ba)
    data = ''
    for i in range(len(ba)):
        temp = hex(ba[i])
        data = data + temp
    return data

def main():
    #ascii to bin
    fin = open("test.txt", "r")
    fout = open("testb.txt", "wb")
    data = fin.readline()
    data = ascii_to_bin(data)
    fout.write(data)
    fout.flush()
    fin.close()
    fout.close()
    #back
    fin = open("testb.txt", "rb")
    fout = open("testh.txt", "w")
    data = fin.readline()
    data = bin_to_ascii(data)
    fout.write(data)
    fout.flush()
    fin.close()
    fout.close()


if __name__ == '__main__':
    main()
