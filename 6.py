#1. Desafio da Paridade
#Crie um programa que leia um número inteiro e informe se ele é par ou ímpar.

#Dica: Utilize o operador % (módulo) para verificar o resto da divisão.

'''
num = int(input("digite um valor:"))
if num % 2 == 0:
    print("Ele é par")
else:
    print("Ele e ímpar")
'''
#2. Desafio da Soma dos Números
#Crie um programa que leia dois números e exiba a soma deles.
'''
num1 = int(input("Digite o valor 1:"))
num2 = int(input("Digite o valor 2:"))
soma = num1 + num2
print(soma)
'''

#3. Desafio da Média
#Solicite ao usuário para digitar três notas de um aluno e calcule a média. Exiba se o aluno foi aprovado ou reprovado, considerando a média mínima de 7.
'''
num1 = int(input("Digite uma nota 1:"))
num2 = int(input("Digite uma nota 2:"))
num3 = int(input("Digite uma nota 3:"))
soma = num1 + num2 + num3
print(soma / 3)
print("Essa é sua nota final!!!")
'''

#4. Desafio da Tabuada
#Crie um programa que exiba a tabuada de um número fornecido pelo usuário.

'''
num = int(input("Digite a tabuada que você quer:"))
mult = num * 1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10
print(mult)
'''

#5. Desafio do Fatorial
#Crie um programa que calcule o fatorial de um número fornecido pelo usuário.
#Fatorial de n (n!) é o produto de todos os números inteiros de 1 até n.
'''
num = int(input("Digite um numero valido para ser fatorado:"))
fato = 1
if num < 0:
    print("Numero invalido!!!")
else:
    for i in range(1, num + 1):
        fato *= i
    print(fato)
'''
#1. Soma de Números Pares
#Crie um programa que some todos os números pares de 1 a 100.
#Dica: Use um loop for e o operador %.
'''
soma = 0 
for i in range(1, 101):
    if i % 2 == 0:
        soma += i 
    print(soma)
'''

#2. Número ao Contrário
#Escreva um programa que leia um número inteiro e exiba ele ao contrário. Por exemplo, se o número for 1234, o programa deve exibir 4321.
#Dica: Use strings para manipular o número.
'''
num = (input("Digite numeros para ser invertido: "))
inverso = num[::-1]
print(inverso)
'''
#3. Contar Vogais
#Crie um programa que leia uma frase e conte quantas vogais (a, e, i, o, u) existem na frase.
'''
frase = input("Digite um frase:")
vogais = 'a e i o u'
contador = 0 

for letra in frase:
    if letra in vogais:
        contador +=1 
print(contador) 
'''
#Oposto
'''
frase = input("Digite um frase:")
consoantes = 'b, c, d, f, g, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z.'
contador = -1 

for letra in frase:
    if letra in consoantes:
        contador +=1 
print(contador) 
'''
#4 Escreva um programa que mostre os números de 1 a 50. Porém:
#Para números divisíveis por 3, exiba "Fizz".
#Para números divisíveis por 5, exiba "Buzz".
#Para números divisíveis por ambos, exiba "FizzBuzz".
'''
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

#5. Números Únicos
#Escreva um programa que remova números duplicados de uma lista e exiba os números únicos.
'''
num = input("Digite numeros: ")
uni = list(set(num))
print(uni)
'''

#7. Soma dos Dígitos
#Crie um programa que leia um número inteiro e calcule a soma dos seus dígitos.
#Dica: Transforme o número em string para iterar sobre seus dígitos.
'''
numero = input("Digite um número: ")
soma = 0
for digito in numero:
    if digito.isdigit():
        soma += int(digito)
    print(soma)
'''
# Resolução provavelmente errada kkkkk odeio python 