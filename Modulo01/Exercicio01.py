# Escreva um programa que solicite ao usuário uma palavra e verifique se ela é um palíndromo (igual ao ler de trás para frente).

palavra = input("Digite uma palavra ")

palavra_invertida = palavra.upper()[:: -1]

if palavra_invertida == palavra.upper():

  print("Essa palavra é um palindromo")
else:
   print("Essa palavra não é um palindromo")
   