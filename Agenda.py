# - Cadastrar um contato
# - Listar os contatos
# - Pesquisar um contato
# - Alterar um contato 
# - Excluir um contato
# - Sair  

from os import system

lista = []

def cadastrar(nome, numero):
    dicionario = {
        "Nome": nome,
        "Número": numero
    }
    lista.append(dicionario)

def menu():
    opc = int(input('''
----------------------------------------------------
[1] - Cadastrar um contato
[2] - Listar os contatos
[3] - Pesquisar um contato
[4] - Alterar um contato 
[5] - Excluir um contato
[6] - Sair 
----------------------------------------------------
Opção desejada: '''))
    return opc

def menu_alterar():
    opc_alterar = int(input('''
----------------------------------------------------
[1] - Alterar nome
[2] - Alterar número
[3] - Alterar nome e número
----------------------------------------------------
Opção desejada:  '''))
    return opc_alterar

def cadastrar_contato():
    nome = str(input("Nome: "))
    numero = int(input("Telefone: "))
    cadastrar(nome, numero)
    system('cls')
    print("Adicionado com sucesso!!!")

def listar_contatos():  
    for contatos in lista:
        for chave, valor in contatos.items():
            print(f"{chave}: {valor}")
    
def pesquisar_contato():
    pesquisar = str(input('Pesquisar nome: '))
    system('cls')
    for i in lista:
        if i["Nome"] == pesquisar:
            for chave, valor in i.items():
                print(f"{chave}: {valor}")

def alterar_contato():
    alterar = str(input('Qual deseja alterar? '))
    for i in lista:
        if i['Nome'] == alterar:
            system('cls')
            novo_nome = str(input("Novo nome: "))
            novo_numero = int(input("Novo numero: "))
            local = lista.index(i)
            lista[local] = {
                "Nome": novo_nome,
                "Número": novo_numero
            }
            system('cls')
            print("Alterado com sucesso!!!")
        else:
            print('não se encontra na lista!!!') 
 
def remover_contato():
    excluir_nome = str(input("Excluir contato: "))#.lower()
    for nome in lista:
        if nome["Nome"] == excluir_nome:
            local = lista.index(nome)
            lista.pop(local)
            system('cls')
            print("Contato excluido com sucesso!!!")
        else:
            print('opção invalida!!!')

def operacao():
    while True:
        escolha = menu()
        match escolha:
            case 1:
                system('cls')
                cadastrar_contato()
            case 2:
                system('cls')
                listar_contatos()
            case 3:
                system('cls')
                pesquisar_contato()
            case 4:
                system('cls')
                alterar_contato()
            case 5:
                system('cls')
                remover_contato()
            case 6:
                system('cls')
                break

operacao()
