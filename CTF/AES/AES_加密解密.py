from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import base64#base64.b64decode
from Crypto.Util.strxor import strxor#异或

#若text不是16位的倍数，则用空格补足
def add_to_16(text):
    #text=""
    if len(text.encode('utf-8'))%16:
        add=16-(len(text.encode('utf-8'))%16)
    else:
        add=0
    text=text+('\0'*add)
    return text.encode('utf-8')

def cbc_en(text,key,iv):
    #text=""
    key=key.encode('utf-8')
    iv=iv.encode('utf-8')
    text=add_to_16(text)
    cryptos=AES.new(key,AES.MODE_CBC,iv)
    cipher_text=cryptos.encrypt(text)
    #因为AES加密后的字符串不一定是ascii字符集的，因此最好转换位16进制字符串输出
    cipher_text_hex=b2a_hex(cipher_text)
    return cipher_text_hex

def cbc_de(text,key,iv):
    key=key.encode('utf-8')
    iv=iv.encode('utf-8')
    cryptos=AES.new(key,AES.MODE_CBC,iv)
    plain_text_bytes=cryptos.decrypt(a2b_hex(text))
    plain_text=bytes.decode(plain_text_bytes)
    return plain_text

def ecb_en(text,key):
    #text=''
    key=key.encode('utf-8')
    text=add_to_16(text)
    cryptos=AES.new(key,AES.MODE_ECB)
    cipher_text=cryptos.encrypt(text)
    cipher_text_hex=b2a_hex(cipher_text)
    return cipher_text_hex

def ecb_de(text,key):
    key=key.encode('utf-8')
    cryptos=AES.new(key,AES.MODE_ECB)
    plain_text_bytes=cryptos.decrypt(a2b_hex(text))
    plain_text=bytes.decode(plain_text_bytes)
    return plain_text

b=base64.b64decode("4KeC/Oj1McI4TDIM2c9Y6ahahc6uhpPbpSgPWktXFLM=")
b=b2a_hex(b)
print(ecb_de(b,'Welcome_To_GACTF'))
