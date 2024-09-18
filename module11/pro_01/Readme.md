A vulnerabilidade nesse caso é chamada de: XXE - XEE - XML External Entity

XML suporta a criação de tag custom, um exemplo de tag custom seria: 

```xml
<!DOCTYPE foo [ <!ENTITY myentity "value" > ]>
```

outro exemplo 

```xml
<!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
<data>&example;</data>
```

Quando o comando SYSTEM é usado, é habilitado carregar o conteúdo contido na URL, mas como o parser do XML é executado via server, as URLs contidas em SYSTEM abre portas para carregar conteúdos maliciosos.


A ideia por de trás é explorar a vulnerabilidade do XML parser utilizado pela aplicação.

Para detectar se uma aplicação está vulnerável a esse tipo de ataque temos algumas opções: 

- triggando DNS lookups


Fonte: 

https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity

https://gosecure.github.io/xxe-workshop/#4