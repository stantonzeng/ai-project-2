import numpy as np

def open_small(num):
    things = []

    with open('Ver_2_CS170_Fall_2021_Small_data__{}.txt'.format(num), 'rt', encoding='utf-8') as f:
        for x in f:
            things.append(x)
    return things

def parse_text(things):
    features_list = []
    for i in range(0, 11):
        features_list.append([])
    
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
                nest_list = features_list[count]
                nest_list.append(i[j:x])
            elif i[x] == " ": 
                help = -1
                nest_list = features_list[count]
                nest_list.append(i[j:x])
                count = count + 1

    return features_list


def print_everything(features_list):
    for i in features_list:
        print(i)

if __name__ == "__main__":
    things = open_small(86)
    features_list = parse_text(things)
    # print_everything(features_list)
    
