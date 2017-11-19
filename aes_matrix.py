#/usr/bin/python3
# aes_matrix.py: code for shifting rows

# shift rows
# data is stored in array of arrays
# first index is row, second is column
def shift_rows(data, encrypt=True):
    ret = [[],[],[],[]]
    # copy values into the matrix
    for i in range(4):
        for j in range(4):
            ret[j].append(data[(4*i*2)+(j*2):(4*i*2)+(j*2)+2])
    # shift
    for i in range(1, 4):
        for j in range(i):
            if (encrypt):
                temp = ret[i].pop(0)
                ret[i].append(temp)
            else:
                temp = ret[i].pop(3)
                ret[i].insert(0, temp)
    return ret

# mix columns
def mix_cols(data, encrypt=True):

    # convert matrix back to string
    ret = ''
    for i in range(4):
        for j in range(4):
            ret = ret + data[j][i]
    return ret

def main():
    # Test shift and mix
    data_start = '00102030011121310212223203132333'.upper()
    data = data_start
    print("Data pre shift:\t%s" % (data,))
    data = shift_rows(data)
    print("Matrix: post shift:")
    for i in range(len(data)):
        print(data[i])
    data = mix_cols(data)
    print("Data post mix:\t%s" % (data,))
    # Test inverse shift and mix
    print("Data pre shift:\t%s" % (data,))
    data = shift_rows(data, False)
    print("Matrix: post shift:")
    for i in range(len(data)):
        print(data[i])
    data = mix_cols(data, False)
    print("Data post mix:\t%s" % (data,))
    print("Input == Output: %s" % (data == data_start,))

if __name__ == '__main__':
    main()
