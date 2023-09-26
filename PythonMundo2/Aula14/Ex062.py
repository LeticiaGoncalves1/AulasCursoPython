print(' --- Gerador de P.A --- ')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

termo = primeiro
contador = 1

while contador <= 10:
    print (f'{termo} → ', end = '')
    termo = termo + razao
    contador = contador + 1
print ('Pausa')
mais = int(input('Quantos termos deseja mostrar a mais? '))
if mais == 0:
    print ('Fim do programa')
    break
else:
    continue