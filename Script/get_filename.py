# -*- coding: utf-8 -*-
# get file name in dictionary
# 本代码用于判断删除.hdi记录条数还是删除照片数，并返回删除对象名称和自动删除对象
import os
import shutil


# 获取文件夹下所有文件的文件名，存入列表L1
def file_name(file_dir):

    L1 = []
    for a,b,files in os.walk(file_dir):
        L = files
        for e in L:
            L1.append(e.split('.')[0])
    return L1


# 读取hdi中的文件名，存入列表L2
def check_hdi_file(file_dir, separator='\t', sep=0):

    try:
        with open(file_dir, 'r') as f:
            L2 = []
            try:
                lines = f.readlines()
                for line in lines:
                    d = line.split(separator)[sep]
                    L2.append(d)
                return L2
            except:
                print(Exception)
            finally:
                f.close()
    except:
        print(Exception)


# 比较两个列表，并把差异元素输出至文件f2
def diff(l1, l2):

    e_dir = []
    if len(l1) == len(l2):
        return 0
    elif len(l1) > len(l2):
        e_dir = [x for x in l1 if x not in l2]
        print('del images', file=f2)
        print('imagefiles', len(imagefiles), '\thdi', len(hdi),
              '\tdel number', len(e_dir), file=f2)
    elif len(l1) < len(l2):
        e_dir = [x for x in l2 if x not in l1]
        print('del hdi', file=f2)
        print('imagefiles', len(imagefiles), '\thdi', len(hdi),
              '\tdel number', len(e_dir), file=f2)
    for e in e_dir:
        print(e,'\tfalse',end='\n', file=f2)


# 调用diff方法，创建result.txt
try:
    with open('/home/froment/Documents/script/result.txt', 'w') as f2:
        try:
            imagefiles = file_name('/home/froment/Documents/script/HDpano/')
            hdi = check_hdi_file('/home/froment/Documents/script/iScan-Image-1.hdi')
            result = diff(imagefiles, hdi)
        except:
            print(Exception)
        finally:
            f2.close()
except:
    print(Exception)


''' 开发自动删除照片或删除hdi条目功能，并输出报告'''


# 读取result文件，mode='base'：判断删除照片还是hdi记录
class sourceFile():

    @staticmethod
    def r_File(source_path, mode='base', seq=1):
        try:
            with open(source_path, 'r') as file:
                try:
                    if mode is 'base':
                        Which_del = file.readline().split(' ')[seq]
                        return Which_del
                    elif mode is not 'base':
                        Which_del = file.readlines()
                        return Which_del
                except:
                    print('文件打开异常')
                finally:
                    file.close()
        except:
            print(Exception)


# 读取hdi文件
class Hdi():

    @staticmethod
    def get_Hdi(hdi_path):
        try:
            with open(hdi_path, 'r') as file:
                try:
                    lines = file.readlines()
                    return lines
                except:
                    print("3")
                finally:
                    file.close()
        except:
            print(Exception)


# 对hdi文件创建备份
class targetFile():

    @staticmethod
    def backup_target(path, backup_path):
        shutil.copy2(path, backup_path+'iScan-Image-1_b.hdi')
        return print("finish")


'''删除hdi记录'''


def del_hdi(result_path, source, backup):

    # 判断是否删除hdi记录
    log = sourceFile().r_File(result_path)
    if 'hdi' in log:
        # 备份hdi
        b = targetFile()
        b.backup_target(source, backup)
    else:
        return 0

    # 调用check_hdi_file方法，路径改为result_path，以列表形式记录result中要删除的对象名称
    infos = check_hdi_file(result_path, separator=' ')[2:]
    # print(infos)

    # 以列表形式读取hdi行，查找要删除的行号lineno_list
    hdi_lines = Hdi().get_Hdi(source_file_path)
    lineno_list = []
    for count in list(range(len(infos))):
        lineno = 0
        for i in hdi_lines:
            if infos[count] in i:
                lineno_list.append(lineno)
                break
            else:
                lineno += 1
    lineno_list = lineno_list[::-1]
    print(len(lineno_list))

    # 删除hdi特定某些行
    for del_line in lineno_list:
        with open(source_file_path, 'r') as old_file:
            with open(source_file_path, 'r+') as new_file:

                current_line = 0

                # 定位到需要删除的行
                while current_line < (del_line):
                    old_file.readline()
                    current_line += 1

                # 当前光标在被删除行的行首，记录该位置
                seek_point = old_file.tell()

                # 设置光标位置
                new_file.seek(seek_point, 0)

                # 读需要删除的行，光标移到下一行行首
                old_file.readline()

                # 被删除行的下一行读给 next_line
                next_line = old_file.readline()

                # 连续覆盖剩余行，后面所有行上移一行
                while next_line:
                    new_file.write(next_line)
                    next_line = old_file.readline()

                # 写完最后一行后截断文件，因为删除操作，文件整体少了一行，原文件最后一行需要去掉
                new_file.truncate()

    with open(source_file_path, 'r') as check:
        l = check.readlines()
        print(len(l))


# 执行删除hdi指定字符串所在行，result_file_path（中间过程路径），
#   source_file_path（hdi源文件路径），backup_path（备份路径）
try:
    result_file_path = r'/home/froment/Documents/script/result.txt'
    source_file_path = r'/home/froment/Documents/script/iScan-Image-1.hdi'
    backup_path = r'/home/froment/Documents/script/'
    del_hdi(result_file_path, source_file_path, backup_path)
except:
    print(Exception)

# 调用diff方法，创建check.txt
try:
    with open('/home/froment/Documents/script/check.txt', 'w') as f2:
        try:
            imagefiles = file_name('/home/froment/Documents/script/HDpano/')
            hdi = check_hdi_file('/home/froment/Documents/script/iScan-Image-1.hdi')
            result = diff(imagefiles, hdi)
        except:
            print(Exception)
        finally:
            f2.close()
except:
    print(Exception)