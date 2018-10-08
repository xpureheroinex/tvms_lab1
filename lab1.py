import math


def average(arr):
    return sum(arr)/len(arr)


def check_average(arr):
    sum = 0
    for num in arr:
        sum += average(arr) - num
    return int(sum) == 0


def dispersia(arr):
    sum = 0
    for num in arr:
        sum += (num - average(arr))**2
    return sum/(len(arr) - 1)


def standard_deviation(arr):
   return math.sqrt(dispersia(arr))


def median(arr):
    arr = sorted(arr)
    if len(arr) % 2 == 0:
        return (arr[len(arr) // 2] + arr[(len(arr) - 1) // 2]) / 2
    else:
        return arr[(len(arr) - 1) // 2]


def mode(arr):
    count = {}
    for num in arr:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1
    sorted_arr = [(k, count[k]) for k in sorted(count, key=count.get, reverse=True)]
    max = sorted_arr[0][1]
    results = []
    for i in sorted_arr:
        if i[1] == max:
            results.append(i[0])
    return results


def max_value(arr):
    return max(arr)


def min_value(arr):
    return min(arr)


def range_value(arr):
    return max_value(arr) - min_value(arr)


def quantile(arr, ind):

    arr = sorted(arr)
    if ind == 0.5:
        return median(arr)
    else:
        return arr[int(math.ceil(len(arr) * ind)) - 1]


print("divide numbers by coma: ")
arr = [int(x) for x in input().split(',')]


print("sorted numbers: ", sorted(arr), "\naverage: ", average(arr), "\nis average correct: ", check_average(arr),
      "\ndispersia: ", dispersia(arr),
      "\nstandart deviation: ", standard_deviation(arr), "\nmedian: ", median(arr),
      "\nmoda: ", mode(arr), "\nmax, min, range: ", max_value(arr), min_value(arr), range_value(arr),
      "\nquantiles 25, 50, 75, 10: ", quantile(arr, 0.25),
      quantile(arr, 0.50), quantile(arr, 0.75), quantile(arr, 0.10))

