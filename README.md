# Validador de CPF

Programa em Python que verifica se um CPF é válido, calculando os dois dígitos verificadores pela regra oficial.

## Como funciona

O CPF tem 11 dígitos, e os dois últimos são verificadores, calculados a partir dos 9 primeiros:

1. Cada um dos 9 primeiros dígitos é multiplicado por um peso, que começa em 10 e diminui a cada passo.
2. A soma é multiplicada por 10, e o resto da divisão por 11 define o primeiro dígito verificador (resto 10 vira 0).
3. O segundo dígito segue a mesma regra, usando os 9 primeiros dígitos mais o primeiro verificador, com pesos de 11 a 2.

Também são rejeitadas as sequências com todos os dígitos iguais (como `11111111111`), que passam no cálculo mas não são CPFs válidos.

## Requisitos

- Python 3.6 ou superior (usa f-strings)

## Como executar

```bash
python validar_cpf.py
```

Digite o CPF quando o programa pedir, somente com números:

```
Escreva seu CPF: 74682489070
Primeiro dígito: 7
Segundo dígito: 0
O seu cpf 74682489070 está Valido!
Fim do Programa.
```

## Observações

- A entrada deve conter apenas números, sem pontos ou traço.
- O programa valida o formato e os dígitos verificadores, mas não consulta a Receita Federal, então não confirma se o CPF pertence a alguém.
- No Linux ou macOS, troque `os.system('cls')` por `os.system('clear')`.

## Licença

Uso livre para estudo.
