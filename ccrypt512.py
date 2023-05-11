import hashlib, base64

SHUFFLE_SHA512_INDICES = [
  42, 21,  0,     1, 43, 22,    23,  2, 44,    45, 24,  3,     4, 46, 25,
  26,  5, 47,    48, 27,  6,     7, 49, 28,    29,  8, 50,    51, 30,  9,
  10, 52, 31,    32, 11, 53,    54, 33, 12,    13, 55, 34,    35, 14, 56,
  57, 36, 15,    16, 58, 37,    38, 17, 59,    60, 39, 18,    19, 61, 40,
  41, 20, 62,    63
]

def shuffle_sha512(data):
  return bytes(data[i] for i in SHUFFLE_SHA512_INDICES)

def extend_by_repeat(data, length):
  return (data * (length // len(data) + 1))[:length]

CUSTOM_ALPHABET = './0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

'''  Base64 encode based on SECTION 22.e)
'''
def custom_b64encode(data, alphabet = CUSTOM_ALPHABET):
  buffer,count,result = 0,0,[]
  for byte in data:
    buffer |= byte << count
    count += 8
    while count >= 6:
      result.append(buffer & 0x3f)
      buffer >>= 6
      count -= 6
  if count > 0:
    result.append(buffer)
  return ''.join(alphabet[idx] for idx in result)

'''  From http://www.akkadia.org/drepper/SHA-crypt.txt
'''
def sha512_crypt(password, salt, rounds_in = None):
  rounds,rounds_defined = 5000, False
  if rounds_in is not None:
    rounds,rounds_defined = rounds_in, True

  assert 1000 <= rounds <= 999999999
  hash = hashlib.sha512
  salt_prefix = '$6$'
  password = password.encode('utf8')
  salt = salt.encode('ascii')[:16]


  A = hash()             # SECTION 1.
  A.update(password)     # SECTION 2.
  A.update(salt)         # SECTION 3.

  B = hash()             # SECTION 4.
  B.update(password)     # SECTION 5.
  B.update(salt)         # SECTION 6.
  B.update(password)     # SECTION 7.
  digestB = B.digest();  # SECTION 8.

  A.update(extend_by_repeat(digestB, len(password)))  # SECTION 9., 10.

  # SECTION 11.
  i = len(password)
  while i > 0:
    if i & 1:
      A.update(digestB)   # SECTION 11.a)
    else:
      A.update(password)  # SECTION 11.b)
    i = i >> 1

  digestA = A.digest()    # SECTION 12.

  DP = hash()             # SECTION 13.
  # SECTION 14.
  for _ in range(len(password)):
    DP.update(password)

  digestDP = DP.digest()  # SECTION 15.

  P = extend_by_repeat(digestDP, len(password))  # SECTION 16.a), 16.b)

  DS = hash()             # SECTION 17.
  # SECTION 18.
  for _ in range(16 + digestA[0]):
    DS.update(salt)

  digestDS = DS.digest()  # SECTION 19.

  S = extend_by_repeat(digestDS, len(salt))      # SECTION 20.a), 20.b)

  # SECTION 21.
  digest_iteration_AC = digestA
  for i in range(rounds):
    C = hash()                        # SECTION 21.a)
    if i % 2:
      C.update(P)                     # SECTION 21.b)
    else:
      C.update(digest_iteration_AC)   # SECTION 21.c)
    if i % 3:
      C.update(S)                     # SECTION 21.d)
    if i % 7:
      C.update(P)                     # SECTION 21.e)
    if i % 2:
      C.update(digest_iteration_AC)   # SECTION 21.f)
    else:
      C.update(P)                     # SECTION 21.g)

    digest_iteration_AC = C.digest()  # SECTION 21.h)

  shuffled_digest = shuffle_sha512(digest_iteration_AC)


  prefix = salt_prefix   # SECTION 22.a)

  # SECTION 22.b)
  if rounds_defined:
    prefix += 'rounds={0}$'.format(rounds_in)


  return (prefix
    + salt.decode('ascii')               # SECTION 22.c)
    + '$'                                # SECTION 22.d)
    + custom_b64encode(shuffled_digest)  # SECTION 22.e)
  )

#actual = sha512_crypt('password', 'salt1234')
#expected = '$6$salt1234$Zr07alHmuONZlfKILiGKKULQZaBG6Qmf5smHCNH35KnciTapZ7dItwaCv5SKZ1xH9ydG59SCgkdtsTqVWGhk81'

#print(actual)
#print(expected)
#assert actual == expected
