A = int(input())
B = int(input())
C = int(input())
D = int(input())

possivel = False
for doses in range(0, C // D + 1):
    cafe = doses * D
    leite = C - cafe
    if A <= leite <= B:
        possivel = True
        break

print('S' if possivel else 'N')