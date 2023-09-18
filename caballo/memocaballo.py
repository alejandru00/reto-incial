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

def contar_movimientos(n):
    # Crear una matriz para almacenar los resultados parciales
    dp = [[0] * 10 for _ in range(n + 1)]

    # Inicializar el caso base
    for i in range(10):
        dp[1][i] = 1

    # Calcular el número de movimientos para n pasos
    for pasos in range(2, n + 1):
        for inicio in range(10):
            for siguiente in movimientos[inicio]:
                dp[pasos][inicio] += dp[pasos - 1][siguiente]

    # Sumar los resultados para n pasos
    total = sum(dp[n])
    return total

n = 33     # Especifica el número de movimientos
total_movements = contar_movimientos(n)
print(f"Total de movimientos para {n} pasos: {total_movements}")
