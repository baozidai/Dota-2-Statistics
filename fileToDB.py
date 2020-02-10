import json
import time

from d2s_init import GameSaver


def process(data):
    index = 0
    lenth = len(data)
    while index < lenth:
        datadic = data[index]
        if "radiant_team" in datadic.keys():
            k = data[index]["radiant_team"]["team_logo"]
            data[index]["radiant_team"]["team_logo"] = str(k)
        if "dire_team" in datadic.keys():
            k = data[index]["dire_team"]["team_logo"]
            data[index]["dire_team"]["team_logo"] = str(k)
        index += 1
    return data


def get_content():
    global flag, path
    if path == "":
        flag = 1
        return
    path = path[:-1]
    with open(path, "rt", encoding="utf-8") as f1:
        content = f1.read()
    return json.loads(content, encoding="utf-8")


if __name__ == "__main__":
    gameSaver = GameSaver.GameSaver()
    gameSaver.init_progressing_game()
    f = open("pathlist.txt", "rt", encoding="utf-8")
    flag = 0
    path = ""
    counter = 0

    t1 = time.time()
    try:
        while True:
            path = f.readline()
            data = get_content()
            if flag == 1:
                break
            elif isinstance(data[-1], str):
                data.pop()
            try:
                data = process(data)
                gameSaver.d2s_in_progress_game_col.insert_many(data)
                counter += 1
                if counter % 1000 == 0:
                    print("耗时{:.1f}s，存入{}/88271个文件".format((time.time() - t1), counter))
            except Exception as e:
                print(path)
                print(data)
                e.with_traceback()
    except Exception as e:
        print(path)
        print(data)
        e.with_traceback()
    print("总耗时:{:.1f}s".format(time.time() - t1))
