import pymongo


class MongoConnector:

    def __init__(self, url="localhost:27017"):
        self.client = pymongo.MongoClient(url)
        self.dblist = self.client.list_database_names()

    def get_db_list(self):
        print(self.dblist)
        return self.dblist

    def create_new_db(self, db_name="newdb"):
        if db_name in self.dblist:
            print("已存在的db，请重命名")
        else:
            self.client[db_name]

