



payload = pickle.dumps(b'cat /etc/passwd')

encoded_payload = base64.urlsafe_b64encode(payload).decode()

print(encoded_payload)


gASVEwAAAAAAAABDD2NhdCAvZXRjL3Bhc3N3ZJQu