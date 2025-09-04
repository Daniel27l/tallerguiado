alcancia = [10, 50, 200,]
meta = 1000

total =sum(alcancia)

if total >= meta:
    print("¡Felicidades! Has alcanzado tu meta de ahorro.")
else:
    falta =meta - total
    print(f"Te faltan {falta} pesos para alcanzar tu meta de ahorro.")

