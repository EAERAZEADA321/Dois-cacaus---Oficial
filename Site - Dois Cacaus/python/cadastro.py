print("Sistema de cidades")
print("Selecione uma das opções")
print("1===Cadastrar===")
cad = int(input())

if cad == 1:
    nome = input("Digite seu nome:")
    idade = input("Digite sua idade:")
    cidade = input("DIgite o nome de sua cidade")
    bus = (input("Deseja buscar algum nome? Sim/Não"))
    if bus == "Sim":
        print("Como voce quer procurar")
        nomepes = input("Nome:")
        idadepes = input("Idade:")
        cidadepes = input("Cidade:")
        if nomepes == nome:
            print(F"{nome}")
        elif idadepes == idade:
            print(f"{idade}")
        elif cidadepes == cidade:
            print(cidade)
        else:
            print("Nao cadastrado")