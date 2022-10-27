km=float(input("Inserir distância em quilômetro:"))
m=km*1000
cm=km*100000

def ImprimirKm (km):
    print(km, "quilômetros são", m, "metros e", cm, "centímetros")

ImprimirKm (km)