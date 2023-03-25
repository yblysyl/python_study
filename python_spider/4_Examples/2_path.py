import os
print(os.getcwd())#返回当前工作目录的路径名
print(os.path.abspath(__file__))#返回当前文件的绝对路径
print(os.path.realpath(__file__))#返回当前文件的规范路径
#print(os.path.dirname())#返回指定路径名的父目录名
print(os.path.dirname(os.path.abspath(__file__)))  #来获取当前文件所在的文件夹路径
 