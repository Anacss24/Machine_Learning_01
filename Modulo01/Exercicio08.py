#Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

numeros= [10,5,20,30,50,100,58,25]
segundo_maior_valor = []

def segundo_maior(lista):
  maior = max(lista[0], lista[1])
  segundo_maior = min(lista[0], lista[1])

  for numero in lista:
        if numero > maior:
            segundo_maior = maior
            maior = numero
        elif numero > segundo_maior and numero != maior:
            segundo_maior = numero

  return segundo_maior

segundo_maior_valor = segundo_maior(numeros)

print("O segundo maior valor na lista é:", segundo_maior_valor)