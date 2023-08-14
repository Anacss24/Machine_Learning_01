# Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = []

def encontrar_primos(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True



for num in numeros:
    if encontrar_primos(num):
        primos.append(num)

print(primos)
