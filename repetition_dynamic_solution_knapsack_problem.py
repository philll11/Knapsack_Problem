weight = [6, 3, 4, 2]
value = [30, 14, 16, 9]


def knapsack(weightList, value, weight):
    dynamicList = [0] * (weight + 1)

    n = len(weightList)
    i = n - 1;
    w = 1;
    while i > -1:
        while w < weight + 1:
            if (w < weightList[i]):
                dynamicList[w] = dynamicList[w] + dynamicList[w - 1]
            else:
                dynamicList[w] = value[i]
            w = w + 1
        i = i - 1
    print(dynamicList)


knapsack(weight, value, 10)
