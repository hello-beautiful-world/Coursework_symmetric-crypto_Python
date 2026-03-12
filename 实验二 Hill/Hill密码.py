from numpy import linalg

# 输入矩阵并判断是否存在逆矩阵
def inputMatrix():
    while True:
        # 输入矩阵
        for i in range(3):
            matrix[i]= list(input("").split())
        # 转换字符型为整型
        for i in range(3):
            matrix[i]=[int(e) for e in matrix[i]]
        # 判断输入的矩阵是否满足密钥的要求    
        if  judgeMatrix(matrix):
            print("请重新输入!!!")
            continue
        return matrix

# 判断输入的矩阵是否满足密钥的要求
def judgeMatrix(matrix):
    if linalg.det(matrix)==0:
        print("您输入矩阵的行列式为0，没有逆矩阵！！！")
        return True
    if linalg.det(matrix)%2==0 or linalg.det(matrix)%13==0:
        print("您输入矩阵的行列式与26不互素！！！")
        return True
    else:
        return False
    
# 对消息分组
def createMassageList(massage):
    massageList = []
    # 扩充消息序列并创建分组
    while len(massage) % 3 != 0:
        massage += " "
    for i in range(len(massage)/3):
        massageList.append(massage[i*3:i*3+3])
    return massageList

# 字母序列转化为数字
def letterToDigit(massageList,massage):
    massageDigitList = []  # 替换后的数字列表
    letterList = []  # 字母列表
    for i in range(ord("a"), ord("z") + 1):
        letterList.append(chr(i))
    for i in range(10):
        letterList.append(str(i))
    letterList.append(" ")
    # 替换字母为数字
    for massage in massageList:
        listTmp = []
        for i in range(3):
            listTmp.append(letterList.index(massage[i]))
        massageDigitList.append(listTmp)
    return massageDigitList

# 数字序列转化为字母
def digitToLetter(massageList):
    massageLetterList = []  # 还原后的字母列表
    letterList = []
    for i in range(ord("a"), ord("z") + 1):
        letterList.append(chr(i))
    for i in range(10):
        letterList.append(str(i))
    letterList.append(" ")
    # 替换数字为字母
    for massage in massageList:
        massageLetterList.append(letterList[massage % 37])
    return massageLetterList

# 加密
def encrypt(massage, matrix):
    ciphertextList = [] # 加密结果列表
    massageList = createMassageList(massage)
    massageDigitList = letterToDigit(massageList)
    # 矩阵相乘
    for massageDigit in massageDigitList:
        for i in range(len(massageDigit)):
            sum = 0
            for j in range(len(massageDigit)):
                sum += massageDigit[j] * matrix[j][i]
            ciphertextList.append(sum % 37)
    return ciphertextList

# 解密
def decrypt(massage, matrix):
    plaintextList = []  # 解密结果列表
    matrix_inverse = linalg.inv(matrix)
    massageList = createMassageList(massage)
    # 矩阵相乘
    for msg in massageList:
        for i in range(3):
            sum = 0
            for j in range(3):
                sum += msg[j] * matrix_inverse[j][i]
            plaintextList.append(sum % 37)
    # 浮点型转换为整型(采用四舍五入——round())
    plaintextList = list(map(lambda x: int(round(x)), plaintextList))
    plaintextList = digitToLetter(plaintextList)    # 数字转换为字母
    plaintext = ""
    for item in plaintextList:
        plaintext += item
    return plaintext

if __name__ == "__main__":
    while True:
        print("—————Hill密码—————")
        choice = input("加密请输入1，解密请输2：\n")
        if choice == "1":
            print("输入矩阵 ,用空格隔开：")
            matrix = inputMatrix()
            massage = input("输入明文序列：")
            massageList = createMassageList(massage, matrix)
            ciphertextList = encrypt(massage, matrix)
            print("加密结果：", ciphertextList)
        elif choice == "2":
            massageList = list(map(int, list(input("输入密文序列：").split(","))))
            print("输入矩阵：")
            matrix = inputMatrix()
            matrix_inverse = linalg.inv(matrix)
            print("逆矩阵：")
            for item in matrix_inverse:
                print(item)
            plaintext = decrypt(massageList, matrix)
            print("解密结果：", plaintext)
