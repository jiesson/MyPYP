import os
import shutil

def get_file_name_list(file_dir):
    '''
    :brief:获取文件夹下内，所有文件
    :param file_dir:文件夹目录
    :return: 文件列表
    '''
    for root,dirs,files in os.walk(file_dir):
        return files

def print_all_files(file_list,s):
    '''
    :brief:输出所有文件名
    :param file_list: 文件列表
    :return:
    '''
    for file_name in file_list:
        if file_name[-5]==s:
            print(file_name)
            cop(file_name)
            #return file_name

def cop(file):
    name=str(file)
    # ss='copy D:\\桌面\\2008245f43dd0413b96\\2008245f43dd0625dca\\部分标记有误的数据\\'+str(name)+' D:\\桌面\\2008245f43dd0413b96\\2008245f43dd0625dca\\0\\'+str(name)
    #     # os.system(ss)
    shutil.copyfile('d:\\sss\\aaa\\'+str(name),'d:\\sss\\0\\'+str(name))
#使用：
filename_list = get_file_name_list('D:\\sss\\aaa')
print_all_files(filename_list,"w")

#cop("0_w.jpg")