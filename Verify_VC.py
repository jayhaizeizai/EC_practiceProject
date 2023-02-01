from EC_Point import EC_Point
from EC_Point_Add import EC_Point_Add
from EC_Point_Mul import EC_Point_Mul
from modular_sqrt import modular_sqrt
from check_ECDSA_Signature import check_ECDSA_Signature
import hashlib
import time
import json
from jwcrypto.common import base64url_decode, json_decode

input_file = open("input.json")
input_str = input_file.read()
input_json = json.loads (input_str)

public_key = input_json['public_key'][4:68] #What we get is an uncompressed public key, while we need put compressed public key into check_ECDSA_Signature, a convert is done here
print('public_key: ',public_key)

req_params = input_json['req_params']

header, claims, signMsg = req_params.split(".")

parsed_header = json_decode(base64url_decode(header))

parsed_claims = json_decode(base64url_decode(claims))

raw_signature = base64url_decode(signMsg)
r = int.from_bytes(raw_signature[:32], 'big')
print('r: ', r)
s = int.from_bytes(raw_signature[32:64], 'big')
print('s: ', s)

msg = header + "." + claims
msg_hash = hashlib.sha256(msg.encode()).digest()
hashBytes = int.from_bytes(msg_hash, 'big')
print("msg_hash_hex: ", msg_hash.hex())

if check_ECDSA_Signature(hashBytes,r,s,int(public_key,16)) :
    print("Verification Pass")
