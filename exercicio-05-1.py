thisdict = {
    "heilhtlr" : "1945119",
    "exodsrenns" : "rdrgprco",
    "lrsmsc" : "nndclv12",
    "simancaisimata" : "28012021"
}

def cadastrar_usuario(thisdict_local):

    ask = input("Insira seu nome de usuário. ")
    if ask in thisdict_local:
        print("Esse nome de usuário está indisponível.")
    else:
        senha = input("Insira uma senha.")
        return thisdict_local.update({ask : senha})
    
def login(thisdict_local):
    ask = input("Insira seu nome de usuário. ")
    senha = input("Insira sua senha de acesso. ")
    if ask in thisdict_local and thisdict_local[ask] == senha:
        print("Login bem-sucedido!")
    else:
        print("Login ou senha incorretos.")
        
while True:
    
    ask = int(input("Insira uma das opções.\n"
                "(1): Cadastrar usuário\n"
                "(2): Fazer login\n"
                "(3): Sair\n"
                ": "))
    if ask == 1:
        cadastrar_usuario(thisdict)
    elif ask == 2:
        login(thisdict)
    elif ask == 3:
        print("Vaza.")
        break
    else:
        print("Opção inválida. Tente novamente.")
    

    
    
    