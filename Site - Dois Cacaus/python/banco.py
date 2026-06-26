print("SELCIONE UMA DAS OPÇÕES:")
print("1==SACAR==")
print("2==DEPOSITAR==")

sac = int(input())
saldo1 = 200000
if sac == 1:
    print("SEU SALDO ATUAL É:R$200.000,OO")
    quantidade1 = float(input("QUANTO DESEJA SACAR:R$"))
    sac = saldo1 - quantidade1
    if quantidade1 >=0:
        print(f"SEU SALDO ATUAL É:{sac}")
    else:
        print("Voce ta devendo o banco")
else:
    print("SAQUE EFETUADO")

if sac == 2:
   quantia = float(input("QUANTIA REQUERENTE PARA DEPOSITO:"))
   if quantia >= 1:
       saldo1 = quantia + saldo1
       print(f"SEU SALDO ATUAL É:R${saldo1}")
   else:
       print("TA FAZENDO OQUE, SAQUE?")
else:
    print("DEPOSITO EFETUADO")
    
