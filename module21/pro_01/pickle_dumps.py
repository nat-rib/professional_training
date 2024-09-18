
import pickle
import os
import base64
import builtins


payload = pickle.dumps(b'cat /etc/passwd')

encoded_payload = base64.urlsafe_b64encode(payload).decode()

print(encoded_payload)



