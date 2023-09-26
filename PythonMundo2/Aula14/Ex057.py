# Inicializa uma variável 'sexo' como uma string vazia
sexo = ''

# Inicia um loop infinito usando 'while True'
while (True):
    # Solicita que o usuário insira seu sexo ('M' ou 'F') e converte a entrada para maiúsculas
    sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]

    # Verifica se a entrada do usuário é 'M' (masculino)
    if sexo == 'M':
        print (f'Sexo masculino cadastrado com sucesso!')
        # Sai do loop usando 'break' porque o sexo foi cadastrado com sucesso
        break
    # Verifica se a entrada do usuário é 'F' (feminino)
    elif sexo == 'F':
        print (f'Sexo feminino cadastrado com sucesso!')
        # Sai do loop usando 'break' porque o sexo foi cadastrado com sucesso
        break
    else:
        # Se a entrada não for 'M' nem 'F', exibe uma mensagem de comando inválido e continua o loop
        print ('Comando inválido! Digite um sexo válido [M/F]')
        continue
