import sympy

def rsa_key():
    list_primes = list(sympy.primerange(0, 200))
    print(list_primes)
    #Select two price number p and q
    # p = 7
    # q = 19
    p = 67
    q = 137
    #Calculate Product q * q
    n = p * q
    #Calculate totient (p-1)(q-1)
    t = (p - 1) * (q - 1)
    #Select public key p_key
    # encode_key = -1
    # for num in list_primes:
    #     if((t % num != 0)and(num<t)):
    #         encode_key = num
    #         break
    #     else:
    #         continue
    encode_key = 13
    print("Pulic key: {}".format(encode_key))
    #Select private key
    decode_key = -1
    for i in range(10000):
        if ((i*t+1)%encode_key==0):
            decode_key = (i*t+1)/encode_key
            break
    print("Private key: {}".format(decode_key))
    print("t: {}".format(t))
    return encode_key, int(decode_key), n

if __name__ == '__main__':
    rsa_key()
