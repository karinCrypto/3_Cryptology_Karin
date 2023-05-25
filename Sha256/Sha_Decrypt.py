import hashlib

str = """ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
				2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6"""
for i in range(123):
    str = str.replace(hashlib.sha256(chr(i).encode()).hexdigest(), chr(i))
    print(str)
