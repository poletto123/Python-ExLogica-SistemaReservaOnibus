listaJanela = []
listaCorredor = []
continuar = True

def mostrarMenu():
    opcao = int(input("Escolha uma opção:\n"
             "1. Vender passagem\n"
             "2. Cancelar compra\n"
             "3. Mostrar mapa de ocupação\n"
             "4. Sair\n"))
    while opcao not in [1,2,3,4]:
        print("Opção inválida")
        opcao = mostrarMenu()
    return int(opcao)

def numeroPoltrona():
    numeroPoltrona = int(input("Qual o número da poltrona desejada? De 1 a 24\n")) - 1
    while 24 < numeroPoltrona < 1:
        print("Opção inválida\n")
        numeroPoltrona = numeroPoltrona()
    return numeroPoltrona

def corredorPoltrona():
    corredorPoltrona = int(input("Você quer:\n"
                                 "1. Corredor?\n"
                                 "2. Janela?\n"))
    while corredorPoltrona not in [1,2]:
        print("Opção inválida")
        corredorPoltrona = corredorPoltrona()
    return corredorPoltrona

def checkOnibusLotadoVazio():
    numPoltronasDisponiveisCorredor = len(listaCorredor)
    numPoltronasDisponiveisJanela = len(listaJanela)

    for i in listaJanela:
        if i[1] == True:
            numPoltronasDisponiveisJanela -= 1
    for i in listaCorredor:
        if i[1] == True:
            numPoltronasDisponiveisCorredor -= 1

    if numPoltronasDisponiveisJanela == 0 and numPoltronasDisponiveisCorredor == 0:
        return True
    elif numPoltronasDisponiveisJanela == len(listaJanela) and numPoltronasDisponiveisCorredor == len(listaCorredor):
        return False
    else:
        return None

# Uma poltrona ocupada retorna True
# Uma poltrona disponível retorna False
for poltrona in range (0, 24):
    listaJanela.append((poltrona, True))
    listaCorredor.append((poltrona, True))

#######################################################

print("Seja bem-vindo ao sistema de reserva da FOGUETE\n")
while continuar == True:

    opcao = mostrarMenu()

    if opcao == 1:
        onibusLotado = checkOnibusLotadoVazio()
        if onibusLotado:
            print("Ônibus lotado!\n")
            continue;
        else:
            corredorPol = corredorPoltrona()
            numeroPol = numeroPoltrona()
            if corredorPol == 1:
                if listaCorredor[numeroPol] == [numeroPol, True]:
                    print("Poltrona ocupada. Venda não realizada!\n")
                else:
                    listaCorredor[numeroPol] = [numeroPol, True]
                    print("Venda realizada com sucesso!\n")
            elif corredorPol == 2:
                if listaJanela[numeroPol] == [numeroPol, True]:
                    print("Poltrona ocupada. Venda não realizada!\n")
                else:
                    listaJanela[numeroPol] = [numeroPol, True]
                    print("Venda realizada com sucesso!\n")

    elif opcao == 2:
        onibusLotado = checkOnibusLotadoVazio()
        if onibusLotado is False:
            print("Ônibus vazio!\n")
            continue
        else:
            corredorPol = corredorPoltrona()
            numeroPol = numeroPoltrona()
            if corredorPol == 1:
                if listaCorredor[numeroPol] == [numeroPol, False]:
                    print("Poltrona livre. Cancelamento não realizado!\n")
                else:
                    listaCorredor[numeroPol] = [numeroPol, False]
                    print("Cancelamento realizado com sucesso!\n")
            elif corredorPol == 2:
                if listaJanela[numeroPol] == [numeroPol, False]:
                    print("Poltrona livre. Cancelamento não realizado!\n")
                else:
                    listaJanela[numeroPol] = [numeroPol, False]
                    print("Cancelamento realizado com sucesso!\n")

    elif opcao == 3:
        print("\nJANELA")
        for poltrona in listaJanela:
            if poltrona[1] == True:
                print(f"{poltrona[0] + 1} - Ocupado")
            elif poltrona[1] == False:
                print(f"{poltrona[0] + 1} - Livre")
        print("\n", end="")

        print("CORREDOR")
        for poltrona in listaCorredor:
            if poltrona[1] == True:
                print(f"{poltrona[0] + 1} - Ocupado")
            elif poltrona[1] == False:
                print(f"{poltrona[0] + 1} - Livre")
        print("\n", end="")

    elif opcao == 4:
        print("Até logo!")
        continuar = False

