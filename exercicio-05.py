thisdict = {
    "minaestrela": "89652937",
    "lensouir": "4810385"
}

quest = input("Insira seu nome de usuário: ")

quest2 = input("Insira a senha: ")

if quest in thisdict: 
    if thisdict[quest] == quest2:
        print("Nome de usuário válido.")
        print("Login bem-sucedido!")
else:
    print("Usuário inválido.")
    
        
