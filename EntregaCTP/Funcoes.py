listaJanela = list([0]*24) # 24 lugares
listaCorredor = list([0]*24) # 24 lugares

def menu():
    escolha = int(input("1 - Vender Passagem \n2 - Cancelar Compra \n3 - Mostrar Mapa de Ocupação \n4 - Sair \n"))
    while escolha != 1 and escolha != 2 and escolha != 3 and escolha != 4:
        print("\nDigite um valor entre 1 e 4\n")
        escolha = int(input("1 - Vender Passagem \n2 - Cancelar Compra \n3 - Mostrar Mapa de Ocupação \n4 - Sair \n"))
    return escolha

def numeroPoltrona():
    numeroPoltrona = int(input("Qual é o número da poltrona? (1 - 24) \n")) - 1
    while numeroPoltrona < 0 or numeroPoltrona > 23:
        print("Opção inválida. Digite um número de 1 a 24")
        numeroPoltrona = int(input("Qual é o número da poltrona? (1 - 24) \n")) -1
    return numeroPoltrona

def janelaCorredor():
    janelaCorredor = input("Deseja a poltrona da JANELA ou CORREDOR? (J/C) \n").upper()
    while janelaCorredor not in ["J", "C"]:
        print("Opção inválida. Digite J ou C")
        janelaCorredor = input("Deseja a poltrona da JANELA ou CORREDOR? (J/C) \n").upper()
    return janelaCorredor

def venderPoltrona():
    numPoltrona = numeroPoltrona()
    janCorredor = janelaCorredor()

    if janCorredor == "C":
        if listaCorredor[numPoltrona] == 0:
            listaCorredor[numPoltrona] = 1
            print("\nVenda realizada com sucesso!\n")
        else:
            print("\nPoltrona ocupada. Venda não realizada!\n")

    if janCorredor == "J":
        if listaJanela[numPoltrona] == 0:
            listaJanela[numPoltrona] = 1
            print("\nVenda realizada com sucesso!\n")
        else:
            print("\nPoltrona ocupada. Venda não realizada!\n")

def cancelarCompra():
    numPoltrona = numeroPoltrona()
    janCorredor = janelaCorredor()

    if janCorredor == "J":
        if listaJanela[numPoltrona] == 1:
            listaJanela[numPoltrona] = 0
            print("\nCompra cancelada com sucesso!\n")
        else:
            print("\nPoltrona livre. Compra não cancelada!\n")

    if janCorredor == "C":
        if listaCorredor[numPoltrona] == 1:
            listaCorredor[numPoltrona] = 0
            print("\nCompra cancelada com sucesso!")
        else:
            print("\nPoltrona livre. Compra não cancelada!\n")

def mostrarLugares():
    print("\nJANELA:            ", end="")
    print("CORREDOR: ")

    for x in range(len(listaJanela)):
        if listaJanela[x] == 0:
            print((x + 1), " - ", "Livre  ", end="")
        else:
            print((x + 1), " - ", "Ocupada", end="")

        if listaCorredor[x] == 0:
            print("     ", (x + 1), " - ", "Livre")
        else:
            print("     ", (x + 1), " - ", "Ocupada")

    print("\n\n")