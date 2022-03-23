# Binary search
# arr, target, start point, end point 필요
# arr는 정렬되어 있어야 함

## 재귀함수를 통한 구현
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


## 반복문을 이용한 구현
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


## 파이썬 라이브러리 bisect
## bisect_left(arr, x) : 정렬된 순서를 유지하며 arr에 x를 삽일할 가장 왼쪽 인덱스 반환
from bisect import bisect_left, bisect_right

arr = [1, 2, 4, 4, 5, 7, 9]
x = 4
print('?', bisect_left(arr, 4))
print(bisect_right(arr, 4))

### 값이 특정 범위에 속하는 데이터 개수 구하기
from bisect import bisect_left, bisect_right

arr = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

### 값이 4인 데이터 개수 print
print(bisect_right(arr, 4) - bisect_left(arr, 4))
### 값이 [-1, 5]범위에 있는 데이터 개수 print
print(bisect_right(arr, -1) - bisect_left(arr, 5))


# Parametric Search
# 최적화 문제를 결정문제(yes or no)로 바꾸어 해결하는 방법
# 백준 나무자르기