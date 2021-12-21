AGENDA = {}


def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contatos(contato)
    else:
        print('>>> Agenda vazia.')


def buscar_contatos(contato):
    try:
        print('Nome:', contato)
        print('Telefone:', AGENDA[contato]['telefone'])
        print('email:', AGENDA[contato]['email'])
        print('endereco:', AGENDA[contato]['endereco'])
        print('-----------------------------------------')
    except KeyError:
        print('>>> Contato inexistente.')
    except Exception as error:
        print('>>> Um erro inesperado ocorreu.')
        print(error)


def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA [contato] = {
    'telefone': telefone,
    'email': email,
    'endereco': endereco,
    }
    salvar()
    print()
    print(f'>>> Contato {contato} adicionado e editado com sucesso')
    print()


def ler_detalhes_contato():
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    endereco = input("Digite o endereco do contato: ")
    return telefone, email, endereco


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print()
        print(f'>>> Contato {contato} excluido com sucesso')
        print()
    except KeyError:
        print('>>> Contato inexistente.')
    except Exception as error:
        print('>>> Um erro inesperado ocorreu.')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as fn:
            linhas = fn.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA [nome] = {
                    'telefone': telefone,   
                    'email': email,
                    'endereco': endereco,
                }
        print('>>> Database carregado com sucesso!!!')
        print('>>> {} contatos carregados.'.format(len(AGENDA)))
    except FileNotFoundError:
        print('>>> Arquivo nao encontrado')
    except Exception as error:
        print('>>> Algum erro ocorreu')
        print(error)


def imprimir_menu():
    print('-----------------------------------------')
    print("0 - Exportar contatos .csv")
    print("1 - Mostrar todos os contatos da Agenda")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Importar contatos")
    print("7 - Fechar agenda")
    print('-----------------------------------------')


def exportar_contatos(file_name):
    try:
        with open(file_name, 'w') as file:
            #file.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write('{}, {}, {}, {}\n'.format(contato, telefone, email, endereco))
        print('>>> Agenda exportada com sucesso')
    except Exception as error:
        print('>>> Algum erro ocorreu durante exportar o arquivo')
        print(error)


def importar_contatos(file_name):
    try:
        with open(file_name, 'r') as fn:
            linhas = fn.readlines()
            for linha in linhas:
                detalhes = (linha.strip().split(','))
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('>>> Arquivo nao encontrado')
    except Exception as error:
        print('>>> Algum erro ocorreu')
        print(error)


carregar()
while True:
    imprimir_menu()

    opcao = input("Escolha uma opcao: ")
    if opcao == '0':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ') 
        exportar_contatos(nome_do_arquivo)
    elif opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input("Digite o nome do contato: ")
        buscar_contatos(contato)
    elif opcao == '3':
        contato = input("Digite o nome do contato a ser incluso: ")
        try:
            AGENDA[contato]
            print('>>> Contato já existente')
        except KeyError:
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('Digite o nome do contato a ser editado: ')
        try:
            AGENDA[contato]
            print('>>> Editar contato:', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>> Contato inexistente.')
    elif opcao == '5':
        contato = input("Digite o nome do contato a ser excluído: ")
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input("Digite o nome do arquivo para importar: ")
        importar_contatos(nome_do_arquivo)
    elif opcao == '7':
        print('>>> Fechando programa!')
        break
    else:
        print('>>> Opcao invalida! Tente outra opcao.')