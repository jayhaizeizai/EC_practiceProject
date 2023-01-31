from EC_Point import EC_Point 
from EC_Config import p,a,b
import math
from modular_sqrt import modular_sqrt

#Notice that this only return one of the symmetric point pair, another one is (x,p-y)

def Generate_EC_Point_from_x(x):
    y=modular_sqrt(pow(x,3)+a*x+b,p)
    EC_Point_Ans=EC_Point(x,y)
    return EC_Point_Ans

Generate_EC_Point_from_x(10).displayPoint()
