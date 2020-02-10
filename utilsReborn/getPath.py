def get_path(pathlist):
    with open(pathlist, "rt", encoding="utf-8") as f:
        path = f.readline()
    return path
