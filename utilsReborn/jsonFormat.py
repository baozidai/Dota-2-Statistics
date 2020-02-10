import os
import time


def walk_files(listpath):
    t1 = time.time()
    counter = 0
    for root, dirs, files in os.walk("D:\\Dota2比赛数据\\data"):
        # for dir in dirs:
        #     print(os.path.join(root, dir))
        for file in files:
            write_to_file(os.path.join(root, file), listpath)
            counter+=1
            if counter%1000==0:
                print("耗时{}s，{}个文件".format((time.time()-t1), counter))
    print("总耗时{}s，共{}个文件".format((time.time()-t1), counter))


def write_to_file(path, file_path):
    with open("pathlist.txt", "at", encoding="utf-8") as f:
        f.write(path+"\n")
