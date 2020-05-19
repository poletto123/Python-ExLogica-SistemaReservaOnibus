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

# Uma poltrona disponível retorna False
# Uma poltrona ocupada retorna True
for poltrona in range (0, 24):
    listaJanela.append((poltrona, False))
    listaCorredor.append((poltrona, False))

#######################################################

print("Seja bem-vindo ao sistema de reserva da FOGUETE\n")
while continuar == True:
    opcao = mostrarMenu()
    if opcao == 1:

        tamanhoListaCorredor = numPoltronasDisponiveisCorredor = len(listaCorredor)
        tamanhoListaJanela = numPoltronasDisponiveisJanela = len(listaJanela)

        for i in listaJanela:
            if i[1] == True:
                numPoltronasDisponiveisJanela -= 1
        for i in listaCorredor:
            if i[1] == True:
                numPoltronasDisponiveisCorredor -= 1

        if numPoltronasDisponiveisJanela == 0 and numPoltronasDisponiveisCorredor == 0:
            print("Ônibus lotado. Opção inválida!")
        else:
            corredorPol = corredorPoltrona()
            numeroPol = numeroPoltrona()
            if corredorPol == 1:
                if listaCorredor[numeroPol] == (numeroPol, True):
                    print("Poltrona ocupada. Venda não realizada!\n")
                else:
                    listaCorredor[numeroPol] = [numeroPol, True]
                    print("Venda realizada com sucesso!\n")

