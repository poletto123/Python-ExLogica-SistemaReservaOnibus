assentos_janela = list([0]*24)

assentos_corredor = list([0]*24)

print("Assentos na Janela:",assentos_janela)
print("Assentos no Corredor:",assentos_corredor)

opcao = int(input("O que você deseja?"
"\n 1 - Vender passagem"
"\n 2 - Cancelar compra"
"\n 3 - Mostrar mapa de ocupação"
"\n 4 - Sair"))

while(opcao!=1 or opcao!=2 or opcao !=3 or opcao!=4):
  if(opcao!=1 or opcao!=2 or opcao !=3 or opcao!=4):
    print("ERRO: Digite uma opção válida.")
    opcao = int(input("O que você deseja?"
    "\n 1 - Vender passagem"
    "\n 2 - Cancelar compra"
    "\n 3 - Mostrar mapa de ocupação"
    "\n 4 - Sair"))

  if(opcao==1):
    opcao_assento = input("Você deseja um assento no corredor ou janela?")

    if(opcao_assento=="corredor" or opcao_assento=="Corredor"):
      posicao_assento = int(input("Qual o número do assento [entre 1 a 24] você deseja?"))
      if(assentos_corredor[posicao_assento-1]==1):
        print("Desculpe mas já está reservado.")
      else:
        assentos_corredor[posicao_assento-1] = 1
        print("Venda realizada com sucesso!")
        print(assentos_corredor)

    if(opcao_assento=="janela" or opcao_assento=="Janela"):
      posicao_assento = int(input("Qual o número do assento [entre 1 a 24] você deseja?"))
      if(assentos_janela[posicao_assento-1]==1):
        print("Desculpe mas já está reservado.")
        print(assentos_janela)
      else:
        assentos_janela[posicao_assento-1] = 1
        print("Venda realizada com sucesso!")
        print(assentos_janela)

  elif(opcao==2):
    posicao_assento = int(input("Qual o número do assento [entre 1 a 24] você deseja cancelar?"))
    opcao_assento = input("Você deseja cancelar esse assento no corredor ou janela?")

    if(opcao_assento=="corredor" or opcao_assento=="Corredor"):
      if(assentos_corredor[posicao_assento-1]==1):
        assentos_corredor[posicao_assento-1] = 0
        print("Cancelamento realizado com sucesso!")
        print(assentos_corredor)
      else:
        print("Desculpe mas já está cancelado.")
        print(assentos_corredor)
    if(opcao_assento=="janela" or opcao_assento=="Janela"):
      if(assentos_janela[posicao_assento-1]==1):
        assentos_janela[posicao_assento-1] = 0
        print("Cancelamento realizado com sucesso!")
        print(assentos_janela)
      else:
        print("Desculpe mas já está cancelado.")
        print(assentos_janela)
  elif(opcao==3):

    #for que printe 

    print(assentos_corredor)
    print(assentos_janela)
  elif(opcao==4):
    print("Saindo...")
    break