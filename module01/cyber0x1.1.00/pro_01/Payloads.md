1) primeiro metodo seria aproveitar da vulnerabilidade da api de transfer e executar um post

curl -d amount=10 -XPOST localhost:8080/transfer

2) segundo metodo seria subir uma pagina fake, no caso o index2.html, que contenha um codigo malicioso que quando a vitima acessar vai roubar o saldo da conta 
