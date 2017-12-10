#/usr/bin/python3
# aes_matrix.py: code for shifting rows

# shift rows
# data is stored in array of arrays
# first index is row, second is column
from aes_mult import multiply, modz, hex

# convert strig to matrix
def strToMat(data):
    ret = [[],[],[],[]]
    # copy values into the matrix
    for i in range(4):
        for j in range(4):
            ret[j].append(data[(4*i*2)+(j*2):(4*i*2)+(j*2)+2])
    return ret
    
# convert matrix to string
def matToStr(data):
    ret = ''
    for i in range(4):
        for j in range(4):
            ret = ret + data[j][i]
    return ret

def shift_rows(data, encrypt=True):
    # convert string to matrix
    ret = strToMat(data)
    popLoc = 0 if encrypt else 3
    insLoc = 3 if encrypt else 0
    # shift
    for i in range(1, 4):
        for j in range(i):
            temp = ret[i].pop(popLoc)
            ret[i].insert(insLoc, temp)
    # convert matrix back to string 
    ret = matToStr(ret)
    return ret

mixMat = [['0x02','0x03','0x01','0x01'],
          ['0x01','0x02','0x03','0x01'],
          ['0x01','0x01','0x02','0x03'],
          ['0x03','0x01','0x01','0x02']]

invMat = [['0x0E','0x0B','0x0D','0x09'],
          ['0x09','0x0E','0x0B','0x0D'],
          ['0x0D','0x09','0x0E','0x0B'],
          ['0x0B','0x0D','0x09','0x0E']]

# mix columns
def mix_cols(data, encrypt=True):
    multMat = mixMat if encrypt else invMat
    # convert string to matrix
    tmpMat = strToMat(data)
    ret = []
    # each column of data
    for i in range(4):
        ret.append([])
        # each row of mult matrix
        for j in range(4):
            tmp = 0
            # each item in the row
            for k in range(4):
                tmp = tmp ^ int(multiply(multMat[j][k], tmpMat[k][i]), 16)
            tmp = modz(tmp)
            # convert to string
            tmp = hex(tmp)
            ret[i].append(tmp)
    # convert matrix back to string
    tmp = []
    for i in range(4):
        tmp.append(''.join(ret[i]))
    ret = ''.join(tmp)
    return ret

def main():
    # Test shift and mix
    data_start = '00102030011121310212223203132333'.upper()
    data = data_start
    print("Data pre shift: \t%s" % (data,))
    data = shift_rows(data)
    print("Data post shift:\t%s" % (data,))
    data = mix_cols(data)
    print("Data post mix:  \t%s" % (data,))
    # Test inverse shift and mix
    print("Data pre shift: \t%s" % (data,))
    data = shift_rows(data, False)
    print("Data post shift:\t%s" % (data,))
    data = mix_cols(data, False)
    print("Data post mix:  \t%s" % (data,))
    print("Input == Output: %s" % (data == data_start,))

if __name__ == '__main__':
    main()
