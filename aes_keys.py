#/usr/bin/python3
# aes_expansion.py code for computing the key expansion for aes
from aes_inv import inverse
from aes_mult import modz, hex
from aes_sbox import sub

# key expansion core for 4byte string (hex)
# round num increments each call, starting at 00000010
roundNum = 0
def core(val):
    global roundNum
    RCon = modz(1 << roundNum)
    val = val[2:] + val[:2]
    ret = sub(val)
    swap = hex(int(ret[:2], 16) ^ RCon)
    ret = swap + ret[2:]
    roundNum = roundNum + 1
    return ret

# Take an input key of a 128, 192, or 256 bits and return an array of round keys
def expand(key, encrypt=True):
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
    # 16 byte keys, 1 byte = 2 chars
    expKeyLen = (numRounds + 1) * 16 * 2
    
    expKey = key
    global roundNum
    roundNum = 0
    # max value of j from key expansion loop
    iterMax = 4 + (numRounds - 10)
    while len(expKey) < expKeyLen:
        # 4,6,8 for 128, 192, 256 bit keys
        for i in range (iterMax):
            temp1 = expKey[len(expKey) - 8:]
            if i == 0:
                temp1 = core(temp1)
            if (i == 4) and (iterMax == 8):
                temp1 = sub(temp1)
            temp2 = expKey[len(expKey) - (8 * iterMax):]
            temp2 = temp2[:8]
            xor = hex(int(temp1, 16) ^ int(temp2, 16))
            xor = '0' * (8 - len(xor)) + xor
            expKey = expKey + xor                 
    expKey = expKey[:expKeyLen]
    roundKeys = []
    for i in range(numRounds + 1):
        roundKeys.append(expKey[i*32:(i+1)*32])
    if not encrypt:
        roundKeys.reverse()
    return roundKeys
    
    
def main():
    key1 = ''.join(expand('000102030405060708090A0B0C0D0E0F'))
    key1_expand = '000102030405060708090A0B0C0D0E0F'\
                  'D6AA74FDD2AF72FADAA678F1D6AB76FE'\
                  'B692CF0B643DBDF1BE9BC5006830B3FE'\
                  'B6FF744ED2C2C9BF6C590CBF0469BF41'\
                  '47F7F7BC95353E03F96C32BCFD058DFD'\
                  '3CAAA3E8A99F9DEB50F3AF57ADF622AA'\
                  '5E390F7DF7A69296A7553DC10AA31F6B'\
                  '14F9701AE35FE28C440ADF4D4EA9C026'\
                  '47438735A41C65B9E016BAF4AEBF7AD2'\
                  '549932D1F08557681093ED9CBE2C974E'\
                  '13111D7FE3944A17F307A78B4D2B30C5'
    print('Key1:\n%s\nKey1 expanded:\n%s\nequal:%s\n' % (key1,key1_expand,key1==key1_expand))
    
    key2 = ''.join(expand('1AD3EFA21CE55D9C8E53D19E2A08E200'))
    key2_expand = '1AD3EFA21CE55D9C8E53D19E2A08E200'\
                  '2B4B8C4737AED1DBB9FD004593F5E245'\
                  'CFD3E29BF87D334041803305D275D140'\
                  '56EDEB2EAE90D86EEF10EB6B3D653A2B'\
                  '136D1A09BDFDC26752ED290C6F881327'\
                  'C710D6A17AED14C628003DCA47882EED'\
                  '2321830159CC97C771CCAA0D364484E0'\
                  '787E620421B2F5C3507E5FCE663ADB2E'\
                  '78C753375975A6F4090BF93A6F312214'\
                  'A454A99FFD210F6BF42AF6519B1BD445'\
                  '3D1CC78BC03DC8E034173EB1AF0CEAF4'
    print('Key2:\n%s\nKey2 expanded:\n%s\nequal:%s\n' % (key2,key2_expand,key2==key2_expand))

    key3 = ''.join(expand('4F5A524FA0653DDD7DD02ADF6B9A6B76E4CC26374C581D7D'))
    key3_expand = '4F5A524FA0653DDD7DD02ADF6B9A6B76E4CC26374C581D7D'\
                  '24FEAD66849B90BBF94BBA6492D1D112761DF7253A45EA58'\
                  '4879C7E6CCE2575D35A9ED39A7783C2BD165CB0EEB202156'\
                  'FB84760F3766215202CFCC6BA5B7F04074D23B4E9FF21A18'\
                  '7A26DBD44D40FA864F8F36EDEA38C6AD9EEAFDE30118E7FB'\
                  'C7B2D4A88AF22E2EC57D18C32F45DE6EB1AF238DB0B7C476'\
                  '4EAEEC4FC45CC2610121DAA22E6404CC9FCB27412F7CE337'\
                  '1EBF765ADAE3B43BDBC26E99F5A66A556A6D4D144511AE23'\
                  '1C5B5034C6B8E40F1D7A8A96E8DCE0C382B1ADD7C7A003F4'[:len(key3)]
    print('Key3:\n%s\nKey3 expanded:\n%s\nequal:%s\n' % (key3,key3_expand,key3==key3_expand))
    
    
    key4 = ''.join(expand('54D1C20A0D7B90A27E8099BFEC6245ADDE4FCAB68F6C18A2C5B07B56AA1E300F'))
    key4_expand = '54D1C20A0D7B90A27E8099BFEC6245ADDE4FCAB68F6C18A2C5B07B56AA1E300F'\
                  '27D5B4A62AAE2404542EBDBBB84CF816B2668BF13D0A9353F8BAE80552A4D80A'\
                  '6CB4D3A6461AF7A212344A19AA78B20F1EDABC8723D02FD4DB6AC7D189CE1FDB'\
                  'E3746A01A56E9DA3B75AD7BA1D2265B5BA49F1529999DE8642F31957CB3D068C'\
                  'CC1B0E1E697593BDDE2F4407C30D21B2949E0C650D07D2E34FF4CBB484C9CD38'\
                  '01A6094168D39AFCB6FCDEFB75F1FF49093F1A5E0438C8BD4BCC0309CF05CE31'\
                  '4A2DCECB22FE543794028ACCE1F37585F13287C9F50A4F74BEC64C7D71C3824C'\
                  '243EE76806C0B35F92C2399373314C167EF5AE8E8BFFE1FA3539AD8744FA2FCB'[:len(key4)]
    print('Key4:\n%s\nKey4 expanded:\n%s\nequal:%s\n' % (key4,key4_expand,key4==key4_expand))
    

if __name__=='__main__':
    main()
