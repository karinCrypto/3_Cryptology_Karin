import hashlib

str = "test"
print(hashlib.sha256(str.encode()).hexdigest())
