# Lista de nomes e números de telefone
lista_de_contatos = [
    {'nome': 'Ana Oliveira', 'telefone': '123-456-7890'},
    {'nome': 'João Silva', 'telefone': '234-567-8901'},
    {'nome': 'Maria Santos', 'telefone': '345-678-9012'},
    {'nome': 'Pedro Costa', 'telefone': '456-789-0123'},
    {'nome': 'Laura Pereira', 'telefone': '567-890-1234'},
    {'nome': 'Lucas Rodrigues', 'telefone': '678-901-2345'},
    {'nome': 'Julia Lima', 'telefone': '789-012-3456'},
    {'nome': 'Gabriel Souza', 'telefone': '890-123-4567'},
    {'nome': 'Mariana Oliveira', 'telefone': '901-234-5678'},
    {'nome': 'Matheus Santos', 'telefone': '012-345-6789'},
    {'nome': 'Isabella Costa', 'telefone': '123-456-7890'},
    {'nome': 'Felipe Silva', 'telefone': '234-567-8901'},
    {'nome': 'Larissa Santos', 'telefone': '345-678-9012'},
    {'nome': 'Rafael Costa', 'telefone': '456-789-0123'},
    {'nome': 'Beatriz Pereira', 'telefone': '567-890-1234'},
    {'nome': 'Enzo Rodrigues', 'telefone': '678-901-2345'},
    {'nome': 'Livia Lima', 'telefone': '789-012-3456'},
    {'nome': 'Daniel Souza', 'telefone': '890-123-4567'},
    {'nome': 'Sophia Oliveira', 'telefone': '901-234-5678'},
    {'nome': 'Gustavo Santos', 'telefone': '012-345-6789'},
    {'nome': 'Ana Luiza Costa', 'telefone': '123-456-7890'},
    {'nome': 'Eduardo Silva', 'telefone': '234-567-8901'},
    {'nome': 'Catarina Santos', 'telefone': '345-678-9012'},
    {'nome': 'Vinicius Costa', 'telefone': '456-789-0123'},
    {'nome': 'Carolina Pereira', 'telefone': '567-890-1234'},
    {'nome': 'Bruno Rodrigues', 'telefone': '678-901-2345'},
    {'nome': 'Amanda Lima', 'telefone': '789-012-3456'},
    {'nome': 'Lucas Souza', 'telefone': '890-123-4567'},
    {'nome': 'Juliana Oliveira', 'telefone': '901-234-5678'},
    {'nome': 'Rafaela Santos', 'telefone': '012-345-6789'},
    {'nome': 'Thiago Costa', 'telefone': '123-456-7890'},
    {'nome': 'Natasha Silva', 'telefone': '234-567-8901'},
    {'nome': 'Leonardo Santos', 'telefone': '345-678-9012'},
    {'nome': 'Marina Costa', 'telefone': '456-789-0123'},
    {'nome': 'Fernando Pereira', 'telefone': '567-890-1234'},
    {'nome': 'Larissa Rodrigues', 'telefone': '678-901-2345'},
    {'nome': 'Renato Lima', 'telefone': '789-012-3456'},
    {'nome': 'Isadora Souza', 'telefone': '890-123-4567'},
    {'nome': 'Vitor Oliveira', 'telefone': '901-234-5678'},
    {'nome': 'Camila Santos', 'telefone': '012-345-6789'},
    {'nome': 'Lucas Costa', 'telefone': '123-456-7890'},
    {'nome': 'Caroline Silva', 'telefone': '234-567-8901'},
    {'nome': 'Rodrigo Santos', 'telefone': '345-678-9012'},
    {'nome': 'Luana Costa', 'telefone': '456-789-0123'},
    {'nome': 'Marcos Pereira', 'telefone': '567-890-1234'},
    {'nome': 'Aline Rodrigues', 'telefone': '678-901-2345'},
]

pesquisa = input('Informe o nome que deseja procurar: ')

if pesquisa in lista_de_contatos:
    print('O nome informado esta na lista de contatos: ')
else:
    print('O nome informado não esta na lista de contatos')
