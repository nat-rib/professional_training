
import pickle
import base64

payload = pickle.dumps(b'eval(\"1024 + 1024\")')

encoded_payload = base64.urlsafe_b64encode(payload).decode()

print(encoded_payload)
