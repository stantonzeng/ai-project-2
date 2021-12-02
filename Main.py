import numpy as np
import math

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

def finding_neighbor(features_list, myset):
    # print("hi")
    
    best_accuracy = 0
    best_feature = -1

    for i in range(1, 11): #For each feature
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
                d = math.sqrt((features_list[i][x]-features_list[i][f])**2)
                if d < distance_apart:
                    nearest_neighbor = f
                    nearest_class = features_list[0][f]
                    distance_apart = d

            print(x, "is nearest neighbor with", nearest_neighbor, "at class", nearest_class, "using feature", i)
            # print("Compared",features_list[i][x],"with", features_list[i][nearest_neighbor])
            if nearest_class == features_list[0][x]:
                correct += 1
        
        accuracy = correct/500
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_feature = i
    
    print("The best accuracy is:", best_accuracy, "with feature",best_feature)

        
    


if __name__ == "__main__":
    things = open_small(86)
    features_list = parse_text(things)

    myset = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

    accuracy_list = []
    # for i in range(0, 10):
    finding_neighbor(features_list, myset)
    # print_everything(features_list)
    
