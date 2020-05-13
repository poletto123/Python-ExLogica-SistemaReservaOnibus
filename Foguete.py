import sys

janela = list([0]*24) # 24
corredor = list([0]*24) # 24

opcao = int(input("1 - Vender Passagem \n2 - Cancelar Compra \n3 - Mostrar Mapa de Ocupação \n4 - Sair \n"))

while opcao >= 0 and opcao < 0:
    if opcao == 1:

        soma = sum(janela + corredor)

        if soma == 48:
            print("Ônibus lotado. Opção inválida!")
        else:
            numero = int(input("Qual é o número da poltrona? (1 - 24) \n"))
            poltrona = input("Deseja vender a janela da JANELA ou CORREDOR? (J/C) \n").upper()

            numero -= 1

            if poltrona == "J":
                if janela[numero] == 0:

                    janela[numero] = 1
                    print("\nVenda realizada com sucesso!")
                    print(janela[numero])

                else:

                    print("\nPoltrona ocupada. Venda não realizada!\n")

                if poltrona == "C":
                    if corredor[numero] == 0:

                        corredor[numero] = 1
                        print("\nVenda realizada com sucesso!")

                    else:

                        print("\nPoltrona ocupada. Venda não realizada!\n")

    if opcao == 2:
        soma = sum(janela + corredor)

        if soma == 0:
            print("Todas as poltronas estão livres. Opção inválida!")
        else:
            numero = int(input("Qual é o número da poltrona? (1 - 24) \n"))
            poltrona = input("Deseja vender a janela da JANELA ou CORREDOR? (J/C) \n").upper()

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


    if opcao == 3:
        print("\nJANELA:            ", end="")
        print("CORREDOR: ")

        for x in range(len(janela)):
            if janela[x] == 0:
                print((x+1), " - ", "Livre", end="")
            else:
                print((x+1), " - ", "Ocupada", end="")

            if corredor[x] == 0:
                print("     ", (x+1), " - ", "Livre")
            else:
                print("     ", (x+1), " - ", "Ocupada")



        print("\n\n")

    if opcao == 4:
        sys.exit()

    if opcao != 1 and opcao != 2 and opcao != 3 and opcao != 4:
        print("\nDigite um valor entre 1 e 4\n")

    opcao = int(input("1 - Vender Passagem \n2 - Cancelar Compra \n3 - Mostrar Mapa de Ocupação \n4 - Sair \n"))
