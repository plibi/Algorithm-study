#list의 sort메소드, 파이썬의 내장함수 sorted의 시간복잡도 nlogn
#quick sort를 사용해보았지만 메모리 초과
#계수 정렬 사용-> 시간복잡도 n + K(원소 중 가장 큰 값)

import sys
num = int(sys.stdin.readline())

check_list = [0] * 10001               #최대 1만의 숫자까지 입력이 되기 때문에 10000이 입력되었을 때 index값으로 10000을 입력하기 위해서 10001개

for i in range(num):
    n = int(sys.stdin.readline())      #입력되는 수를 check_list에 저장
    check_list[n] += 1

for i in range(10001):
    for _ in range(check_list[i]):     #check_list를 끝까지 돌면서 인덱스 값이 몇번 입력되었는지 반복해서 프린트
        print(i)