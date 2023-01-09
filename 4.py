def pairs_count(arr, target):
    counter = 0
    for x in range(len(arr)):
        y = x + 1
        for y in range(y, len(arr)):
            if arr[x] + arr[y] == target: counter += 1
    return counter

if __name__ == '__main__':
    print("pairs_count([1, 3, 6, 2, 2, 0, 4, 5], 5) -> ", pairs_count([1, 3, 6, 2, 2, 0, 4, 5], 5))