conta = {
    "615325": 96.00,
    "989176": 37.00     
}

def auntenticar_conta():
    senha = input("Insira sua senha.")
    if senha in conta:
        print("Sua senha é válida.")
    else:
        print("Senha inválida.")

def verificar_saldo():
    saldo = conta[saldo]
    
def depositar_valor():
    deposito = input("Insira o valor de  depósito.")
    if deposito in conta:
        conta[deposito] = conta[deposito] + deposito
def retirar_valor():
    saque = input("Insira o valor de saque.")
    if saque in conta:
        if saque < conta[saque]:
            print("Valor indisponível para saque.")
    else:
        saque = saque + conta[saque]
        
def operaçoes_bancarias():

    while True:
 
        ask = int(input("Insira uma das opções.\n"
                "1: Verificar saldo\n"
                "2: Depositar dinheiro\n"
                "3: Retirar dinheiro\n"
                "4: Sair\n"
                ": ")) 
        
        if ask == 1:
            print(verificar_saldo)
        elif ask == 2:
            depositar_valor()
        elif ask == 3:
            retirar_valor()
        elif ask == 4:
            print("Encerramos por aqui!")
            break
        else:
            print("Opção inválida. Tente novamente.")