idade = int(input("idade"))

if idade < 13:
    print("Você é criança.")
elif idade < 18:
    print("Você é adolescente.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")
    