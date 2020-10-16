#在线分解大素数：http://www.factordb.com/index.php；http://www.atool.org/quality_factor.php

import gmpy2
from  Crypto.Util.number import long_to_bytes
import random

#已知p、q、e求d
def get_d(p,q,e):
    n=(p-1)*(q-1)
    d=gmpy2.invert(e,n)
    return d

#print(get_d(38456719616722997,44106885765559411,65537))

#已知n较小，e求d，直接分解n

#已知n，e和密文c，求明文m（n，e不太大时）
#首先分解n，得到p，q
def nec_get_m(p,q,n,e,c):
    d=gmpy2.invert(e,(p-1)*(q-1))
    m=pow(c,d,n)
    st=long_to_bytes(m)
    print(st)


# c = 0x6cd55a2bbb49dfd2831e34b76cb5bdfad34418a4be96180b618581e9b6319f86
# n = 108539847268573990275234024354672437246525085076605516960320005722741589898641
# #n = int("",16)
# e = 65537
# #e = int("",16)
# q = 333360321402603178263879595968004169219
# p = 325593180411801742356727264127253758939
# get_m(p,q,n,e,c)


def ned_get_pq(n,e,d):
    while True:
        k = e * d - 1
        g = random.randint(0, n)
        while k%2==0:
            k=k//2
            temp=gmpy2.powmod(g,k,n)-1
            if gmpy2.gcd(temp,n)>1 and temp!=0:
                p=gmpy2.gcd(temp,n)
                q=n/p
                return p,q


# d=int("0x71ee0f4883690893ab503e97e25e6308d4c1e0a050cbea7b9c040f7a5b5b484afcecc8a9b3cc6bf089a1e83281562df217caab7220e3dfc14399139ce437af2f131f9345675e4d848cfab5827818eeab7834374be4a0513f81f3df125a932c2bb4c24c834d798bcc80f9c4a8770b01f8e54620b72a4f0491edd391e635d48e71",16)
# e=int("0x10001",16)
# n=int("0x71ee0f4883690893ab503e97e25e6308d4c1e0a050cbea7b9c040f7a5b5b484afcecc8a9b3cc6bf089a1e83281562df217caab7220e3dfc14399139ce437af2f131f9345675e4d848cfab5827818eeab7834374be4a0513f81f3df125a932c2bb4c24c834d798bcc80f9c4a8770b01f8e54620b72a4f0491edd391e635d48e71",16)
# p,q=ned_get_pq(n,e,d)
# print(p)
# print("%d" %(q))


#低加密指数小明文攻击，m非常小，且e较小，导致c<n，因此可直接对c开e次方
def low_m_e(c,e,n):
    k=0
    while(gmpy2.iroot(c+k*n,e)[1]==False):#开e次方，返回结果和状态
        k+=1
    print(k,c+k*n,gmpy2.iroot(c+k*n,e)[0])
    m=gmpy2.iroot(c+k*n,e)[0]
    return m

#low_m_e(3524799146410,3,100000980001501)

s=gmpy2.iroot(8,2)
print(s)



