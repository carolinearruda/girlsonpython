#Desenvolva um programa que armazene quatros notas em uma lista e que apresente a média final, a maior nota e a menor nota

notas=[]
notas.append(float(input("Nota 1:")))
notas.append(float(input("Nota 2:")))
notas.append(float(input("Nota 3:")))
notas.append(float(input("Nota 4:")))

media=sum(notas)/len(notas)
print(f"a média é {media}")
maiornota=max(notas)
print (f"a maior nota é {maiornota}")
print(f"a nota mais baixa foi {min(notas)}")



