
agenda = {}

def salvarContato(agenda):
    nomeContato = input("Nome do contato:  ")
    numeroContato = input("Numero do contato:  ")

    if nomeContato in agenda:
        print("Contato já existe na agenda!")

    else:
        agenda[nomeContato] = numeroContato
        print("Contato salvo com sucesso!")


def pesquisarContato(agenda, nomeContato):
    
    if nomeContato in agenda:
        print(f"Nome: {nomeContato}, número: {agenda[nomeContato]}")

    else:
        print("Contato não encontrado!")


def atualizarContato(agenda, nomeContato):
    
    if nomeContato in agenda:
         novoContato = input("Digite o número do novo contato: ")
         agenda[nomeContato] = novoContato
         print(f"Contato atualizado!")
    
    else:
        print("Contato não encontrado!")


def excluirContato(agenda, nomeContato):

    if nomeContato in agenda:
        del agenda[nomeContato]
        print("Contato excluído com sucesso!")

    else:
        print("Contato não encontrado")


def listaDeContatos(agenda):

    if not agenda:
        print("Não há contatos na lista!")
        return
    
    contatos = list(agenda.items())
    numerosContatos = len(contatos)

    for i in range(numerosContatos):
        for j in range(0, numerosContatos-i -1):
          if contatos[j][0] > contatos[j + 1][0]:
             contatos[j], contatos[j + 1] = contatos[j + 1], contatos[j]

    for nomeContato, numeroContato in contatos:
         print(f"Nome: {nomeContato}, Número: {numeroContato}")


def menu():
    
    while True:
        print("Menu")
        print("1 - Adicionar contato")
        print("2 - Pesquisar contato")
        print("3 - Atualizar número de contato")
        print("4 - Excluir contato")
        print("5 - Lista de contatos")
        print("6 - Sair")

        escolhaUsuario = input("Escolha uma opção")

        if escolhaUsuario == "1":
             salvarContato(agenda)

        elif escolhaUsuario == "2":
            nomeContato = input("Digite o nome do contato que queira pesquisar")
            pesquisarContato(agenda, nomeContato)

        elif escolhaUsuario == "3":
            nomeContato = input("Digite o nome do contato que queira atualizar")
            atualizarContato(agenda, nomeContato)

        elif escolhaUsuario == "4":
            nomeContato = input("Digite o nome do contato que queira excluir: ")
            excluirContato(agenda, nomeContato)
            
        elif escolhaUsuario == "5":
            listaDeContatos(agenda)

        elif escolhaUsuario == "6":
            print("Encerrando...")
            break
        
        else:
            print("Opção inválida, tente novamente")


menu()
            
        

    
    
    
        
    




    
