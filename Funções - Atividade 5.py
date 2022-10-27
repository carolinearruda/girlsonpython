#Desenvolva um programa que tenha uma função que verifique se um número inteiro qualquer é par ou impar
def even_or_odd(number):

    if number % 2 == 0:
        return f'O número {number} é par'
    return f'O número {number} é impar'

number = int(input('Informe um número inteiro qualquer: '))
print(even_or_odd(number))

#Carregue a data atual do computador e apresente somente a data


#Desenvolva um programa que leia um número inteiro qualquer e que apresente o número informado, seguido do seu antecessor e do seu sucessor
'''
numero = int(input('Informe um número inteiro qualquer: '))
print(f'O antecessor do número {numero} é {numero - 1}, e o sucessor é {numero + 1}')
'''

#Format - Substituir os valores de acordo com cada um dos format types
'''
txt = "Nós temos {:<} anos."
print(txt.format(84))

txt = "Nós temos {:>} anos."
print(txt.format(84))

txt = "Nós temos {:^} anos."
print(txt.format(84))

txt = "Nós temos {:=} anos."
print(txt.format(84))

txt = "Nós temos {:+} anos."
print(txt.format(84))

txt = "Nós temos {:-} anos."
print(txt.format(84))

txt = "Nós temos {: } anos."
print(txt.format(84))

txt = "Nós temos {:,} anos."
print(txt.format(84))

txt = "Nós temos {:_} anos."
print(txt.format(84))

txt = "Nós temos {:b} anos."
print(txt.format(84))

txt = "Nós temos {:c} anos."
print(txt.format(84))

txt = "Nós temos {:d} anos."
print(txt.format(84))

txt = "Nós temos {:e} anos."
print(txt.format(84))

txt = "Nós temos {:E} anos."
print(txt.format(84))

txt = "Nós temos {:f} anos."
print(txt.format(84))

txt = "Nós temos {:F} anos."
print(txt.format(84))

txt = "Nós temos {:g} anos."
print(txt.format(84))

txt = "Nós temos {:G} anos."
print(txt.format(84))

txt = "Nós temos {:o} anos."
print(txt.format(84))

txt = "Nós temos {:x} anos."
print(txt.format(84))

txt = "Nós temos {:X} anos."
print(txt.format(84))

txt = "Nós temos {:n} anos."
print(txt.format(84))

txt = "Nós temos {:%} anos."
print(txt.format(84))
'''