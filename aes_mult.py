#/usr/bin/python3
# aes_mult.py code for the multiplication for aes
aes_b = 0b100011011

def hex(a):
    ret = ("%x" % a).upper()
    if len(ret) % 2:
        ret = '0' + ret
    return ret

# takes an integer base and x and does modz
def modz(x, b=aes_b):
    while len(bin(x)) >= len(bin(b)):
        x = x ^ (b << (len(bin(x)) - len(bin(b))))
    return x

# takes two hex numbers as strings, returns hex mult mod b
def multiply(x, y, b=aes_b):
    ix = int(x,16)
    by = bin(int(y,16))
    len_b = len(by)-1
    ret = 0
    # multiply
    for i in range(len_b, 1, -1):
        if by[i] == '1':
            ret = ret ^ (ix << len_b - i)

    # mod b
    ret = modz(ret, b)
    ret = hex(ret)
    return ret

def main():
    x = '0x3B'
    y = '0x16'
    ret = multiply(x, y)  
    print(ret)
    

if __name__=='__main__':
    main()
