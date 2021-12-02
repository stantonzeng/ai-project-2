import numpy as np

things = []

with open('Ver_2_CS170_Fall_2021_Small_data__86.txt', 'rt', encoding='utf-8') as f:
    # lines = f.readlines()
    for x in f:
        things.append(x)

feature = []

features_list = []
for i in range(0, 11):
    features_list.append(feature)

print(len(things))
for i in things:
    help = 1
    count = 0
    j = 3
    for x in range(3, len(i)):
        if help == -1 and i[x] == " ":
            continue

        if help == -1:
            j = x
        help = 1
        if x == len(i)-1:
            features_list[count].append(i[j:x])
        elif i[x] == " ": 
            help = -1
            features_list[count].append(i[j:x])
            count = count + 1

for i in features_list:
    print(i)

