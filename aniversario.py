import pandas as pd
from tabulate import tabulate
from datetime import datetime

# ============================================
# BANCO DE DADOS DE ANIVERSARIANTES
# ============================================

dados_aniversarios = {
    1: {
        'Nome': ['João Silva', 'Maria Santos'],
        'Nascimento': ['15/01/1985', '28/01/1992'],
        'Local': ['Blumenau SC', 'Brusque SC'],
        'RG': [1234567, 7654321],
        'CPF': ['11122233344', '55566677788']
    },
    2: {
        'Nome': ['Pedro Costa', 'Ana Paula'],
        'Nascimento': ['10/02/1990', '25/02/1988'],
        'Local': ['Itajai SC', 'Navegantes SC'],
        'RG': [9876543, 2468135],
        'CPF': ['99911122233', '44455566677']
    },
    6: {
        'Nome': ['Fernando Luiz de Souza', 'Danilo'],
        'Nascimento': ['26/06/1984', '20/06/2000'],
        'Local': ['Santa Cecília SC', 'Monte Castelo SC'],
        'RG': [4868289, 390957471],
        'CPF': ['05085843748', '43713216210']
    }
}

# ============================================
# DICIONÁRIO DE MESES
# ============================================

meses = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
}

# ============================================
# FUNÇÕES
# ============================================

def exibir_menu():
    """Exibe o menu principal do programa"""
    print('\n' + '='*60)
    print('*** SISTEMA DE CONSULTA DE ANIVERSARIANTES ***')
    print('*** Igreja Reviver ***')
    print('='*60)
    print('\n1. Consultar aniversariantes por mês')
    print('2. Buscar pessoa por nome')
    print('3. Listar todos os aniversariantes')
    print('4. Sair')
    print('\n' + '-'*60)

def consultar_por_mes(numero_mes):
    """Consulta aniversariantes de um mês específico"""
    if numero_mes not in meses:
        print('\n❌ Erro: Mês inválido! Digite um número de 1 a 12.')
        return False
    
    if numero_mes not in dados_aniversarios:
        print(f'\n⚠  Não há aniversariantes cadastrados para {meses[numero_mes]}')
        return False
    
    dados = dados_aniversarios[numero_mes]
    df = pd.DataFrame(dados)
    
    print(f'\n🎆 Aniversariantes de {meses[numero_mes].upper()} 🎆\n')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
    print(f'\nTotal: {len(df)} pessoa(s)')
    return True

def buscar_por_nome(nome_busca):
    """Busca uma pessoa pelo nome em todos os meses"""
    resultados = []
    
    for mes, dados in dados_aniversarios.items():
        for idx, nome in enumerate(dados['Nome']):
            if nome_busca.lower() in nome.lower():
                resultados.append({
                    'Mês': meses[mes],
                    'Nome': nome,
                    'Nascimento': dados['Nascimento'][idx],
                    'Local': dados['Local'][idx],
                    'RG': dados['RG'][idx],
                    'CPF': dados['CPF'][idx]
                })
    
    if not resultados:
        print(f'\n❌ Nenhuma pessoa encontrada com o nome: {nome_busca}')
        return False
    
    df = pd.DataFrame(resultados)
    print(f'\n🔍 Resultado(s) da busca por: "{nome_busca}" \n')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))
    print(f'\nTotal: {len(df)} resultado(s) encontrado(s)')
    return True

def listar_todos():
    """Lista todos os aniversariantes cadastrados"""
    todos_dados = []
    
    for mes in sorted(dados_aniversarios.keys()):
        dados = dados_aniversarios[mes]
        for idx, nome in enumerate(dados['Nome']):
            todos_dados.append({
                'Mês': meses[mes],
                'Nome': nome,
                'Nascimento': dados['Nascimento'][idx],
                'Local': dados['Local'][idx],
                'RG': dados['RG'][idx],
                'CPF': dados['CPF'][idx]
            })
    
    df = pd.DataFrame(todos_dados)
    print(f'\n📄 TODOS OS ANIVERSARIANTES (Total: {len(df)}) \n')
    print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=True))

# ============================================
# PROGRAMA PRINCIPAL
# ============================================

def main():
    """Função principal do programa"""
    while True:
        exibir_menu()
        
        try:
            opcao = input('\nEscolha uma opção (1-4): ').strip()
            
            if opcao == '1':
                try:
                    mes = int(input('\nDigite o número do mês (1-12): '))
                    consultar_por_mes(mes)
                except ValueError:
                    print('\n❌ Erro: Digite um número válido!')
            
            elif opcao == '2':
                nome = input('\nDigite o nome (ou parte dele): ').strip()
                if not nome:
                    print('\n❌ Erro: Digite um nome válido!')
                else:
                    buscar_por_nome(nome)
            
            elif opcao == '3':
                listar_todos()
            
            elif opcao == '4':
                print('\n👋 Até logo!')
                break
            
            else:
                print('\n❌ Opção inválida! Escolha 1, 2, 3 ou 4.')
        
        except KeyboardInterrupt:
            print('\n\n👋 Programa interrompido pelo usuário!')
            break
        except Exception as e:
            print(f'\n❌ Erro inesperado: {str(e)}')
        
        input('\nPressione "Enter" para continuar...')

if __name__ == '__main__':
    main()
