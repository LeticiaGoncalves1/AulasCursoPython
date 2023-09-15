from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0

for cadastro in range (1, 8):
    nasc = int(input(f'Ano que a {cadastro} pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1

print (f'Ao todo, tivemos {totmaior} pessoas maiores de 21 anos, e {totmenor} pessoas menores de 21 anos.')
