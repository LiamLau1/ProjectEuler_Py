import random
import math

points = 1000000;
inside = 0;
i = 0;

for i in range(points - 1):
    x = random.random();
    y = random.random();
    a = x*x;
    b = y*y;
    d = math.sqrt(a+b);
    if d <=1 :
        inside = inside +1 ;

pi = 4*inside/points;
print(pi);
