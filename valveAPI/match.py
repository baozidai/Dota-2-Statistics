import json
import time
import utils
from d2s_init import GameSaver

class Match:

    """比赛相关的接口类"""

    def __init__(self,key=None):
        '''
        Match类的初始化方法，需要提供一个APIkey
        :param key: API key
        '''
        self.key = key
        if self.key == None:
            print("You did not init me with a avaliable API key")

    def getLivingLeagueMatches(self):
        rawUrl = "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/"
        # "https://api.steampowered.com/IDOTA2Match_570/GetLiveLeagueGames/v0001/?key=D518F9B2B7774F0AB3061DA164B9AABB"
        key = self.key
        url = rawUrl + "?key={}".format(key)
        result = utils.requestsGet(url)
        if result == "503ERROR":
            matches = result
        else:
            matches = result['games']
            if matches == []:
                matches = "EMPTYERROR"
            else:
                matches = utils.resultAppendTime(matches) #  在尾部添加时间戳
        return matches
    def saveLivingLeagueMatches(self,fileName="./matches"):
        matches = self.getLivingLeagueMatches()
        if matches == "503ERROR":
            return "503ERROR"
        elif matches == "EMPTYERROR":
            return matches
        timeNow = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        utils.resSaveToJson(matches, fileName + "_" + timeNow)
        return 0

    def get_after_game_statistic(self, match_id):
        apiUrl = "http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1?key={}&match_id={}"
        key = self.key
        return utils.requestsGet(apiUrl.format(key, match_id))

    def save_after_game_statistic_to_bd(self, match_id):
        web_back_dict = self.get_after_game_statistic(match_id)
        result_dict = web_back_dict['result']
        # result_string = json.dumps(result_dict)
        after_game_statistic_saver = GameSaver.GameSaver()
        after_game_statistic_saver.init_after_game()
        try:
            after_game_statistic_saver.d2s_after_game_col.insert_one(result_dict)
            return None
        except Exception:
            return result_dict




