from Crypto.Util.number import inverse

a=0
p=17
x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))


if  (x1==x2) and (y1==y2):
    s=((3*pow(x1,2)+a)*inverse((2*y1),p)) % p
else:
    s=((y2-y1)*inverse((x2-x1),p)) % p

print(s)
x3=(pow(s,2)-x1-x2) % p
y3=(s*(x1-x3)-y1 )% p

print("(",x3,",",y3,")")