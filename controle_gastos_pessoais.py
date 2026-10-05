"""
Projeto: Controle de Gastos Pessoais
Programa de terminal para registrar e consultar gastos pessoais.
"""

# Lista global que armazena todos os gastos registrados.
# Cada gasto é um dicionário com as chaves: 'descricao', 'valor' e 'categoria'.
gastos = []


def adicionar_gasto():
    """
    Pede ao usuário descrição, valor e categoria de um gasto,
    valida se o valor é positivo (maior que zero) e adiciona
    o novo gasto na lista global 'gastos'.
    """
    descricao = input('Descrição do gasto: ')
    valor = float(input('Valor gasto: '))

    # Enquanto o valor informado for inválido (<= 0), pede novamente.
    while valor <= 0:
        print('O valor adicionado precisa ser no mínimo R$1,00!!')
        valor = float(input('Valor gasto: '))

    categoria = input('Categoria: ')

    # Monta o dicionário com os dados do novo gasto.
    novo_gasto = {
        'descricao': descricao,
        'valor': valor,
        'categoria': categoria
    }

    # Adiciona o novo gasto na lista global (sem recriar a lista).
    gastos.append(novo_gasto)