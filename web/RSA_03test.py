from hashlib import sha512
from Crypto.PublicKey import RSA
from sympy import nextprime

key_pair = RSA.generate(bits=1024)
m = b'123456'
hash1 = int.from_bytes(sha512(m).digest(), byteorder='big')
# H(m)
n = key_pair.n
e = key_pair.e
d = key_pair.d
p = key_pair.p
q = key_pair.q
# msg
R = nextprime(p)
# gcd(R,m)=1, 随机生成

print("Public key")
print(f'n={hex(n)}')
print(f'e={hex(e)}')
print('Private key')
print(f'N={hex(n)}')
print(f'd={hex(d)}\n')
print(f'p={hex(p)}')
print(f'q={hex(q)}\n')
print(f'hash={hex(hash1)}')


def init():
    return hex(n), hex(e), hex(d), hex(R)


def blindData(msg):
    data = blind(msg)
    signData = sign(data)
    unblindData = unblind(signData)
    return hex(data),hex(signData),hex(unblindData)


def blind(msg):
    # 盲化
    # print(f'msg1111{msg}')
    hash = int.from_bytes(sha512(msg.encode("utf-8")).digest(), byteorder='big')
    print(f'msg hash {hex(hash)}')
    blind_msg = (pow(R, e) * hash) % n
    # R^e*H(m) mod n
    print(f'blind: {hex(blind_msg)}')
    return blind_msg
    # M


def sign(msg):
    # 对M进行签名
    blind_signature = pow(msg, d, n)
    # M^d mod n
    print(f'Blind_signature:\n{hex(blind_signature)}')
    return blind_signature


def unblind(blind_sign):
    # 除盲
    r = pow(R, -1, n)
    # R 的逆元
    unblind_msg = pow(blind_sign * r, 1, n)
    # blind_sign * r mod n
    # H(m)^d mod n
    print(f'Unblind_signature:\n{hex(unblind_msg)}')
    return unblind_msg


def double_Spending():
    # 检测双花
    pass


def verify(sign, msg):
    print(sign,msg)
    # sigma,m
    hash_from_sign = pow(sign, e, n)
    hash = int.from_bytes(sha512(msg.encode("utf-8")).digest(), byteorder='big')
    # sign^e mod n
    # H(m)^d^e mod n == H(m) mod n

    print(f" hash_from_sign {hex(hash_from_sign)}")
    print(f" hash {hex(hash)}")

    if hash == hash_from_sign:
        print('valid')
        return 'valid'
    else:
        print('invalid')
        return 'invalid'

# verify(unblind(sign(blind("123456"))),"123456")
# blind("123456") 盲化
