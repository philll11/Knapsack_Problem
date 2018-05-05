

weight = [6, 3, 4, 2]
value = [30, 14, 16, 9]

def knapsackSingleItems(weightList, value, n, i, weight):

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


print(knapsackSingleItems(weight, value, len(weight), 0, 10))
print(knapsackMultipleItems(weight, value, len(weight), 0, 10))
