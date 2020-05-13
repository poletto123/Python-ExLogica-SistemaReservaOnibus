janela = list([0]*24) # 24
corredor = list([0]*24) # 24

def menu():
    escolha = int(input("1 - Vender Passagem \n2 - Cancelar Compra \n3 - Mostrar Mapa de Ocupação \n4 - Sair \n"))
    return escolha

def venderPoltrona():
    numero = int(input("Qual é o número da poltrona? (1 - 24) \n"))
    poltrona = input("Deseja vender a poltrona da JANELA ou CORREDOR? (J/C) \n").upper()

    numero -= 1

    if poltrona == "C":
        if corredor[numero] == 0:

            corredor[numero] = 1
            print("\nVenda realizada com sucesso!")

        else:
            print("\nPoltrona ocupada. Venda não realizada!\n")

    if poltrona == "J":
        if janela[numero] == 0:

            janela[numero] = 1
            print("\nVenda realizada com sucesso!")

        else:
            print("\nPoltrona ocupada. Venda não realizada!\n")

def cancelarCompra():
    numero = int(input("Qual é o número da poltrona? (1 - 24) \n"))
    poltrona = input("Deseja cancelar a poltrona da JANELA ou CORREDOR? (J/C) \n").upper()

    numero -= 1

    if poltrona == "J":
        if janela[numero] == 1:

            janela[numero] = 0
            print("\nCompra cancelada com sucesso!")

        else:

            print("\nPoltrona livre. Compra não cancelada!\n")

    if poltrona == "C":
        if corredor[numero] == 1:
            corredor[numero] = 0
            print("\nCompra cancelada com sucesso!")
        else:
            print("\nPoltrona livre. Compra não cancelada!\n")

def mostrarLugares():
    print("\nJANELA:            ", end="")
    print("CORREDOR: ")

    for x in range(len(janela)):
        if janela[x] == 0:
            print((x + 1), " - ", "Livre  ", end="")
        else:
            print((x + 1), " - ", "Ocupada", end="")

        if corredor[x] == 0:
            print("     ", (x + 1), " - ", "Livre")
        else:
            print("     ", (x + 1), " - ", "Ocupada")

    print("\n\n")