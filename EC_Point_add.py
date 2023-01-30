from Crypto.Util.number import inverse
from EC_Point import EC_Point
from Config import a,p


def EC_Point_add(EC_Point1:EC_Point,EC_Point2:EC_Point):
    x1=EC_Point1.x
    y1=EC_Point1.y
    x2=EC_Point2.x
    y2=EC_Point2.y
    if  (x1==x2) and (y1==y2):
        s=((3*pow(x1,2)+a)*inverse((2*y1),p)) % p
    else:
        s=((y2-y1)*inverse((x2-x1),p)) % p
    x3=(pow(s,2)-x1-x2) % p
    y3=(s*(x1-x3)-y1 )% p
    EC_Point3=EC_Point(x3,y3)
    return EC_Point3
