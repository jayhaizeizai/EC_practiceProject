from EC_Point import EC_Point
from EC_Point_Add import EC_Point_Add
from Config import a,p

def EC_Point_Mul(EC_Point_P:EC_Point, d):
    if (d==1) :
        return EC_Point_P
    T=EC_Point_Mul(EC_Point_P,d>>1)
    EC_Point_T=EC_Point_Add(T,T)
    if (d%2==1): 
        EC_Point_T = EC_Point_Add(EC_Point_T,EC_Point_P)
    return EC_Point_T
