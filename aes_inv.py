#/usr/bin/python3
# aes_inv.py code for the inverse for aes
from aes_mult import aes_b, modz, multiply, hex

#takes ints, returns tuple of quotient and remainder
def divide(x, y):
    r = y
    q = '0' * (len(bin(y)) - len(bin(x)) + 1)
    for i in range(len(q)):
        shiftx = x << (len(q) - 1 - i)
        if (len(bin(shiftx)) == len(bin(r))):
            q = q[:i] + '1' + q[i+1:]
            r = r ^ shiftx

    return (int(q, 2), r)

# extended euclidean, takes a list of quotients and returns the inverse
def EEA(q_list):
    k_list = [0b0, 0b1]
    for i in range(len(q_list)):
        k_list.append(k_list[i] ^ int(multiply(hex(k_list[i+1]), hex(q_list[i])), 16))
    return k_list[len(k_list) - 1]

#takes one hex number as a string, returns hex inverse mod b
def inverse(x, b=aes_b):
    ix = int(x,16)
    if (ix > b):
        ix = modz(ix, b)
    bx = bin(ix)
    q_list = []
    tempdiv = b
    tempq, tempr = divide(ix, tempdiv)
    while tempr != 0:
        q_list.append(tempq)
        tempdiv = ix
        ix = tempr
        tempq, tempr = divide(ix, tempdiv)

    ret = hex(EEA(q_list))
    return ret
        

def main():
    x = '0x0F'
    ret = inverse(x)
    print(ret)
    

if __name__=='__main__':
    main()
