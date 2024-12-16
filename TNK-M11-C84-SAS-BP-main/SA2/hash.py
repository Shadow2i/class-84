# Import hashlib library
import hashlib

def generateHash(inputString):

    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()
    # Convert the input string to bytes and update the hash object
    hash_object.update(inputString.encode('utf-8'))
    # Get the hexadecimal representation of the hash in hashValue variable
    hashValue = hash_object.hexdigest()
    
    return hashValue


inputString = "Hello, Conver me into a hash."
print("Input String:", inputString)
hashValue = generateHash(inputString)
print("Hash value:", hashValue)
