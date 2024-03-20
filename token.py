import secrets

# Generate a token with 32 bytes length (256 bits)
token = secrets.token_hex(32)
print("Generated Token:", token)
