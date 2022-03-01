arr = [1, 2, 3, 4, 5]

for _ in range(5):
    max_arr = max(arr)
    while arr[0] != max_arr:
        arr = arr[1:] + [arr[0]]
    print(arr)
    arr = arr[1:]
