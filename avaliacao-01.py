conta = {
    "615325": 96.00,
    "989176": 37.00     
}

def auntenticar_conta():
    senha = input("Insira sua senha. ")
    if senha in conta:
        print("Sua senha é válida. ")
        return senha
    else:
        print("Senha inválida. ")

def verificar_saldo(senha_local):
    print (conta[senha_local])
    
    
def depositar_valor(senha_local):
    deposito = int(input("Insira o valor de  depósito. "))
    conta[senha_local] = conta[senha_local] + deposito

def retirar_valor(senha_local):
    saque = int(input("Insira o valor de saque. "))
    if saque > conta[senha_local]:
        print("Valor indisponível para saque. ")
    else:
        conta[senha_local] = conta[senha_local] - saque
        
def operaçoes_bancarias(senha_local):

    while True:
 
        ask = int(input("Insira uma das opções.\n"
                "[ 1 ]: Verificar saldo\n"
                "[ 2 ]: Depositar dinheiro\n"
                "[ 3 ]: Retirar dinheiro\n"
                "[ 4 ]: Sair\n"
                ": ")) 
        
        if ask == 1:
            verificar_saldo(senha_local)
        elif ask == 2:
            depositar_valor(senha_local)
        elif ask == 3:
            retirar_valor(senha_local)
        elif ask == 4:
            print("Encerramos por aqui! ")
            break
        else:
            print("Opção inválida. Tente novamente. ")
        
senha = auntenticar_conta()
operaçoes_bancarias(senha)