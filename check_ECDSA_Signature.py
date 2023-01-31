from EC_Point import EC_Point
from EC_Point_Add import EC_Point_Add
from EC_Point_Mul import EC_Point_Mul
from EC_Config import a,b,p,EC_Point_G,q
from Generate_EC_Point_from_x import Generate_EC_Point_from_x
from EC_Point_Negative import EC_Point_Negative

def check_ECDSA_Signature(z,r,s,public_key:int):
    if (s==0): return False
    if (s % q==0): return False
    if (r % q==0): return False
    
    EC_Point_publicKey=Generate_EC_Point_from_x(public_key)
    EC_Point_R=Generate_EC_Point_from_x(r)

    # To verify ECDSA, obtain:
    #   zG = z * G, where z is the message and G is a generator of the EC.
    #   rQ = r * Q, where Q.x = public_key.
    #   sR = s * R, where R.x = r.
    # and check that:
    #   zG +/- rQ = +/- sR, or more efficiently that:
    #   (zG +/- rQ).x = sR.x.


    EC_Point_zG=EC_Point_Mul(EC_Point_G,z)
    EC_Point_rPubkey=EC_Point_Mul(EC_Point_publicKey,r)
    EC_Point_sR=EC_Point_Mul(EC_Point_R,s)
    if (EC_Point_Add(EC_Point_zG,EC_Point_rPubkey).x==EC_Point_sR.x): 
        return True
    if (EC_Point_Add(EC_Point_zG,EC_Point_Negative(EC_Point_rPubkey)).x==EC_Point_sR.x): 
        return True
    return False


