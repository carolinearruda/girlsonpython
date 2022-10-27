#armazene quatro notas em uma lista e uma lista com o nome dos alunos

notas=[]
alunos=[]

notas.append(float(input("Nota 1:")))
notas.append(float(input("Nota 2:")))
notas.append(float(input("Nota 3:")))
notas.append(float(input("Nota 4:")))
print(notas)

alunos.append(input("Aluno 1:"))
alunos.append(input("Aluno 2:"))
alunos.append(input("Aluno 3:"))
alunos.append(input("Aluno 4:"))
print(alunos)

#apresente a média final e o nome do aluno.
media=sum(notas)/len(notas)
print(f"A média é {media}")


#caso a média seja igual ou superior a 7, apresentar a mensagem 'APROVADO' e 'REPROVADO'.
if media >= 7:
    print("APROVADO")
else:
    print("REPROVADO")

#ordene o nome dos alunos 
alunos.sort()
print(alunos)

#conte quantos alunos tiraram a mesma nota
print(notas.count(5))
