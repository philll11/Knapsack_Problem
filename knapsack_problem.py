weight = [6, 3, 4, 2]
value = [30, 14, 16, 9]

def knapsackSingleItems(weightList, valueue, n, i, weight):
    if i == n:
        return 0
    if weightList[i] > weight:
        return knapsackSingleItems(weightList, value, n, i + 1, weight)
    return max(value[i] + knapsackSingleItems(weightList, value, n, i + 1, weight - weightList[i]),
               knapsackSingleItems(weightList, value, n, i + 1, weight))


def knapsackMultipleItems(weightList, value, n, i, weight):
    if i == n:
        return 0
    if weightList[i] > weight:
        return knapsackMultipleItems(weightList, value, n, i + 1, weight)
    return max(value[i] + knapsackMultipleItems(weightList, value, n, i, weight - weightList[i]),
               knapsackMultipleItems(weightList, value, n, i + 1, weight))


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


print(knapsackMultipleItems(weight, value, len(weight), 0, 10))
print(dynamicMultipleKnapsack(weight, value, len(weight), 10))

print(knapsackSingleItems(weight, value, len(weight), 0, 10))
print(dynamicKnapsack(weight, value, len(weight), 10))



























