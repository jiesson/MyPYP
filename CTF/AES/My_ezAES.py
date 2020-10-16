from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import binascii,hashlib
import random
import itertools

def getstr():
    re=[]
    list="1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()\"\'\\_+[]{}\|;:,.<>/?`~"
    for i in itertools.product(list,repeat=2):#获取笛卡尔积，得到list中的2个字符的所以组合
        ss=''.join(i)
        re.append(ss)
    #print(re)
    return re

def gs(ad):
    key = 'T0EyZaLRzQmNe2' + ad#猜解密钥
    cip = binascii.unhexlify('72481dab9dd83141706925d92bdd39e4')#最后一组密文
    tIV = binascii.unhexlify('c70000000000a32c412a3e7474e584cd')#倒数第二组密文，仅有后20位，随机添加12位前缀
    aes = AES.new(key.encode("utf-8"), AES.MODE_CBC, tIV)#以倒数第二组密文作为向量，解密最后一组密文
    check = aes.decrypt(cip)[6:]#获取最后一组密文解密后的明文，只取最后10位
    #print(binascii.hexlify(check))
    if binascii.hexlify(check)==b'0a0a0a0a0a0a0a0a0a0a':#最后10位均为\n，说明解密密钥正确
        print(key)
        return key
    return 0

def kkk():
    for k in getstr():
        # print(k)
        re = gs(k)
        # print(re)
        if re:
            print("successful")
            return re

def pad(message,KEYSIZE):#补齐位数
    p = bytes((KEYSIZE - len(message) % KEYSIZE) * chr(KEYSIZE - len(message) % KEYSIZE),encoding='utf-8')
    return message + p

def solve():
    key=kkk()#获取key
    h=hashlib.md5(key.encode('utf-8')).hexdigest()#key的hash的16进制
    secret=binascii.unhexlify(h)[:10]#仅取unhex的后10位
    message = b'AES CBC Mode is commonly used in data encryption. What do you know about it?'+secret
    msg=pad(message,16)#补齐
    msgs=[msg[i:(i+16)] for i in range(0,len(msg),16)]#分段
    msgs.reverse()#反向排序
    iv=binascii.unhexlify("72481dab9dd83141706925d92bdd39e4")#最后一组密文
    for m in msgs:#反向遍历每组明文
        #iv=decry(key.encode('utf-8'),iv,m)
        aes=AES.new(key.encode('utf-8'),AES.MODE_ECB)#通过ECB一组一组解密
        x=aes.decrypt(iv)#解密最后一组密文
        re=strxor(x,m)#解密后的最后一组密文与最后一组明文异或，得到倒数第二组密文
        iv=re
    print(iv)

solve()
#kkk()