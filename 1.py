def trans(numb, sist):
    digit = ''
    while numb != 0:
        digit = str(numb % sist) + digit
        numb //= sist
    if len(digit) % 4 != 0:
        digit = ((len(digit) // 4 + 1) * 4 - len(digit)) * '0' + digit
    return digit

try:
    numb = int(input('Введите число: '))
    sist = int(input('Введите целевую систему счисления: '))
    while sist != 2 and sist != 8:
         print('Выберете либо 2-ичную систему счисления, либо 8-ичную')
         sist = int(input())
    print(trans(numb, sist))
except ValueError:
    print('Это не число. Введите число.')