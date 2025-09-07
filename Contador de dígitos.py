numero = int(input("ingresa un número entero "))
num = abs(numero)
digitos = 0
if num == 0:
    digitos = 1
else:
    while num > 0:
        num = num // 10 
        digitos += 1     
print(f"digitos ={digitos} ")
