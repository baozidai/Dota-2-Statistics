import json

import requests

import utils
from valveAPI import mykey


def getHeroesList(APIkey=mykey,language="zh_cn",IfItemizedonly=True):
    heroesList = None
    rawUrl = "http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1?key={}&language={}&itemizedonly={}"
    url = rawUrl.format(APIkey,language,IfItemizedonly)
    requestResult = requests.get(url)
    if 200 == requestResult.status_code:
        resultDict = json.loads(requestResult.text)
        if resultDict['result']['status'] == 200:
            heroesList = resultDict['result']['heroes']
            print(heroesList)
        else:
            print("读取英雄列表失败，可能是V社API的原因")
    else:
        print("读取英雄列表失败，可能是网络原因")
    return heroesList

def saveHeroList(fileName="heroList.json",APIkey=mykey,language="zh_cn",IfItemizedonly=True):
    heroesList = getHeroesList(APIkey,language,IfItemizedonly)
    utils.resSaveToJson(heroesList, fileName)