from Crypto.Util.number import bytes_to_long,long_to_bytes,getPrime
import gmpy2,sympy
from Crypto.PublicKey import RSA
from binascii import a2b_hex,b2a_hex,unhexlify
import base64
from functools import reduce
# rsa_components=(n,e,int(d),p,q)
# arsa=RSA.construct(rsa_components)
# rsakey = RSA.importKey(arsa.exportKey())
# rsakey = PKCS1_OAEP.new(rsakey)
# decrypted = rsakey.decrypt(c_bytes)
# print(decrypted)
def get_ne():
    f = open('pubkey.pem', 'rb')
    ss = RSA.importKey(f.read())
    print("n=%d\ne=%d" % (ss.n, ss.e))
    f.close()

n=62078208638445817213739226854534031566665495569130972218813975279479576033261
e=9850747023606211927
p=336771668019607304680919844592337860739
q=n//p
d=gmpy2.invert(e,(p-1)*(q-1))
f=open('flag.enc','rb')
s=f.read()
#s=b'ewOCeQfkac7Qj8QGhKkuJUit7/CSxbbaIs/u66ImN0o='
b=base64.b64decode(s)
#b=b'sss'
c=bytes_to_long(b)
print(b)
m=pow(c,d,n)
#print(long_to_bytes(m))
from Crypto.Cipher import PKCS1_v1_5
rsa_components=(n,e,int(d),p,q)
# arsa=RSA.construct(rsa_components)
m=b'flags'
pp=(n,e)
pub=RSA.construct(pp)
priv=RSA.construct(rsa_components)
key=PKCS1_v1_5.new(pub)
enc=key.encrypt(m)
print(enc)
ri=PKCS1_v1_5.new(priv)
mm=ri.decrypt(b,e)
print(mm)

print(len(b))