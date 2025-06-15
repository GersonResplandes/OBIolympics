E = int(input())
S = int(input())
L = int(input())

lista = []

lista.append(E - S)
lista.append(E - L)
lista.append(S - E)
lista.append(S - L)
lista.append(L - S)
lista.append(L - E)

r = 0

for i in range(len(lista)):
    if lista[i] >= 0:
        r = lista[i] + r

print(r)