n = 2 #  numero de pasos

movimientos = {
    0: [6, 4],
    1: [6, 8],
    2: [7, 9],
    3: [4, 8],
    4: [3, 9, 0],
    5: [],
    6: [1, 7, 0],
    7: [2, 6],
    8: [1, 3],
    9: [2, 4]
}


def calcular(inicio, pasos):
    movs = 0
    if pasos:
        for siguiente in movimientos[inicio]:
            movs += 1 + calcular(siguiente, pasos - 1)

    return movs

def totalizar(pasos):
    total = 0
    for i in range(10):
        total += calcular(i, pasos)
    return total

n = 30 #  numero de pasos

totall = (totalizar(n) - totalizar(n-1))
print(totall)

