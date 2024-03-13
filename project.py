import math

p = float(input("Enter initial investment: ")) #initial investment
r = float(input("Enter index fund invested in, or percentage gained: ")) #rate
nasdaq = (13.8)
sandp500 = (10.2)
dowjones = (8.7)
r /= 1200
t = int(input("Enter years until retirement: ")) #years
t *= 12
mc = float(input("Enter monthly contribution: "))
a = float(p)
e = 2.71828182846

while t != 0:
   
     a = (a + mc)*((e)**r); t-=1




print(a)