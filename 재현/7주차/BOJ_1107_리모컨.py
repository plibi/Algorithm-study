# 소요시간 : 30분 이상
# 새롭게 알게 된 내용: 브루트포스로 접근하는 방법이 더 좋을 수도 있다.
# n과 가장 가까운 수를 찾는 과정에서 논리적으로 경우의 수를 나눠 찾으려면 복잡해짐.
# n의 범위 안에서 그냥 반복문을 돌려서 찾아낸다.

state = 100
n = int(input())
m = int(input())

if m:
    broken = [int(i) for i in input().split()]
else:
    broken = []

usable = list(set(range(10)) - set(broken))
if n == state:
    print(0)
else:

    # n과 가장 가까운수를 찾는다 
    result = abs(n-state)
    for i in range(1000001):
        for j in str(i):
            if int(j) not in usable:
                # print('if', 'i:', i, 'j:', j)
                break
        else:
            # +,-로만 움직여서 n으로 가는 버튼횟수와 n과 가장 가까운 채널로 이동한뒤 +,-로 움직여서 n으로 가는 횟수를 비교해 더 적은 쪽 선택
            result = min(result, abs(n-i)+len(str(i)))
            # print('else i:', i)
            # print(result)
    print(result)
    

