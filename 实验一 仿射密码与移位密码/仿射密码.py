letter = "abcdefghijklmnopqrstuvwxyz"
LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(pt, key_1, key_2):
    ct = ""
    for e in pt:
        if e not in letter:
            if e not in LETTER:
                ct += e
            else:
                ct += LETTER[(LETTER.index(e)*key_1 + key_2) % 26]
        else:
            ct += letter[(letter.index(e)*key_1+key_2) % 26]
    return ct


def decrypt(ct, key_1, key_2):
    inverseElementKey_1,m,n= ext_gcd(key_1,26)
    pt = ""
    for e in ct:
        if e not in letter:
            if e not in LETTER:
                pt += e
            else:
                pt += LETTER[((LETTER.index(e) - key_2)*inverseElementKey_1) % 26]
        else:
            pt += letter[((letter.index(e) - key_2)*inverseElementKey_1)% 26]
    return pt
def judgeKey_1(key_1):
    if (key_1 % 2 ==0 )or (key_1 % 13==0 ):
        return True
    
def ext_gcd(a,b):
    if b==0:
        return 1,0,a
    else:
        x,y,gcd=ext_gcd(b,a%b)
        x,y=y,(x-(a//b)*y)
        return x,y,gcd

if __name__ == "__main__":
    key_1 = int(input("key_1:"))
    key_2 = int(input("key_2:"))
    while True:    
        if (key_1 < 1) or (key_1 > 25) or judgeKey_1(key_1) :
            print("Invalid key_1!")
            key_1 = int(input("key_1:"))
        else:
            if (key_2 < 1) or (key_2> 25):
                print("Invalid key_2!")
                key_2 = int(input("key_2:"))
            else:
                break
        
        
    #加密
    with open("plaintext.txt", "r") as f:
        pt = f.read()
    ct = encrypt(pt, key_1, key_2)
    print(ct)
    #解密
    with open("ciphertext.txt", "w") as f:
        f.write(ct)
    pt = decrypt(ct, key_1, key_2)
    print(pt)
    
