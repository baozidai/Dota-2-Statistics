import pymongo

false = False; true = True


class GameSaver:

    dbclient = None
    d2s_db = None
    d2s_in_progress_game_col = None
    d2s_after_game_col = None

    def __init__(self,url="mongodb://localhost:27017/"):
        self.dbclient = pymongo.MongoClient(url)
        self.d2s_db = self.dbclient["d2s"]
        # self.d2s_in_progress_game_col = self.d2s_db["d2s_in_progress_game"]

    def init_progressing_game(self):
        """
        初始化进行中的游戏的collection
        :return:
        """
        self.d2s_in_progress_game_col = self.d2s_db["d2s_in_progress_game"]

    def init_after_game(self):
        """
        初始化赛后数据集合
        :return:
        """
        self.d2s_after_game_col = self.d2s_db["d2s_after_game"]

    def save_one_file(self, data):
        self.d2s_in_progress_game_col.insert_many(data)

