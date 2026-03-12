letter = "abcdefghijklmnopqrstuvwxyz"
LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(pt, key):
    ct = ""
    for e in pt:
        if e not in letter:
            if e not in LETTER:
                ct += e
            else:
                ct += LETTER[(LETTER.index(e) + key) % 26]
        else:
            ct += letter[(letter.index(e) + key) % 26]
    return ct


def decrypt(ct, key):
    pt = ""
    for e in ct:
        if e not in letter:
            if e not in LETTER:
                pt += e
            else:
                pt += LETTER[(LETTER.index(e) - key) % 26]
        else:
            pt += letter[(letter.index(e) - key) % 26]
    return pt


if __name__ == "__main__":
    key = int(input("key:"))
    while True:    
        if (key < 1) or (key > 25):
            print("Invalid key!")
            key = int(input("key:"))
        else:
            break
    #加密
    with open("plaintext.txt", "r") as f:
        pt = f.read()
    ct = encrypt(pt, key)
    print(ct)
    #解密
    with open("ciphertext.txt", "w") as f:
        f.write(ct)
    pt = decrypt(ct, key)
    print(pt)
    
