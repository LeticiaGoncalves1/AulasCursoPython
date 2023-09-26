# Gerador de Progressão Aritmética (P.A).
print(' --- Gerador de P.A --- ')

# Solicita ao usuário que insira o primeiro termo da P.A e a razão da P.A, e converte as entradas para números inteiros.
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

# Inicializa a variável "termo" com o valor do primeiro termo da P.A.
termo = primeiro

# Inicializa a variável "contador" com 1 para rastrear o número de termos impressos.
contador = 1

# Inicia um loop while que continua enquanto o contador for menor ou igual a 10.
while contador <= 10:
    # Imprime o valor atual do "termo".
    print(f'{termo} → ', end='')

    # Atualiza o "termo" adicionando a "razao" a ele, gerando o próximo termo da P.A.
    termo += razao

    # Incrementa o contador em 1 para acompanhar o número de termos impressos.
    contador = contador + 1

# Após o loop while, imprime 'Fim!' para indicar o término do programa.
print('Fim!')
