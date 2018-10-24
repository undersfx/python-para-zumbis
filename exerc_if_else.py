speed = int(input("Velocidade (em km/h):"))

if speed <= 1:
    print("Tá suave")
else:
    valor = (speed - 1) * 5
    print("Multado em: R$ %5.2f"  %valor)
