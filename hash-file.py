import hashlib

def calculate_hash(filename):
    """Calculate the hash of a file."""
    md5_hash = hashlib.md5()
    with open(filename, "rb") as file:
        while True:
            chunk = file.read(8192)
            if not chunk:
                break
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def compare_hashes(hash1, hash2):
    """Compare two hash values."""
    print("Hash 1:", hash1)
    print("Hash 2:", hash2)
    return hash1 == hash2

# Example usage:
current_version_hash = calculate_hash("/Users/twomac/Documents/Two/AIT/ISE/Master 2/IoT security/computing/test.py")
expected_version_hash = "333fc272ed93fb65720a559fc9cefaa9"  # Hash of the expected version

if compare_hashes(current_version_hash, expected_version_hash):
    print("Version is correct.")
else:
    print("Version does not match the expected version.")