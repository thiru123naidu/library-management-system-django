import jwt

MY_SECREATE="nsdjcdjs12344t!@#$%^&*()_++-vfdmngbnfgfgntihtoh"
def jwt_create(payload):
    token = jwt.encode(payload=payload,key=MY_SECREATE, algorithm="HS256")
    return token

#payload = {"rollnumber":25,"password":"thiru"}


def jwt_decode():
    a="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xsbnVtYmVyIjoyNSwicGFzc3dvcmQiOiJ0aGlydSJ9.e9XPoK28FEzXStIHWbdVDlCTLA9nvz4CJihWcRv5ugU"
    decode_data = jwt.decode(a,options={"verify_signature":False})
    print(decode_data)
#jwt_decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoidGhpcnUiLCJyb2xsbnVtYmVyIjoyNSwiZ2VuZGVyIjoibWFsZSJ9.ccLjt0QNBc7H5AuTbiba69aeBZaQFDPU37IOjTPk42A")
#a="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xsbnVtYmVyIjoyNSwicGFzc3dvcmQiOiJ0aGlydSJ9.e9XPoK28FEzXStIHWbdVDlCTLA9nvz4CJihWcRv5ugU"
#jwt_decode()







