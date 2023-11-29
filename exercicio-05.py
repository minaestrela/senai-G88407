thisdict = {
    "minaestrela": "89652937",
    "lensouir": "4810385"
}

quest = input("Insira seu nome de usuário: ")

quest2 = input("Insira a senha: ")

if quest in thisdict: 
    if thisdict(quest) == quest2:
        print("Login bem-sucedido!")
    print("Nome de usuário válido.")
else:
    print("Usuário inválido.")
    
        
