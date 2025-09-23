def menu():
    print('menu')
    print('1 - Cadastro')
    print('2 - Listar')
    print('0 - Sair')

menu() #Chamando a função

def cadastrar(lista):
  while True:     
    pessoa = {}
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade: "))
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['animais'] = cadastrarPet()
    lista.append(pessoa)
    r = pegarResposta("Deseja cadastrar outro cliente:" )
    if r ==True:
        break

def cadastrarPet():
    animais = []
    while True:
        nome = input ("Informe o nome do animal: ")
        animais.append(nome)
        r = pegarResposta("Deseja cadastrar outro animal: ")
        if r == True:
            break
    return animais

def pegarResposta(frase):
    retorno = False 
    r = ""
    while True:
        r = input(f'{frase}? (s/n)')
        r = r[0].lower()
        if r != 's' and r != 'n':
           print("Resposta Inválida")
        else:
            break
    if r =='n':
        retorno = True
    return retorno
def listar (lista):

    for elemento in (lista):
        print(f'{elemento["nome"]} - {elemento["idade"]}')
        print("Os pets:")
        for pet in elemento["animais"]:
            print(pet)
        print("-"*30)