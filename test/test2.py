#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test2.py
# @Author: Feng
# @Date  : 2018/10/9
# @Desc  :


# python opencv去图片水印（图片底色为白色）

# -*- coding: utf-8 -*-
import cv2, os, shutil, datetime, re, time
from threading import Thread
from hashlib import md5

PICHASH = {}


def md5_file(name):
    try:
        m = md5()
        a_file = open(name, 'rb')
        m.update(a_file.read())
        a_file.close()
        return m.hexdigest()

    except:
        return None


def nowater(dir, newdir, dirlist):
    global PICHASH
    for ppicdir in dirlist:
        print(ppicdir)
        print(os.path.isdir(dir + ppicdir))
        if os.path.isdir(dir + ppicdir):
            sortfiles = os.listdir(dir + ppicdir)
            if '.DS_Store' in sortfiles:
                sortfiles.remove('.DS_Store')
            sortfiles.sort()
            for oldfile in sortfiles:
                filetype = "." + oldfile.split(".")[len(oldfile.split(".")) - 1]
                picname_front = oldfile.split(filetype)[0]
                oldfile = dir + ppicdir + "/" + oldfile
                jpgname = picname_front + ".jpg"
                jpgname = newdir + ppicdir + "/" + jpgname

                try:
                    oldfile_hash = md5_file(oldfile)
                    oldfile_tmphashvalue = PICHASH.get(oldfile_hash)
                    file_object = open('pichash.txt', 'a')
                    file_object.write(oldfile + ":" + oldfile_hash + '\n')
                    file_object.close()
                    if (oldfile_tmphashvalue == None):
                        if not os.path.exists(newdir + ppicdir):
                            os.makedirs(newdir + ppicdir)
                        print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + oldfile + ",ing\n")
                        img = cv2.imread(oldfile)
                        x, y, z = img.shape
                        if x < 100:
                            print(datetime.datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S") + "," + jpgname + "too small , continue")
                        elif x > 5000:
                            print(datetime.datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S") + "," + jpgname + "too big , continue")
                        elif not os.path.exists(jpgname):
                            for i in range(x):
                                for j in range(y):
                                    varP = img[i, j]
                                    if sum(varP) > 250 and sum(varP) < 765:
                                        img[i, j] = [255, 255, 255]
                            cv2.imwrite(jpgname, img)
                            print("jpgname:" + jpgname)
                            PICHASH[oldfile_hash] = oldfile
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + oldfile + ",done\n")
                        else:
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + jpgname + "exists\n")

                    elif oldfile_tmphashvalue is not None:
                        if os.path.exists(jpgname):
                            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + jpgname + "exists\n")
                        else:
                            shutil.copyfile(oldfile_tmphashvalue, oldfile)
                            shutil.copyfile(oldfile, jpgname)
                            print(datetime.datetime.now().strftime(
                                "%Y-%m-%d %H:%M:%S") + "," + jpgname + " same with the old, continue")
                except Exception as e:
                    print("Exception:", e)
                    continue


if __name__ == '__main__':
    dir = "./pic/"
    newdir = "./picnew/"
    list0 = []
    list1 = []
    list2 = []
    for ppicdir in os.listdir(dir):
        file_path = (dir + ppicdir)#.replace('\\', '\\\\')
        print(ppicdir)
        print(file_path)
        print(os.path.isdir(file_path))
        if os.path.isdir(file_path):
            if re.compile(r'^[0-1].*').match(str(ppicdir)):
                list0.append(ppicdir)
            elif re.compile(r'^[2-3].*').match(str(ppicdir)):
                list1.append(ppicdir)
            elif re.compile(r'^[4-5].*').match(str(ppicdir)):
                list2.append(ppicdir)
            else:
                continue
        # else:
        #     nowater(dir, newdir, None)

    Thread(target=nowater, args=(dir, newdir, list0,)).start()
    Thread(target=nowater, args=(dir, newdir, list1,)).start()
    Thread(target=nowater, args=(dir, newdir, list2,)).start()
