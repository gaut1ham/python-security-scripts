import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

file1 = input("Enter first file path: ")
file2 = input("Enter second file path: ")

if calculate_hash(file1) == calculate_hash(file2):
    print("Files are identical")
else:
    print("Files have been modified")
