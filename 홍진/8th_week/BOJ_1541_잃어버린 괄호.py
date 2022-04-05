import sys

inp = sys.stdin.readline().rstrip()

sep_minus = inp.split('-')

result = 0
if '+' in sep_minus[0]:
    sep_plus = sep_minus[0].split('+')

    sum = 0
    for num in sep_plus:
        sum += int(num)
    result += sum
else:
    result = int(sep_minus[0])

if len(sep_minus) > 1:
    for sep in sep_minus[1:]:
        if '+' in sep:
            sep_plus = sep.split('+')

            sum = 0
            for num in sep_plus:
                sum += int(num)
            result -= sum
        else:
            result -= int(sep)

print(result)
