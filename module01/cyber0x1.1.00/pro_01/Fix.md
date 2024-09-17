uma maneira de previnir esse tipo de ataque é fazer as APIs usarem tokens que são enviados junto com o payload para autenticar as requisições. exemplo: 

```
<form action="/transfer.do" method="post">
<input type="hidden" name="CSRFToken" value="OWY4NmQwODE4ODRjN2Q2NTlhMmZlYWEwYzU1YWQwMTVhM2JmNGYxYjJiMGI4MjJjZDE1ZDZMGYwMGEwOA==">
[...]
</form>
```

outra maneira de previnir seria usando um atribuito chamando SameSite nos cookies, esse atributo garante que o browser não inclui os cookies em outras requisições geradas por outros sites. Exemplo: 

```
const sessionConfig = {
  secret: 'pjwq09!@#jmx',
  name: 'saturnbank',
  resave: false,
  saveUninitialized: false,
  store: store,
  cookie : {
    sameSite: 'strict',
  }
};
```

fonte: https://learn.snyk.io/lesson/csrf-attack/
