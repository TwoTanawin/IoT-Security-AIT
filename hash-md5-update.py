import hashlib

# String to be hashed
data = "Hello, world!"

# Create an MD5 hash object
hash_object = hashlib.md5()

# Update the hash object with the bytes-like object
hash_object.update(data.encode('utf-8'))

# Additional data
additional_data = "This is additional data."

# Update the hash object with additional data
hash_object.update(additional_data.encode('utf-8'))

# Get the hexadecimal representation of the updated hash
md5_hash = hash_object.hexdigest()

print("Updated MD5 Hash:", md5_hash)
print(f'size digest_size: {hash_object.digest_size}')
print(f'size block_size: {hash_object.block_size}')
