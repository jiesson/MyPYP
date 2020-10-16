import jwt
import datetime
import base64
import hmac,hashlib
import json
import os

# def testKey(key, sig, contents, headDict, quiet):
#     if headDict["alg"] == "HS256":
#         testSig = base64.urlsafe_b64encode(hmac.new(key,contents,hashlib.sha256).digest()).decode('UTF-8').strip("=")
#     elif headDict["alg"] == "HS384":
#         testSig = base64.urlsafe_b64encode(hmac.new(key,contents,hashlib.sha384).digest()).decode('UTF-8').strip("=")
#     elif headDict["alg"] == "HS512":
#         testSig = base64.urlsafe_b64encode(hmac.new(key,contents,hashlib.sha512).digest()).decode('UTF-8').strip("=")
#     else:
#         print("Algorithm is not HMAC-SHA - cannot test with this tool.")
#         exit(1)
#     if testSig == sig:
#         cracked = True
#         if len(key) > 25:
#             print("\n[+] "+key[0:25].decode('UTF-8')+"...(output trimmed) is the CORRECT key!")
#         else:
#             print("\n[+] "+key.decode('UTF-8')+" is the CORRECT key!")
#         return cracked
#     else:
#         cracked = False
#         if quiet == False:
#             if len(key) > 25:
#                 print("[-] "+key[0:25].decode('UTF-8')+"...(output trimmed) is not the correct key")
#             else:
#                 print("[-] "+key.decode('UTF-8')+" is not the correct key")
#         return cracked

def get_b64_de(jwt):
    if(len(jwt)%3==1):
        jwt+="=="
    elif(len(jwt)%3==2):
        jwt+="="
    res=base64.b64decode(jwt)
    return res

def get_de(jwt):
    #jwt="1.2.3"
    ss=jwt.split(".")
    for i in ss:
        print(get_b64_de(i))

def en_jwt():
    head={
        "typ": "JWT",
        "alg": "HS256"
    }
    head_b64=base64.urlsafe_b64encode(json.dumps(head,separators=(",",":")).encode()).decode('UTF-8').strip("=")
    print(head_b64)
    playload={
        "secretid": [],
        "username": "admin",
        "password": "admin",
        "iat": 1597647315
    }
    play_b64=base64.urlsafe_b64encode(json.dumps(playload,separators=(",",":")).encode()).decode("UTF-8").strip("=")
    print(play_b64)
    content=head_b64+'.'+play_b64
    key='admin'
    Sig = base64.urlsafe_b64encode(hmac.new(key.encode('utf-8'), content.encode('utf-8'), hashlib.sha256).digest()).decode('UTF-8').strip("=")
    print(Sig)
    return content+'.'+Sig

def use_jwt():
    dic = {
        "secretid": [],
        "username": "admin",
        "password": "admin",
        "iat": 1597647315
    }
    s = jwt.encode(dic, key='secret', algorithm="HS256")
    print(s)
    #s="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZWNyZXRpZCI6W10sInVzZXJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6ImFkbWluIiwiaWF0IjoxNTk3NjQ3MzE1fQ.41SvKCKkmgrWQCahQcS8redJltnzKPIopKppN6g1Oow"
    s = jwt.decode(s, key='sss', algorithms="HS256")
    print(s)

def test_key(key,jw):
    j=jw.split(".")
    cont=j[0]+'.'+j[1]
    sig=j[2]
    Sig = base64.urlsafe_b64encode(hmac.new(key.encode('utf-8'), cont.encode('utf-8'), hashlib.sha256).digest()).decode('UTF-8').strip("=")
    if sig==Sig:
        print("success:"+key)
        return key
    return 0

def pass_dict():
    with open('常见.txt', "r") as f:
        data = f.readlines()
    f.close()
    return data

def get_key(jw):
    for i in pass_dict():
        i = i.strip('\n')
        tmp=test_key(key=i, jw=jw)
        if tmp!=0:
            return tmp


#print(en_jwt())
jw="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZWNyZXRpZCI6W10sInVzZXJuYW1lIjoiYWRtaW4iLCJwYXNzd29yZCI6ImFkbWluIiwiaWF0IjoxNTk3NjQ3MzE1fQ.n5dQCUvMstdUfxioXRt6fhuG04kX1UL9KrN7HfvzfaM"
print(get_key(jw))