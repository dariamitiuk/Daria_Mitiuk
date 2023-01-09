from itertools import *
def nextBigger(number):
    arr, number = [], str(number)
    for i in permutations(number):
        arr.append(int(''.join(i)))
    if len(number) > 1 and int(number) != sorted(arr)[-1]:
        result = sorted(arr)[sorted(arr).index(int(number)) + 1]
    else: return -1
    if result > int(number): return result
    else: return -1

if __name__ == '__main__':
    print("nextBigger(12) -> ", nextBigger(12))
    print("nextBigger(2017) -> ", nextBigger(2017))