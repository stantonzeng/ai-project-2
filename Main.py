import numpy as np
import math
import time

def open_small(num):
    things = []

    with open('Ver_2_CS170_Fall_2021_Small_data__{}.txt'.format(num), 'rt', encoding='utf-8') as f:
        for x in f:
            things.append(x)
    return things

def open_large(num):
    things = []

    with open('Ver_2_CS170_Fall_2021_LARGE_data__{}.txt'.format(num), 'rt', encoding='utf-8') as f:
        for x in f:
            things.append(x)
    return things

def parse_text(things, size):
    features_list = []
    for i in range(0, size+1):
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
                nest_list.append(float(i[j:x]))
            elif i[x] == " ": 
                help = -1
                nest_list = features_list[count]
                nest_list.append(float(i[j:x]))
                count = count + 1

    return features_list


def print_everything(features_list):
    for i in features_list:
        print(i)

def get_sum(features_list, myset, x, f, i):
    sum = 0
    for z in range(1, len(features_list)):
        if z == i:
            continue
        # print("Comparing",x,"at", features_list[z][x], "with",f, "at",features_list[z][f], "using feature", z, "at value",myset[z], "minus", i)
        sum += (myset[z]*(features_list[z][x]-features_list[z][f]))**2
    return sum

def finding_neighbor(features_list, myset):
    best_accuracy = 0
    best_feature = -1

    for i in range(1, len(features_list)): #For each feature
        correct = 0
        if(myset[i] != 0): #As long as we have not checked this feature yet
            continue 
        for x in range(len(features_list[0])): #Which object we are measuring (out of 500)
            nearest_neighbor = -1
            nearest_class = -1
            distance_apart = math.inf
            
            for f in range(len(features_list[0])): #Object that we are comparing it with
                if f == x:
                    continue
                # print("Seeing if", x, "is nearest neighbor with", f)
                # print("i:",i)
                d = math.sqrt( get_sum(features_list, myset, x, f, i) + ((features_list[i][x]-features_list[i][f])**2) )
                if d < distance_apart:
                    nearest_neighbor = f
                    nearest_class = features_list[0][f]
                    distance_apart = d

            # print(x+1, "is nearest neighbor with", nearest_neighbor+1, "at class", nearest_class, "using feature", i)
            # print("Compared",features_list[i][x],"with", features_list[i][nearest_neighbor])
            # print("Compared",features_list[0][x],"with", nearest_class)
            if nearest_class == features_list[0][x]:
                correct += 1
        
        accuracy = correct/len(features_list[0])
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_feature = i
    
    myset[best_feature] = 1

    temp_set = []

    for i in range(1,len(features_list)):
        if myset[i] == 1:
            temp_set.append(i)
    
    print("The best accuracy is:", best_accuracy, "with feature", best_feature, "for the set" ,temp_set)
    


if __name__ == "__main__":
    # things = open_small(101)
    # size = 5

    things = open_small(86)
    size = 10

    # things = open_large(27)
    # size = 50
    features_list = parse_text(things, size)
    print(len(features_list))

    myset = {}

    for i in range(1, len(features_list)):
        myset[i] = 0

    accuracy_list = []
    for i in range(1, len(features_list)):
        finding_neighbor(features_list, myset)
        # time.sleep(5)
    
