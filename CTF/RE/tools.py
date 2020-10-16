import hashlib

def xor():
    a="{\\rtf1"
    b=[0x05,0x7d,0x41,0x15,0x26,0x01]
    flag=''
    for i,j in enumerate(b):
        flag+=chr(ord(a[i])^j)
    print(flag)

def h_t_a():
    s = [0x70, 0x76, 0x6b, 0x71, 0x7b, 0x6d, 0x31, 0x36, 0x34, 0x36, 0x37, 0x35, 0x32, 0x36, 0x32, 0x30, 0x33, 0x33,
         0x6c, 0x34, 0x6d, 0x34, 0x39, 0x6c, 0x6e, 0x70, 0x37, 0x70, 0x39, 0x6d, 0x6e, 0x6b, 0x32, 0x38, 0x6b, 0x37,
         0x35, 0x7d]
    ff = ''
    for i in s:
        ff += chr(i)
    print(ff)

def kaisha():
    s="pvkq{m164675262033l4m49lnp7p9mnk28k75}"
    k="abcdefghijklmnopqrstuvwxyz"
    for i in range(27):
        print("key=%d"%i)
        for ss in s:
            if ss.isalpha():
                n=k.find(ss)
                ss=k[n-i]
            print(ss,end='')
        print('\n')


def hash_cra():
    flag='@DBApp'
    for i in range(100000,999999):
        s=str(i)+flag
        x=hashlib.sha1(s.encode())
        cnt=x.hexdigest()
        if "6e32d0943418c2c" in cnt:
            print(cnt)
            print(s)

