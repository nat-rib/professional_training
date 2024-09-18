# A vulnerabilidade 

    A vulnerabilidade encontrada é do tipo RCE - Remote Code Execution.

    Essa vulnerabilidade se aproveita da possibilidade do pickle de serializar e deserializar mais do que apenas objetos python.


## Pickle

Pickle é uma biblioteca python que consegue serializar e deserializar objetos em Python. 

O processo de pickling converte um objeto para um stream de bytes, é um processo alternativo de serialização.

Pickle é uma mini linguagem usada para converter um python object para um stream de bytes


Fonte: https://davidhamann.de/2020/04/05/exploiting-python-pickle/

https://dan.lousqui.fr/explaining-and-exploiting-deserialization-vulnerability-with-python-en.html
