from pathlib import Path
import re



dict_first_path = {}
dict_second_path = {}

path1 = "C:/Users/MaksRS/YandexDisk/Test/Relematika_V3/RTDS/pdf/"
path2 = "C:/Users/MaksRS/YandexDisk/Test/Relematika_V3/Терминал Релематика/ПСА_Терминал НВЧЗ/"
p1 = Path(path1)
n = 1
for x in p1.rglob("*"):
    path_file = str(x).split(" ")
    time_file = path_file[5].split("_")
    time_file[2] = time_file[2].split(".")[0]
    dict_first_path[n] = time_file
    n = n + 1
p2 = Path(path2)
n = 1
for x in p2.rglob("*"):
    path_file = str(x).split("\\")
    name_file = path_file[8]
    if (name_file.split(".")[1] == "cfg"):
        # print(type(name_file))
        time_file = name_file.split("_")
        # print(time_file)
        dict_second_path[n] = [time_file[4], time_file[5], time_file[6]]
        n = n + 1

for key1, item1 in dict_first_path.items():
    # print(key1, item1)
    flag = False
    for key2, item2 in dict_second_path.items():
        # print(key2, item2)
        if (int(item1[0]) == int(item2[0])) and (int(item1[1]) == int(item2[1])) and (int(item1[2]) - 3 < int(item2[2]) < int(item1[2]) + 3):
            flag = True
    if not flag:
        print("Отсутствует тест --->", key1, item1)

