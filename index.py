'''SISTEMA BANCÁRIO DIGITAL

Imaginem que foram contratados por um banco para desenvolver um pequeno sistema bancário.

Cada utilizador começa com um saldo inicial de 50.000 Kz.

O vosso trabalho é desenvolver a lógica de funcionamento deste sistema.

1. O sistema deverá apresentar o seguinte menu:

BANCO DIGITAL 

1 - Consultar saldo
2 - Levantar dinheiro
3 - Depositar dinheiro
4 - Sair

Escolha uma opção:

2. Regras de funcionamento:

- Consultar saldo: apresentar o saldo atual.

- Levantar dinheiro: solicitar um valor e verificar se existe saldo suficiente.

- Depositar dinheiro: adicionar o valor ao saldo.

- Sair: terminar o programa.

3. Regras adicionais:

- Não permitir levantamentos superiores ao saldo disponível.

- Não permitir depósitos ou levantamentos com valores negativos ou iguais a zero.

- Não aceitar opções inexistentes.

- Depois de cada operação, o menu deverá voltar a aparecer, exceto quando o utilizador escolher sair.

 OBJECTIVO:

Demonstrar que conseguem trabalhar com:

- Variáveis.
- Condições (if/else).
- Ciclos (while).
- Operadores matemáticos.
- Entrada e saída de dados.

 ATENÇÃO:

Não queremos apenas código. Queremos compreender o raciocínio por trás de cada decisão.

Podem utilizar pseudocódigo ou fluxograma para representar a solução.

Para apresentar amanhã as 19h engenheiros

Boa sorte a todos!'''
import json

utilizadores = [{'nome': 'Feliciana', 'senha': 1234}, {'nome': 'Adão', 'senha': '2345'}]

nome = input('Digite o seu nome de usuário')
palavra_passe = int(input('Digite a sua senha'))