lista = []

def cadastrador(nome, idade, altura):
    registrador = {
        'nome': nome,
        'idade': idade,
        'altura': altura
    }
    
    lista.append(registrador)

def mostrador():
    print('Usuários cadastrados: ')
    for i, usuario in enumerate(lista):
        print(f"{i + 1} - Nome: {usuario['nome']}, Idade: {usuario['idade']}, Altura: {usuario['altura']}")

def removerUser():
    if not lista:
        print("A lista está vazia. ")
        return
    
    mostrador()

    removerIndex = int(input('Digite o índice do usuário para removê-lo: ')) - 1

    if 0 <= removerIndex < len(lista):
        usuarioRemovido = lista.pop(removerIndex)
        print(f"Usuário {usuarioRemovido['nome']} removido com sucesso.")
    else:
        print(f"Digite um número entre 1 e {len(lista)}")

def atualizador():
    if not lista:
        print("A lista está vazia. ")
        return

    mostrador()

    editarIndex = int(input('Digite o índice do usuário para editar. ')) - 1

    if 0 <= editarIndex < len(lista):
        print(f"Você está editando o usuário {lista[editarIndex]['nome']}... ")
        lista[editarIndex]['nome'] = input('Digite o novo nome: ')
        lista[editarIndex]['idade'] = int(input('Digite a nova idade: '))
        lista[editarIndex]['altura'] = float(input('Digite a nova altura: '))
    else:
        print(f"Digite um número entre 1 e {len(lista)}")

while True:
    opcao = input(''' 
=========== CRUD ===========                  
(1) - Adicionar usuário
(2) - Listar usuários
(3) - Remover usuário
(4) - Atualizar um usuário
(5) - Sair
============================                  
''')

    match opcao:
        case '1':
            nome = input('Digite o nome: ')
            idade = int(input('Digite a idade: '))
            altura = float(input('Digite a altura: '))
            cadastrador(nome, idade, altura)
        case '2':
            mostrador()
        case '3':
            removerUser()
        case '4':
            atualizador()
        case '5':
            print('Saindo do programa... ')
            break
        case _:
            print('Digite uma opção válida: ')


