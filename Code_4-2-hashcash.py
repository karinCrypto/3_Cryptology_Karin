from hashlib import sha256 as sha

def hashcash(msg, difficulty):
    nonce = 0
    print('+++ Start')
    while True:
        target = '%s%d' %(msg, nonce)
        ret = sha(target.encode()).hexdigest()

        if ret[:difficulty] == '0'*difficulty:
            print('+++ Bingo')
            print('--->', ret)
            print('---> NONCE=%d' %nonce)
            break

        nonce += 1


def main():
    msg = 'Attack at 9PM!'
    difficulty = 2
    hashcash(msg, difficulty)


main()
