
import pickle
import base64

payload = pickle.dumps(b'touch foo.txt \n echo "Algeum passou por aqui" >> foo.txt \n head -n 1 foo.txt')

encoded_payload = base64.urlsafe_b64encode(payload).decode()

print(encoded_payload)