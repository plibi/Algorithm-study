import numpy as np
def solution(arr1, arr2):
    arr11 = np.array(arr1)
    arr22 = np.array(arr2)
    answer = arr11 + arr22
    return answer.tolist()