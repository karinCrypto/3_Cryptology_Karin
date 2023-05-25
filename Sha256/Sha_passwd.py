import hashlib

print("==================================================★ HASH256 ★==================")
put = input("패스워드 입력 : ")
passwd = ''
result = hashlib.sha256(put.encode())
passwd += result.hexdigest()
result = hashlib.sha256(passwd.encode())

print("Start Passwd : ", put)


num = int(input("반복 횟수 : "))
for i in range(1,num+1):
     result = hashlib.sha256(passwd.encode())
     print("\npasswd(%d) : " %i, passwd)
     print("SHA256 : ",result.hexdigest())

     passwd=''
     passwd += result.hexdigest()
