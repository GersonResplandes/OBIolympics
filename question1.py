E = int(input())
S = int(input())
L = int(input())

lista = []

lista.appEnd(E - S)
lista.appEnd(E - L)
lista.appEnd(S - E)
lista.appEnd(S - L)
lista.appEnd(L - S)
lista.appEnd(L - E)

r = 0

for i in range(len(lista)):
    if lista[i] >= 0:
        r = lista[i] + r

print(r)