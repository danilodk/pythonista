# 🔍 Consulta de Aniversariantes - Igreja Reviver

[![Python 3.x](https://img.shields.io/badge/python-3.x+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Active](https://img.shields.io/badge/status-active-success.svg)](#)

> Um sistema robusto e intuitivo para consulta, busca e gerenciamento de aniversariantes da Igreja Reviver, desenvolvido em Python com interface interativa.

## 🌟 Destaques

- ✅ **Menu Interativo**: Interface amigável com 4 opções de consulta
- 🔍 **Busca Avançada**: Procure pessoas pelo nome em todo o banco de dados
- 📄 **Listagem Completa**: Visualize todos os aniversariantes cadastrados
- 📅 **Consulta por Mês**: Veja aniversariantes de qualquer mês específico
- 🎨 **Formato Elegante**: Apresentação dos dados em tabelas bem formatadas
- ⚠️ **Tratamento de Erros**: Validação robusta e mensagens de feedback
- 📚 **Código Limpo**: Estrutura modular com funções bem documentadas

## 🚀 Funcionalidades

### 1. **Consultar Aniversariantes por Mês**
Ver todos os aniversariantes de um mês específico com informações completas:
- Nome
- Data de Nascimento
- Local
- RG
- CPF

### 2. **Buscar Pessoa por Nome**
Realizar busca flexibilizada pelo nome em todo o banco de dados:
- Suporta buscas parciais
- Case-insensitive (ignora maiúsculas/minúsculas)
- Retorna todos os resultados encontrados

### 3. **Listar Todos os Aniversariantes**
Visualizar o banco de dados completo organizado por mês com contagem total de registros.

### 4. **Menu Principal**
Sistema intuitivo com seleção numérica de opções e validação de entrada.

## 📂 Estrutura do Projeto

```
pythonista/
├── README.md          # Este arquivo
├── aniversario.py     # Código principal do programa
└── requirements.txt   # Dependências do projeto
```

## 🔧 Requisitos

- **Python**: 3.7+
- **Bibliotecas**:
  - `pandas` - Manipulação e processamento de dados
  - `tabulate` - Formatação elegante de tabelas

## 💻 Instalação

### Clonar o Repositório

```bash
git clone https://github.com/danilodk/pythonista.git
cd pythonista
```

### Instalar Dependências

```bash
pip install -r requirements.txt
```

Ou instale as bibliotecas individualmente:

```bash
pip install pandas tabulate
```

## 🌐 Como Usar

### Executar o Programa

```bash
python aniversario.py
```

### Menu de Opções

```
============================================================
*** SISTEMA DE CONSULTA DE ANIVERSARIANTES ***
*** Igreja Reviver ***
============================================================

1. Consultar aniversariantes por mês
2. Buscar pessoa por nome
3. Listar todos os aniversariantes
4. Sair

------------------------------------------------------------
Escolha uma opção (1-4):
```

### Exemplos de Uso

#### Opção 1: Consultar por Mês
```
Digite o número do mês (1-12): 6

🎆 Aniversariantes de JUNHO 🎆

Total: 2 pessoa(s)
```

#### Opção 2: Buscar por Nome
```
Digite o nome (ou parte dele): danilo

🔍 Resultado(s) da busca por: "danilo"

Total: 1 resultado(s) encontrado(s)
```

## 📚 Estrutura do Código

### Funções Principais

| Função | Descrição |
|--------|----------|
| `exibir_menu()` | Exibe o menu principal do programa |
| `consultar_por_mes(numero_mes)` | Consulta aniversariantes de um mês específico |
| `buscar_por_nome(nome_busca)` | Busca pessoas pelo nome em todo o banco |
| `listar_todos()` | Lista todos os aniversariantes cadastrados |
| `main()` | Função principal com loop interativo |

### Banco de Dados

O programa utiliza um dicionário estruturado para armazenar informações:

```python
dados_aniversarios = {
    1: {  # Janeiro
        'Nome': [...],
        'Nascimento': [...],
        'Local': [...],
        'RG': [...],
        'CPF': [...]
    },
    # ... mais meses
}
```

## 👤 Autor

**Danilo Araújo**
- GitHub: [@danilodk](https://github.com/danilodk)

## 📜 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 🐛 Issues e Sugestões

Tem uma sugestão ou encontrou um bug? [Abra uma issue!](https://github.com/danilodk/pythonista/issues)

## 🚀 Melhorias Futuras

- [ ] Adicionar mais meses de dados ao banco de dados
- [ ] Exportar dados para CSV ou Excel
- [ ] Interface gráfica (GUI) com Tkinter ou PyQt
- [ ] Banco de dados persistente (SQLite/PostgreSQL)
- [ ] Sistema de autenticação para gerenciamento
- [ ] API REST para integrações
- [ ] Testes unitários automatizados
- [ ] Documentação adicional em Sphinx

## 📋 Últimas Atualizações

### v2.0.0 (Dezembro 2025)
- ✔️ Refatoração completa do código
- ✔️ Arquitetura modular com funções
- ✔️ Adicionada busca avançada por nome
- ✔️ Melhorado tratamento de erros
- ✔️ Interface do menu mais intuitiva

### v1.0.0
- Versão inicial do projeto

---

**🚀 Desenvolvido com ❤️ em Python**
