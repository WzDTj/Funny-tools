#!/usr/bin/python
#coding=utf-8

import os
from hashlib import md5

def get_dirctory():
    dirctory = raw_input(" - Enter your dirctory:")
    if valid_dirctory(dirctory):
        return dirctory
    else:
        print " - Invalid dirctory path. Enter again. - "
        return get_dirctory()

def valid_dirctory(dirctory):
    if os.path.exists(dirctory): return True
    else: return False

def get_filename_from_dir(dirctory):
    files = os.listdir(dirctory)
    return files

def print_filename(files):
    for file_name in files:
        print file_name

def get_md5code(file_path):
    new_md5 = md5()
    new_file = open(file_path, 'rb')
    new_md5.update(new_file.read())
    new_file.close()
    return new_md5.hexdigest()

# - main -

#获取目录并进入
#dirctory = '/Users/Dantong/Downloads'
#dirctory = '/'
dirctory = get_dirctory()
os.chdir(dirctory)

#获取目录下文件，筛选，生成MD5，打包成字典
temp_files = os.listdir(dirctory)

md5_code = []
files = []

print_filename(files)

for afile in temp_files:
    file_path = afile
    if os.path.isfile(file_path) and os.access(afile, os.R_OK):
        files.append(file_path)
        md5_code.append(get_md5code(file_path))
        print "File Path: " + file_path
        print "MD5 Code: " + get_md5code(file_path) 

dic = zip(md5_code, files)
dic.sort()
#print dic

#将移除文件列表，写入文件。
output = open('compare_list.txt', 'w')
output.write(' - Repetition files - \n')
remove_list = []
prev = ('0', '')
for afile in dic:
    if afile[0] == prev[0]:
        remove_list.append(afile)
        output.write("%s| %s\n" %(afile[1].center(25), prev[1].center(25)))

    prev = afile
output.write(' - End - \n')
output.close()

#需要删除前，列出文件清单，并询问用户
if len(remove_list) == 0:
    print " - No repetition file - "
else:
    print " - These files will be removed - \n"
    for afile in remove_list:
        print ' - ' + afile[1]
    print " - Total %d item(s) - " %(len(remove_list))
    print " - End - \n"

    flag = ''
    while flag != 'y' and flag != 'n':
        flag = raw_input(" - Confrim? (y/n)")
    else:
        if flag == 'y':
            for afile in remove_list:
                os.remove(afile[1])
                print " - %s was removed - " %(afile[1])
            print ' - Clear - '

print ' - Over - '
