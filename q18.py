import random


n = int(input('Введите число элементов: '))
targ = int(input('Введите искомое значение: '))
num = []
min = -1

for i in range(n):
    num.append(random.randint(0,10))
    print(num[i], end = ' ')
    
    if min == -1:
        min = num[i]
    
    if (abs(targ - num[i]) < abs(targ - min)):
        min = num[i]
    
print(f"\n{min}")
    
