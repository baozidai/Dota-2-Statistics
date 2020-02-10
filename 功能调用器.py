from valveAPI import getHeros
from valveAPI import match, mykey

# getHeros.saveHeroList("./data/heroList.json")
# m = match.Match(mykey)
# m.save_after_game_statistic_to_bd(5113724542)
from d2s_init import GameSaver

game_saver = GameSaver.GameSaver()
game_saver.init_progressing_game()
game_saver.init_after_game()
query = {"match_id": 5113724542}

matchSaver = match.Match(mykey)
matchSaver.save_after_game_statistic_to_bd(5113724542)
# f = game_saver.d2s_after_game_col.find_one(query)
# for i in f:
#     # print(i['match_id'])
#     print(type(i))

# print(f)

# for i in game_saver.d2s_in_progress_game_col.find():
#     print(type(i['match_id']))