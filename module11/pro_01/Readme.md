# A vulnerabilidade

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


# Internal vs External DTD

Um Internal DTD é quando a custom tag é especificada refereciando somente elementos do próprio XML, ela é encapsulada dentro da tag <!DOCTYPE>. Exemplo: 

```xml
<!DOCTYPE root_element[ <!ELEMENT element_name (element_content)>
<!ELEMENT another_element_name (another_element_content)>
]>
```

Um External DTD é quando está fora do XML que ele vai atuar, pode estar em um arquivo separado ou via URL. Com um DTD Externo é possível que vários outos XML usem da mesma regra especificada no DTD externo. Exemplo: 

```xml
<!DOCTYPE root_element SYSTEM "DTD_file_name">
```

Fonte: 

https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity

https://gosecure.github.io/xxe-workshop/#4