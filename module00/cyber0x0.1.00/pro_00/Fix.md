Devemos sempre sanitizar as entradas do sistema, principalmente em casos de text box com valores abertos, uma das formas possíveis são:

1) usar escape() para trocar caracteres especiais por valores HTMLs correspondentes. Exemplo: 

    document.getElementById('cookieOutput').innerHTML = document.cookie

    com escape() vira: 

    document.getElementById%28%27cookieOutput%27%29.innetHTML%20%3D%20document.cookie

dessa forma impede o comando de ser executado.

2) usar trim() para retirar espaços vazios do input

3) usar replace()