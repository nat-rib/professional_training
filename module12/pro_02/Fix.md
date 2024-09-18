# Métodos de prevenção

- Fazer um whitelist de URLs que podem ser utilizadas baseadas nas permissões do usuário que está mandando

- Sanitizar entradas e saídas

- Não permitir que URLs que não são necessárias sejam utilizadas, exemplo, URLs que comecem com file://, ftp://, ou até mesmo http:// devem ser bloqueadas se possível e deixar apenas as https://

- Habilitar autenticação em todas as chamadas, mesmo em serviços internos

- É recomendável sempre salvar informações sensíveis em um banco de dados e nunca em arquivos no sistema