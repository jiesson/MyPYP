from pwn import pwnlib
from pwnlib.util.iters import mbruteforce
from string import printable
from binascii import hexlify,unhexlify
from Crypto.Cipher import AES
from hashlib import md5
from Crypto.Util.strxor import strxor

import sys
sys.path.append(r"D:\PYP\My\CTF")
import tools

def guess_key(ad):
    key='T0EyZaLRzQmNe2'+ad
    cip=unhexlify('72481dab9dd83141706925d92bdd39e4')
    tIV=unhexlify('c70000000000a32c412a3e7474e584cd')
    aes=AES.new(key,AES.MODE_CBC,tIV)
    check=aes.decrypt(cip)[6:]
    return all(x=='\n' for x in check)

def pad(message,KEYSIZE):
    p = bytes((KEYSIZE - len(message) % KEYSIZE) * chr(KEYSIZE - len(message) % KEYSIZE),encoding='utf-8')
    return message + p

def decry(key,IV,ms):
    aes=AES.new(key,AES.MODE_ECB)
    return strxor(aes.decrypt(IV),ms)

def solve():
    #key='T0EyZaLRzQmNe2'+mbruteforce(guess_key,printable,2,method='fixed')
    #key = 'T0EyZaLRzQmNe2' +tools.getstr(2)
    # print(bytes(key.encode("utf-8")))
    #key=b'T0EyZaLRzQmNe212'
    key=b'T0EyZaLRzQmNe2pd'
    h=md5(key).hexdigest()
    SECRET=unhexlify(h)[:10]
    message=b'AES CBC Mode is commonly used in data encryption. What do you know about it?'+SECRET
    msg=pad(message,16)
    msgs=[msg[ii:(ii+16)] for ii in range(0,len(msg),16)]#分割字符串
    msgs.reverse()#反向排序
    IV=unhexlify('72481dab9dd83141706925d92bdd39e4')
    for ms in msgs:
        IV=decry(key,IV,ms)
    return IV

if __name__=='__main__':
    print(solve())