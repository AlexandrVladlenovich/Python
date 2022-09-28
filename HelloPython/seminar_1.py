# -*- coding: utf-8 -*-
# 1 задача
a = int(input("Введите первое число"))
b = int(input("Введите второе число"))
if a ** 2 == b:
    print('Да')
elif b ** 2 == a:
    print('Да')
else:
    print('Нет')

# 2 задача (1 вариант)
m = int(input())
for i in range(4):
    x = int(input())
    if x > m:
        m = x
print(m)

# 2 задача (2 вариант)
sp = list()
for i in range(5):
    x = int(input())
    sp.append(x)
print(max(sp))

# 3 задача
n = int(input())
for i in range(-n, n + 1):
    print(i, end=' ')

# 4 задача
n = int(input())
if n == int(n):
    print('нет')
else:
    print(int(n * 10) % 10)

# 5 задача
n = int(input())
if (n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('кратно')
else:
    print('нет')