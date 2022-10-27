#suponha que você tenha uma lista de compras para uma festa de aniversário
'''
lista_festa=["bolo", "salada", "balões", "letreiro", "refrigerante"]
'''
#suponha que o supermercado só tenha produtos com mais de 6 caracteres em seu nome
#imprima lista_festa produtos que atendam a essa condição
#para saber o comprimento de palavra ou lista usar len(palavra) ou len(lista)

'''
for item in lista_festa:
    if len(item) > 6:
        print(item)
'''

#queremos imprimir os últimos 3 itens da nossa lista para saber quais comprar

'''
contador =0
lista_festa.reverse()
while (contador < 3):
       print(lista_festa[contador])
       contador = contador + 1
'''

#faça um programa que peça uma nota, entre zero e dez. mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''
nota = int(input(f"Digite uma nota entre 0 e 10: "))
while nota not in [1,2,3,4,5,6,7,8,9]:
    nota = print("Nota inválida. Favor entrar com um número entre 0 e 10:")
else:
    print(f"Você digitou a nota {nota}")
'''

#faça um programa que leia e valide as seguintes informações:
#nome: maior que 3 caracteres
#idade: entre 0 e 150
#salário: maior que zero
#sexo: f ou m
#estado civil: s, c, v ou d
#use a função len(string) para saber o tamanho do texto

'''
nome = input("Nome: ")
idade = float(input("Idade: "))
salario = float(input("Salário: "))
sexo = input("Sexo - f ou m: ")
estado_civil = input("Estado civil - s, c, v ou d: ")

while len(nome) <= 3:
    nome = input("Informação inválida. Digite seu nome novamente: ")

while (idade <= 0) or (idade >= 150):
    idade = float(input("Informação inválida. Digite sua idade novamente: "))

while (salario<0):
    salario = float(input("Informação inválida. Digite seu salário novamente: "))

while (sexo!= 'f') and (sexo!='m'):
    sexo = input("Informação inválida. Digite seu sexo novamente: ")

while (estado_civil!='s') and (estado_civil!='c') and (estado_civil!='v') and (estado_civil!='d'):
    estado_civil = input("Informação inválida. Digite seu estado civil novamente: ")
'''

#faça um programa que leia 5 números e informe o maior número

lista_numero = []

for numero in range(5): 
    lista_numero.append(input('Digite o número: '))

print ("Maior número da lista é o", max(lista_numero))  

