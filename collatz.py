pasos=""
co= int(input("Ingrese aquí un número, que no sea cero y que no sea negativo:"))
contador=0
while co != 1:
    contador+=1
    if co % 2 == 0:
        co= (co//2)
        print(co)
    else:
        co= (3 * co)+1
        print(co)

print("pasos:",contador)