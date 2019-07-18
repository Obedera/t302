import random
lista = []
i = 0

while i<20:
    lista.append(random.randrange(0, 100))
    i+=1

def verificar_maior(vetor):
    valormax = vetor[0]
    for l in vetor:
        if l>valormax:
            valormax = l
    return valormax

def maior_valor(vetor):
    return max(vetor, key=int)

print(f'Lista {lista} valormax {verificar_maior(lista)} valormax phyton{maior_valor(lista)}')