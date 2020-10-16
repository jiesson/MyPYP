
f=open('usbdata.txt','r')
ss=f.read()
#print(ss)
f.close()
ss=ss.split('\n')
for i in ss:
    if len(i)==16:
        print(i[:8])


#php代码执行
#Netgear DGN设备远程命令执行漏洞
#针对PCL的Rockwell Automation拒绝服务
#系统命令执行