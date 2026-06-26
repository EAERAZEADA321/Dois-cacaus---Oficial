print("Calculo de nivel da multa")
vel = float(input("Digite a velocidade atingida:"))

if vel <= 80:
    print("Deu sorte não recebe multa")
elif vel <= 100:
    print("Sua multa e de nivel leve")
else:
    print("Sua multa e de nivel grave") 