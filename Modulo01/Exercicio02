# Escreva um programa que leia números digitados pelo usuário e pare quando o número 0 for digitado. No final, imprima a média dos números digitados

numeros = []
numero = float(input("Digite um número ou 0 para sair: "))
while not numero == 0:
  numeros.append(numero)
  numero = float(input("Digite outro número ou 0 par sair: "))

numeros_ordenados = sorted(numeros)
media = sum(numeros_ordenados) / len(numeros_ordenados)

print(f"A média dos números digitados é: {media}")