def question():
    return input("O que deseja realizar?\n" +
                 "<I> - Para Inserir um usuário\n"+
                 "<P> - Para Pesquisar um usuário\n"+
                 "<E> - Para Excluir um usuário\n"+
                 "<L> - Para Listar um usuário: ").upper()

def insert(dictionary):
    dictionary[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                                                 input("Digite a última data de acesso: "),
                                                 input("Qual a última estação acessada: ").upper()]
    save(dictionary)

def save(dictionary):
    with open("../database/db.txt", "a") as file:
        for key, value in dictionary.items():
            file.write(key + ":" + str(value))


