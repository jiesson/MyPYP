import hashlib
def md5(s):
    md5=hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

def filehash():
    filename='/fllllllllllllag'
    cookie_secret='414be64e-c786-433a-8bb5-dfc1bb88d11a'
    print(md5(cookie_secret+md5(filename)))

filehash()