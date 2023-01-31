from EC_Point import EC_Point
from EC_Point_Add import EC_Point_Add
from EC_Point_Mul import EC_Point_Mul
from modular_sqrt import modular_sqrt

'''
x1=int(input("x1:"))
y1=int(input("y1:"))
x2=int(input("x2:"))
y2=int(input("y2:"))

#Usage of EC point add
EC_Point1=EC_Point(x1,y1)
EC_Point2=EC_Point(x2,y2)

EC_Point3=EC_Point_Add(EC_Point1,EC_Point2)

EC_Point3.displayPoint()

#Usage of EC point multiple integer
d=int(input("d:"))

EC_Point4=EC_Point_Mul(EC_Point1,d)

EC_Point4.displayPoint()
'''

print: modular_sqrt(15,17)

