def test(arr):
    arr[0][0] = 100
    return arr

arr = [[1,2,3],[4,5,6]]
arr = test(arr)
print(arr)