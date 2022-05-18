
#4. Для даного дійсного x знайти значення наступної функції f, що приймає дійсні значення:
#f (x) = 2 • sin (x), якщо x> 0; 6 - x, якщо x ≤ 0.




import math


x =int(input())
if x >0:
    print(math.sin(x)*2)
else:
    print(6 -x)



