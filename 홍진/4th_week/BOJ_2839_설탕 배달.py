import sys

num = int(sys.stdin.readline())

cnt = 0
while num >= 0:
    if num % 5 == 0:     #5kg 봉지를 쓰는 것이 봉지의 수를 줄일 수 있는 방법이기 때문에 5로 나누어 떨어지는지 먼저 확인
        cnt += num // 5  #나누어 떨어진다면 몫을 cnt에 더하고 while문 탈출
        break
    num -= 3
    if num < 0:          #num 값이 음수가 될 때까지 안된다면 할 수 없는 것이기 때문에 -1을 대입하고 while문 탈출
        cnt = -1
        break
    cnt += 1

print(cnt)