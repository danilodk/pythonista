import pandas as pd
from tabulate import tabulate

# Dados de exemplo para junho
dados_junho = {
    'Nome': ['Fernando Luiz de Souza', 'Danilo'],
    'Nascimento': ['26/06/1984', '20/06/2000'],
    'Local': ['Santa Cecília SC', 'Monte Castelo SC'],
    'RG': [4868289, 390957471],
    'CPF': ['05085843748', '43713216210'],
}

# Transforma os dados em um DataFrame
junho = pd.DataFrame(dados_junho)

# Apresentação do programa
print('*** Sistema de consulta de aniversariantes da Igreja Reviver ***\n')

# Dicionário de meses
meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

# Obtém a opção do usuário
opcao = int(input('Digite o número do mês que deseja consultar (1-12): '))

# Verifica se a opção é válida e imprime os dados do mês correspondente
if opcao in meses:
    print(tabulate(junho, headers='keys', tablefmt='fancy_grid'))
else:
    print('Opção inválida! Por favor, digite um número de 1 a 12.')

# Aguarda a entrada do usuário antes de fechar o programa
input('\nPressione "Enter" para fechar o programa...')
