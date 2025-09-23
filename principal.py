print("Principal")
from menu import *
clientes = []
while True:
    menu()
    opcao = int(input("Digite opção: "))
    match opcao:
        case 1:
            cadastrar(clientes)
        case 2:
            listar(clientes)
        case 0:
            break
        case _:
            print ("Opção inválida")    