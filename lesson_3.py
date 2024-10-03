# 1 задание
n = int(input())
sum = 0
b = 1
if n <= 100:
    for i in range(1, n):
        while b <= n:
            sum += b * b
            b += 1
    print(sum)
else: print('Ошибка! Введите число меньшее или равное 100')

# 2 задание
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j, end='\t')
    print()
