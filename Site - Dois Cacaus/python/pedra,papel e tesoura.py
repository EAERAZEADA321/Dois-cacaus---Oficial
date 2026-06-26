print("===Escolha uma opção para vencer ou perder===")
print("===1-Tesoura===")
print("===2-Pedra===")
print("===3-Papel===")
escolha = int(input(""))

import random


if escolha == 1 :
    escolhamaq = random.randint (1, 3)
    if escolhamaq == 1:
        print("Ambos escolheram tesoura:")
        print("Empate")
    elif escolhamaq == 2:
        print("Voce escolheu tesoura e ele pedra:")
        print("Voce perdeu!!")
    else:
        print("Voce escolheu tesoura e ele papel:")
        print("Voce ganhou!!")
elif escolha == 2 :
    escolhamaq = random.randint (1, 3)
    if escolhamaq == 2:
        print("Ambos escolheram pedra:")
        print("Empate")
    elif escolhamaq == 1:
        print("Voce escolheu pedra e ele tesoura:")
        print("Voce ganhou!!")
    else:
        print("Voce escolheu pedra e ele papel:")
        print("Voce perdeu!!")
elif escolha == 3 :
    escolhamaq = random.randint (1, 3)
    if escolhamaq == 3:
        print("Ambos escolheram papel:")
        print("Empate")
    elif escolhamaq == 2:
        print("Voce escolheu papel e ele pedra:")
        print("Voce ganhou!!")
    else:
        print("Voce escolheu pedra e ele tesoura:")
        print("Voce perdeu!!")
else:
    print("Não Existe outra opção")