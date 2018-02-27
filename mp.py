from threading import Thread

import os


def copyfile(source_dir,target_dir):
    source_list = os.listdir(source_dir)
    for sourcedir in source_list:
        sourcealldir = os.path.join(source_dir,sourcedir)
        targetalldir = os.path.join(target_dir,sourcedir)

        if os.path.isfile(sourcealldir):
            with open(sourcealldir,'rb') as rf:
                content = rf.read()
            with open(targetalldir,'wb') as wf:
                wf.write(content)
                wf.flush()
        if os.path.isdir(sourcealldir):
            if not os.path.exists(targetalldir):
                os.makedirs(targetalldir)
            copyfile(sourcealldir,targetalldir)





if __name__ == '__main__':
    print('主线程开始')
    list = []
    source_dir = r''  # 源目录
    target_dir = r''  # 目标目录
    sourcelist = os.listdir(source_dir)  # 获取根目录下所有路径 目的知道开启几个线程
    for sourcedir in sourcelist:  # 进行遍历 意思是每一个子目录自动开启一个线程
        sourcealldir = os.path.join(source_dir,sourcedir)  # 拼接源路径
        targetalldir = os.path.join(target_dir,sourcedir)  # 拼接目标路径

        if os.path.isfile(sourcealldir):  # 如果源目录下有文件的话  直接进行复制
            with open(sourcealldir,'rb') as rf:
                content = rf.read()
            with open(targetalldir,'wb') as wf:
                wf.write(content)
                wf.flush()
        if os.path.isdir(sourcealldir):  # 如果源目录下有子目录
            if not os.path.exists(targetalldir):  # 可省
                os.makedirs(targetalldir)  # 现在目标目录创建和源目录一样的子目录
            a = Thread(target=copyfile,args=(sourcealldir,targetalldir))  # 开启进程
            a.start()
            # a.join()
            list.append(a)

    for i in list:
        i.join()

    print('主线程结束')