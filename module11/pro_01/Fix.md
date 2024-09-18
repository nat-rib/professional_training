
# Maneiras de prevenção

1) Desabilitar a funcionalidade de custom tags XML (DTD - Document Type Definition)

2) Escolher um parser que já possui por default proteções contra esse tipo de vulnerabilidade. 

3) Caso desabilitar totalmente a funcionalidade de DTD, deve-se então restrigir que sejam criados DTDs externamente. 

4) Sempre sanitizar as entradas e saídas da aplicação. 


Fonte:

https://www.linkedin.com/pulse/xxe-attacks-python-django-applications-jerin-jose


https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html


https://security.snyk.io/package/pip/lxml