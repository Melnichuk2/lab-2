#Мастям гральних карт присвоєно порядкові номери: 1 - піки, 2 - трефи, 3 - бубни, 4 - черви.
#Вартості карт, які старші за десятку, привласнені номери: 11 - валет, 12 - дама, 13 - король, 14 - туз. 
#Дано два цілих числа: N - вартість (6 ≤ N ≤ 14) і M - масть карти (1 ≤ M ≤ 4). Вивести назву 
#відповідної карти виду «шістка бубон», «дама черв», «туз треф», тощо.





N,M = map(int,input().split())

s1 = ''
s2 = ''
if M == 1:
    s1 ='треф'
if M == 2:
    s1 = 'бубней'
if M == 3:
    s1 = 'червей'
if M == 4:
    s1 = 'пик'

if N ==1:
    s2 ='шесть'
if N ==2:
    s2 ='семь'
if N == 3:
    s2 = 'восемь'
if N == 4:
    s2 = 'девять'
if N == 5:
    s2 = 'десять'
if N ==6:
    s2 ='валет'
if N ==7:
    s2 ='дама'
if N ==8:
    s2 ='корль'
if N ==9:
    s2 ='туз'

s =' это '+s2+' '+s1
print(s)