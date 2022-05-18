#14. Дано три різних числа. Знайти, яке з них є середнім (більше одного, але менше іншого).

print('Введите числа = ')
a = int(input())
b = int(input())
c = int(input())

if b < a < c or c < a < b:
    print (' среднее  = ',a)
elif a < b < c or c < b < a:
    print('cpеднее ',b )
else:
    print('среднее =',c)
