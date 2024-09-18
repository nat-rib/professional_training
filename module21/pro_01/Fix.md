# Formas de prevenção

- Não se deve usar pickle para deserializar objetos que vieram de fontes não confiáveis, nesse caso deve-se usar json.

- Garantir que uma conexão encriptada entre os serviços que usarem pickle. Exemplo 


```python3
SECRET_KEY = b"your secret key here"

obj = [ "test", (1, 2), [ "a", "b" ] ]

data = pickle.dumps(obj)

digest = hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()
```


Fonte: 

https://snyk.io/pt-BR/blog/guide-to-python-pickle/