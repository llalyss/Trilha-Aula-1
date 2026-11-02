valores = input().split()

numeros = [int(valores[0]), int(valores[1]), int(valores[2])]
ordenados = sorted(numeros)

for numero in ordenados:
    print(numero)

print()

for numero in numeros:
    print(numero)