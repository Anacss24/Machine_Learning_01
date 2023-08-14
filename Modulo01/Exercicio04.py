# Dada uma lista de strings ['banana', 'maçã', 'laranja', 'abacaxi'], crie uma nova lista com as palavras que têm mais de 5 letras e outra lista com as palavras que terminam com a letra a.


frutas = ['banana', 'maçã', 'laranja', 'abacaxi']
frutas_5_letras = []
frutas_terminadas_com_A = []

for palavra in frutas:
    if len(palavra) > 5:
        frutas_5_letras.append(palavra)
    if palavra[-1] == 'a' or palavra[-1] == 'ã':
        frutas_terminadas_com_A.append(palavra)

print(frutas_5_letras)
print(frutas_terminadas_com_A)