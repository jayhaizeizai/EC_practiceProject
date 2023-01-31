from EC_Point import EC_Point 
from EC_Config import p,a,b
import math
from Crypto.Util.number import inverse


def Generate_EC_Point_from_x(x):
    y=math.sqrt(inverse(pow(x,3)+a*x+b,p))
    EC_Point_Ans=EC_Point(x,y)
    return EC_Point_Ans

Generate_EC_Point_from_x(2).displayPoint