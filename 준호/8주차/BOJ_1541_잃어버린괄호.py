import sys

input_str = sys.stdin.readline().rstrip()

tmp = input_str

check_2 = True
while check_2:
    if tmp[0] == '0':
        tmp = tmp[1:]
    else:
        check_2 = False

for _ in range(5):
    tmp = tmp.replace('-0', '-')
    tmp = tmp.replace('+0', '+')

check = False
for i, chr in enumerate(input_str):
    if chr=='-':
        check = True
        tmp = tmp.replace('-', ')-(')
        tmp = '('+tmp+')'
        break

print(eval(tmp))
