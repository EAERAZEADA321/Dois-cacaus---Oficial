print("As possiveis operações que podem ser realizadas:")
print("+", "-", "*", "/", "%")

operacao = str(input("Digite a operação requerente:"))
n1 = float(input("Digite a quantidade requerente:"))
n2 = float(input("Digite a quantidade requerente:"))


if operacao == "+":
    soma = n1 + n2
    print ("O resultado final:", soma)
    final = (str(input("Deseja continuar ?(Responda: 'Sim'):")))
    valorfinal = soma

elif operacao == "-":
    subtracao = n1 - n2
    print ("O resultado final:", subtracao)
    final = (str(input("Deseja continuar ?(Responda: 'Sim'):")))
    valorfinal = subtracao

elif operacao == "*":
    multi = n1 * n2
    print ("O resultado final:", multi)
    final = (str(input("Deseja continuar ?(Responda: 'Sim'):")))
    valorfinal = multi

elif operacao == "/":
    divisao = n1 / n2
    print ("O resultado final:", divisao)
    final = (str(input("Deseja continuar ?(Responda: 'Sim'):")))
    valorfinal = divisao

elif operacao == "%":
    porc = (n1 * n2) / 100
    print ("O resultado final:", porc)
    final = (str(input("Deseja continuar?(Responda: 'Sim'): ")))
    valorfinal = porc
else:
    print("Ta querendo oque?")

if final == "Sim":
    operacao2 =(str(input("Escolha a operação desejada:")))
    n3 = (float(input("Informe o numero:")))

    if  operacao2 == "+":
        finalv = valorfinal + n3
        print("O novo valor final é", finalv)
    elif operacao2 == "-":
        finalv = valorfinal - n3
        print("O novo valor final é", finalv)
    elif operacao2 == "*":
        finalv = valorfinal * n3
        print("O novo valor final é", finalv)
    elif operacao2 == "/":
        finalv = valorfinal / n3
        print("O novo valor final é", finalv)
    elif operacao2 == "%":
        finalv = (valorfinal * n3)/100
        print("O novo valor final é", finalv)
    else:
        print("Infelizmente acabou")

else:
    print("Finalizamos")