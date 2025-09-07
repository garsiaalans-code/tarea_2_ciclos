numero = int(input("ingresa un número entero: "))
num = abs(numero)
invertido = 0
while num > 0:
    digito = num % 10      
    invertido = invertido * 10 + digito  
    num = num // 10           
if numero < 0:
    invertido = -invertido
print(f"número invertido: {invertido}")
