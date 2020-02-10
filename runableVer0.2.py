import logging
import os
import requests
import urllib3

from valveAPI import getHeros, mykey
import time
from valveAPI.match import Match

# 日志系统初始化

# logger初始化
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)  # logger等级设置
# 文件handler初始化
handler = logging.FileHandler(r"./warn.log")
handler.setLevel(logging.INFO)
# 日志格式化范式
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s")
handler.setFormatter(formatter)  # 格式绑定
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# logger和handler绑定
logger.addHandler(handler)
logger.addHandler(console)

# test code
# logger.info("start print log")
# logger.debug("do something")
# logger.warning("Something maybe fail.")
# try:
#     open("sklearn.txt", "rb")
# except (SystemExit, KeyboardInterrupt):
#     raise
# except Exception:
#     logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)
time.sleep(5) # 等待5秒，更新生命周期
match = Match(mykey)
counter = 0
nowDate = ""
startTime = time.time()
while True:
    if time.time() - startTime > 7200:  # 2h一个周期
        logger.info("生命周期完成，正在更新周期")
        os.system("nohup python3 -u ./runableVer0.2.py  params1 > nohupDevVer2.out 2>&1 &")
        break
    rawDir = "../Matches_data{}/matches"
    if counter == 0:
        nowDate = time.strftime('%Y%m%d', time.localtime(time.time()))
        fileDir = rawDir.format(nowDate)
    elif nowDate != time.strftime('%Y%m%d', time.localtime(time.time())):
        logger.info("昨日命中数据{}次".format(counter))
        counter = 0
        continue
    try:
        status = match.saveLivingLeagueMatches(fileDir)
        if status == "503ERROR":
            time.sleep(30)
            continue
        elif status == "EMPTYERROR":
            time.sleep(1)
            continue
        counter += 1
        time.sleep(15)
    except KeyboardInterrupt:
        break
    except TimeoutError:
        logger.exception("超时错误", exc_info=True)
        for i in range(60):
            logger.info("\r超时,正在等待,还剩{}s".format(300 - i))
            time.sleep(1)
    except urllib3.exceptions.NewConnectionError:
        logger.exception("建立新连接出错", exc_info=True)
        for i in range(60):
            logger.info("\r正在等待,还剩{}s".format(60 - i))
            time.sleep(1)
    except urllib3.exceptions.MaxRetryError:
        logger.exception("新连接建立重试次数过多".format(60 - i), exc_info=True)
        for i in range(60):
            logger.info("\r重试次数过多,正在等待,还剩{}s".format(60 - i))
            time.sleep(1)
    except requests.exceptions.ConnectionError:
        logger.exception("request库底部错误", exc_info=True)
        for i in range(60):
            logger.info("\r重试次数过多,正在等待,还剩{}s".format(60 - i))
            time.sleep(1)
    except Exception:
        logger.exception("这里出错了，请看错误日志", exc_info=True)
        time.sleep(1)
    else:
        logger.info("命中{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
