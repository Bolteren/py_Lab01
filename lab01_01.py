#Первая лабораторка третий вариант.
#ЮУРГУ ВШЭК 209
 
k = 86.9 ** ( -1/4) + ( 1 /( 2 ** (-0.3))) ** (-1/3)
import math
m = 49 ** ( 1 - math.log10(2)) + 5 ** ( -math.log10(4))
p = 5*k + 3*m*math.log10(3)
if math.fabs(k) > math.fabs(m):
    p = math.sin(p)
else:
    p = math.cos(p)
print(p)
exit()
