import hashlib
from simplecrypt import encrypt, decrypt

value="Shanan:Hello!"

def SHA256():
    result=hashlib.sha256(value.encode())
    print("sha256 encrypt data:",result.hexdigest())
SHA256()

def MD5():
    result=hashlib.md5(value.encode())
    print("md5 encrypt data:",result.hexdigest())
MD5() 

message="Shanan:hello"
hex_string=""

def encryption():
    global hex_string
    cypher_code=encrypt('aim',message)
    hex_string=cypher_code.hex()
    print("Encryption",hex_string)
    
def decryption():
    global hex_string
    bite_string=bytes.fromhex(hex_string)
    original=decrypt('aim',bite_string)
    finnal_message=original.decode("utf-8")
    print("Decryption",finnal_message)
    
encryption()
decryption()