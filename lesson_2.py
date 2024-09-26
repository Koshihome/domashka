# задание 1
a, b = input().split()
a = int(a)
b = int(b)
if b == 0:
    print('Ошибка! На ноль делить нельзя')
else:
    c = a / b
    print(c)

# задание 2
sum = float(input())
if sum > 20000:
    sum = (sum + sum * 0.35)
    print(round(sum, 2))
else: print(round(sum, 2))

# задание 3
m = int(input())
if m > 12 or m < 1:
    print('Ошибка!')
else:
    if m == 12 or m == 1 or m == 2:
        print('Зима')
        if m == 12:
            print('Декабрь')
        elif m == 1:
            print('Январь')
        else:
            print('Февраль')
    elif m == 3 or m == 4 or m == 5:
        print('Весна')
        if m == 3:
            print('Март')
        elif m == 4:
            print('Апрель')
        else:
            print('Май')
    elif m == 6 or m == 7 or m == 8:
        print('Лето')
        if m == 6:
            print('Июнь')
        elif m == 7:
            print('Июль')
        else:
            print('Август')
    else:
        print('Осень')
        if m == 9:
            print('Сентябрь')
        elif m == 10:
            print('Октябрь')
        else:
            print('Ноябрь')
