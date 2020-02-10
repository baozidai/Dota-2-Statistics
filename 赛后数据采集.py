# 根据当前数据库中有的进行中比赛来采集数据
import time

from d2s_init import GameSaver
from valveAPI import match, mykey

match_id_list = set()
match_id = None

m = match.Match(mykey)

game_saver = GameSaver.GameSaver()
game_saver.init_progressing_game()

t1 = time.time()
# 全id存入
id_counter = 0
print_flag = 1
for i in game_saver.d2s_in_progress_game_col.find():
    match_id_list.add(i['match_id'])
    if id_counter != match_id_list.__len__():
        id_counter = match_id_list.__len__()
        print_flag = 1
    if id_counter % 1000 == 0 and print_flag == 1:
        print("id载入{}个，耗时{:.1f}s".format(id_counter, (time.time() - t1)))
        print_flag = 0
t2 = time.time()
print("id载入内存完成，共{}个，耗时{:.1f}s".format(id_counter, (t2 - t1)))

total = match_id_list.__len__()
counter = 0


while match_id_list.__len__() != 0:
    match_id = match_id_list.pop()
    matchSaver = match.Match(mykey)
    code = matchSaver.save_after_game_statistic_to_bd(match_id)
    if code is None:
        counter += 1
    else:
        print("error")
        print(code)
    if counter % 100 == 0:
        print("存入{}场比赛, 已用时{}s, 程序合计用时{}s".format(counter, (time.time() - t2), time.time() - t1))

print("共存入{}场比赛, 已用时{}s, 程序合计用时{}s".format(counter, (time.time() - t2), time.time() - t1))
