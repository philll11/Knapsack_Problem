weight = [6, 3, 4, 2]
value = [30, 14, 16, 9]

def dynamicKnapsack(weightList, value, n, weight):
    dynamicList = [0] * (n + 1)
    for i in range(n + 1): dynamicList[i] = [0] * (weight + 1)
    
    for i in range(n + 1):
        for w in range(weight + 1):
            if i == 0 or w == 0:
                dynamicList[i][w] = 0
            elif weightList[i - 1] <= w:
                dynamicList[i][w] = max(value[i - 1] + dynamicList[i - 1][w - weightList[i - 1]],  dynamicList[i - 1][w])
            else:
                dynamicList[i][w] = dynamicList[i - 1][w]

##    for l in dynamicList:
##        for l2 in l:
##            print(l2, end='\t')
##        print('\n')        

    return dynamicList[n][weight]


def dynamicMultipleKnapsack(weightList, value, n, weight):
    dynamicList = [0] * (n + 1)
    for i in range(n + 1): dynamicList[i] = [0] * (weight + 1)
    
    for i in range(n + 1):
        for w in range(weight + 1):
            if i == 0 or w == 0:
                dynamicList[i][w] = 0
            elif weightList[i - 1] <= w:
                dynamicList[i][w] = max(value[i - 1] + dynamicList[i][w - weightList[i - 1]],  dynamicList[i - 1][w])
            else:
                dynamicList[i][w] = dynamicList[i - 1][w]

##    for l in dynamicList:
##        for l2 in l:
##            print(l2, end='\t')
##        print('\n')        

    return dynamicList[n][weight]

print(dynamicMultipleKnapsack(weight, value, len(weight), 10))
print(dynamicKnapsack(weight, value, len(weight), 10))
