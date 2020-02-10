import logging
from datetime import datetime
import json
import os
import time

import requests

logging.basicConfig(filename="errors.log",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=30)

def resSaveToJson(res,fileName):
    '''
    将结果存为Json
    :param res: 传入ClientAPI返回的原始数据，这里要求一个字典dict
    :param fileName: 要储存的文件名，不需要手动输入json后缀. 带路径时使用 / 分隔
    :return: NULL 输出一个存用目标内容的json文件
    '''
    fileName = needSuffix(fileName)
    isDirExistence(dirCut(fileName))
    with open(fileName,'w') as outfile:
        resJson = json.dumps(res,indent=4)
        outfile.write(resJson)
        outfile.close()

def dirCut(fileNameWithDir):
    '''
    切取文件路径
    :param fileNameWithDir: 带想读路径的文件名
    :return: NULL
    '''
    count = fileNameWithDir.rindex("/")
    dir = fileNameWithDir[:count]
    return dir

def isDirExistence(dir):
    '''
    判断路径存在，不存在则尝试创建
    :param dir: 原始路径
    :return: True or False   为False时会自动创建目录
    '''
    if os.path.isdir(dir):
        return True
    else:
        os.mkdir(dir)
        return False

def needSuffix(fileName):
    '''
    判断有无后缀并尝试加入
    :param fileName: 原始文件路径
    :return: 带后缀的文件名
    '''
    if not fileName.endswith(".json"):
        fileName = fileName+".json"
    else:
        return fileName
    return fileName
def requestsGet(url):
    '''
    提供一个API地址，该方法将发送请求该API并返回result域中的内容
    :param url: API地址
    :return: 返回结果中的result域
    '''
    result = None
    requestResult = requests.get(url)
    if 200 == requestResult.status_code:
        resultDict = json.loads(requestResult.text)
        #  test ↓ code
        # resultDict['result']['status'] == 503
        #  test ↑ code
        if 'status' in resultDict['result'].keys(): # 这个if复制判断是赛中数据还是赛后数据，有status的是赛中数据
            if resultDict['result']['status'] == 200:
                result = resultDict['result']
            elif resultDict['result']['status'] == 503:
                result = "503ERROR"
            else:
                logging.warning("result不可靠，可能是V社API的原因")
        else:
            result = resultDict
    elif 503 == requestResult.status_code:
        logging.warning("V社API忙，等待30s")
        result = "503ERROR"
    else:
        logging.warning("调取远端API失败，可能是网络原因")
    requestResult.close()  # 显示关闭连接
    return result
def resultAppendTime(result):
    localTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 产生时间戳
    result.append(localTime)  # 添加当前时间在result最后
    return result
def clearFileInThisDir(dir="./"):
    pass
    # TODO：遍历文件夹文件删除无用数据文件

