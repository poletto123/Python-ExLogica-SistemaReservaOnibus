import sys
from EntregaCTP.Funcoes import *

continuar = True

while continuar == True:

    opcao = menu()

    if opcao == 1:
        soma = sum(listaJanela + listaCorredor)

        if soma == 48:
            print("Ônibus lotado. Opção inválida!")
        else:
            venderPoltrona()

    if opcao == 2:
        soma = sum(listaJanela + listaCorredor)

        if soma == 0:
            print("Todas as poltronas estão livres. Opção inválida!")
        else:
            cancelarCompra()

    if opcao == 3:
        mostrarLugares()

    if opcao == 4:
        continuar = False
