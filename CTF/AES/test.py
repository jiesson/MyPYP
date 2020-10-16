# abcdefghijklmnopqrstuvwxyz
# fghijklmnopqrstuvwxyz
#
#
# afZ_r9VYfScOeO_UL^RWUc
# flag{}
#=E9=82=A3=E4=BD=A0=E4=B9=9F=E5=BE=88=E6=A3=92=E5=93=A6

# 在一次RSA密钥对生成中，假设p=473398607161，q=4511491，e=17
# 求解出d作为flga提交,已知pq求d，de mod N=1
def baopo_d():
    p=473398607161
    q=4511491
    e=17
    #n=p*q
    N=(p-1)*(q-1)
    k=1
    while 1:
        k=k+1
        if((k*e)%N==1):
            print(k)
            return 0

baopo_d()