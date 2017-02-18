#encoding:utf-8
import os
import sys

path=sys.path[0]#当前文件夹路径
#path=sys.argv[1] #以命令行的参数传递


for file in os.listdir(path):
    oldpath=os.path.join(path,file)
    if os.path.isdir(oldpath):
        continue
    filename=os.path.splitext(file)[0]
    filetype=os.path.splitext(file)[1]
    if filename.find('@3x')>=0:
        newpath=os.path.join(path,filename.split('@3x')[0]+filetype)
        # 取@3x前面的字符，若需要取后面的字符则使用filename.split('@3x')[1]
    if not os.path.isfile(newpath):
        os.rename(oldpath, newpath)
        print newpath, 'ok'







