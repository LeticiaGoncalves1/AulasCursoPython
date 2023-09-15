from time import sleep

print ('Contagem regressiva para os fogos de artifício estourarem!')
for contagem in range (10, -1, -1):
    print (contagem)
    sleep (0.4)

for c in range (4):
    sleep (0.5)
    print ('POW 💥 ', end='')
    print ('BOM 💥 ', end='')
