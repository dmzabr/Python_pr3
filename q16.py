import random


n = int(input('Введите число элементов: '))
targ = int(input('Введите искомое значение: '))
num = []

for i in range(n):
    num.append(random.randint(0,10))
    print(num[i], end = ' ')
    
print(f'\n{num.count(targ)}')
    
