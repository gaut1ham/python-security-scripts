import hashlib

text = input("Enter text to hash: ")

hashed = hashlib.sha256(text.encode()).hexdigest()

print("SHA-256 Hash:")
print(hashed)

