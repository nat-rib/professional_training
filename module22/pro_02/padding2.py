from padding_oracle import decrypt, base64_encode, base64_decode
import requests

sess = requests.Session()  # Uses connection pooling
url = 'http://localhost:8085'

def oracle(ciphertext: bytes):
    response = sess.get(url, params={'token': base64_encode(ciphertext)})
    if 'failed' in response.text:
        return False  # Token decryption failed
    elif 'success' in response.text:
        return True
    else:
        raise RuntimeError('Unexpected behavior')

ciphertext = base64_decode('M9I2K9mZxzRUvyMkFRebeQzrCaMta83eAE72lMxzg94=')
assert len(ciphertext) % 16 == 0

plaintext = decrypt(
    ciphertext,
    block_size=16,
    oracle=oracle,
    num_threads=16
)

print(plaintext.decode())