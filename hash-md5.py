import hashlib

# String to be hashed
data = "Hello, world!"

# Create an MD5 hash object
hash_object = hashlib.md5()

# Update the hash object with the bytes-like object
hash_object.update(data.encode('utf-8'))

# Get the hexadecimal representation of the hash
md5_hash = hash_object.hexdigest()

print("MD5 Hash:", md5_hash)
