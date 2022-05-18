#Дано три числа. Знайти суму двох найбільших з них



a = int(input("a="))
b = int(input("a="))
c = int(input("c="))

if a < b: min = a
else: min= b
if c < min: min = c
s = a+b+c- min

print( 'suma 2 bolshih',s )