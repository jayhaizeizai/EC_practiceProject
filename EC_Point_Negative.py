from EC_Point import EC_Point
from EC_Config import p

def EC_Point_Negative(EC_Point_x:EC_Point):
    return EC_Point(EC_Point_x.x,p-EC_Point_x.y)

