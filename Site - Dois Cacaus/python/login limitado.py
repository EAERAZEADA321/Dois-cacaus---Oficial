email = str(input("Digite seu email:"))
senha = str(input("Digite a senha:"))

senhaver = "cariri123"

if senha != senhaver:
    print("login errado")
    senha = input("digite denovo:")
    if senha != senhaver:
        print("login errado denovo mais 1 tentiva")
        senha = input("digite denovo:")
    else:
        print("login completado")
        if senha != senhaver:
            print("login bloqueado:")
        else:
            print("login completado")
else:
    print("login completado")
    