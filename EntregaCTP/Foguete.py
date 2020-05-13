import sys
from EntregaCTP.Funcoes import *

opcao = menu()

while opcao >= 0 or opcao < 0:
    if opcao == 1:
        soma = sum(janela + corredor)

        if soma == 48:
            print("Ônibus lotado. Opção inválida!")
        else:
            venderPoltrona()

    if opcao == 2:
        soma = sum(janela + corredor)

        if soma == 0:
            print("Todas as poltronas estão livres. Opção inválida!")
        else:
            cancelarCompra()

    if opcao == 3:
        mostrarLugares()

    if opcao == 4:
        sys.exit()

    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print("\nDigite um valor entre 1 e 4\n")

    opcao = menu()
