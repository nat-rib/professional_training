# A vulnerabilidade

Essa é uma vulnerabilidade dupla, um SSRF + LFI. 

## SSRF (Server-Side Request Forgery)

Esse tipo de ataque acontece quando uma aplicação que tem requisições para outras aplicações ou servidores e um atacante consegue manipular essas requisições, ou seja, acontece quando sistemas que não deveriam ser acessados via web estão expostos. Isso acontece principalmente por falta de sanitização e por gestão inadequada de acessos. 

## LFI (Local File Inclusion)

Esse tipo de ataque se aproveita da vulnerabilidade do servidor para rodar comando a fim de ler ou rodar arquivos, normalmente acontece com aplicações que usam um URL para arquivo como input.


## Por que esse código é vulnerável? 

O exemplo estudado é vulnerável a SSRF pois ele não faz a sanitização da entrada fornecida pelo usuário, ou seja, um atacante pode enviar uma URL apontando para o próprio servidor, como http://localhost:5000

    ```python3
        response = requests.get(url, allow_redirects=False)
    ```

E ele também é vulnerável a LFI pois ele aceita URLs que começam com file://

    ```python3
        url = request.args.get('url')
        if url:
            try:
                if url.startswith('file:///'):
                    file_path = url[7:]  # Remove "file:///" prefix
                    if os.path.exists(file_path):
                        file_content = open(file_path, 'r').read()
    ```

Fontes: 

https://github.com/bl4de/ctf/blob/master/2017/ASIS_CTF_2017/Golem/Golem_Web_writeup.md