import logging
from valveAPI import getHeros, mykey
import time
from valveAPI.match import Match


match = Match(mykey)
logging.basicConfig(filename="errors.log",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    level=30)

match = Match(mykey)
counter = 0
while True:
    rawDir = "../Matches_data{}/matches"
    if counter == 5760 or counter == 0:
        nowTime = time.strftime('%Y%m%d', time.localtime(time.time()))
        fileDir = rawDir.format(nowTime)
        if counter == 5760:
            counter = 0
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
    except Exception as a:
        logging.error(a)
        time.sleep(1)
