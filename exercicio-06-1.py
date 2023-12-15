cardapio = {
    "Duplo Burger Bacon": 25.45,
    "McChicken": 25.87,
    "McFlurry": 14.00,
    "Club House": 46.04
}

pedido = {
    
}

def exibir_cardapio():
        return

def adicionar_item():
    ask = input("Insira um item do menu.")
    if ask in pedido:
        pedido[ask] = pedido[ask] + 1
        return 
    else:
        if ask in cardapio:
            return pedido.update({ask: 1})

def remover_item():
    item = input("Insira um item.")
    if item in cardapio:
        if pedido[item] == 1:
            pedido.pop(item)
        elif pedido[item] > 1:
            pedido[item] -= 1
            return 

def exibir_pedido():    
    total = 0
    
    for item in pedido:
        print(item, "R$",cardapio[item])
        total = total + (cardapio[item]*pedido[item])
    print("Total: R$", total)

def emitir_nota():
    nota = open("nota-fiscal.txt", "w", encoding="utf-8")

    total = 0

    for item in pedido:
        nota.write(str(item) + " R$" + str(cardapio[item]) + "\n")
        total = total + (cardapio[item]*pedido[item])
    nota.write("Total: R$" + str(total))
    nota.close

while True:
    
    ask = int(input("Insira uma das opções.\n"
                "(1): Exibir cardápio\n"
                "(2): Adicionar item\n"
                "(3): Remover item\n"
                "(4): Exibir pedido\n"
                "(5): Emitir nota\n"
                "(6): Sair\n"
                ": "))

    if ask == 1:
        print(cardapio)
    elif ask == 2:
        adicionar_item()
    elif ask == 3:
        remover_item()
    elif ask == 4:
        exibir_pedido()
    elif ask == 5:
        emitir_nota()
    elif ask == 6:
        print("Encerramos por aqui!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        

        