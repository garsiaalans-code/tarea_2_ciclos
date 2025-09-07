n = int(input("Ingresa un número entero positivo: "))
suma_pares = sum(i for i in range(1, n + 1) if i % 2 == 0)
suma_impares = sum(i for i in range(1, n + 1) if i % 2 != 0)
print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")

