s1 = 'Blockaabbcc'
s2 = s1.upper()

print('s1 : ' + s1)
print('s2 : ' + s2)

s3 = 'amazing value'
s3 = s3.upper()

print('s3 : ' + s3)

s4 = 'abcd 1234,.;///blog'
print('s4 : ' + s4.upper())

s1 = 'BlockABCD'
s2 = s1.lower()

print('s2 : ' + s2)

s3 = '하이. P y T h O n !'
for i in s3:
    print('\'{0}\'는 대문자? : {1}'.format(i, i.isupper()))

s3 = 'a B 2 $%'
for i in s3:
    print('\'{0}\'는 소문자? : {1}'.format(i, i.islower()))
