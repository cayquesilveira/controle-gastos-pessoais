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

def listar_gastos():
    """
    Imprime todos os gastos registrados, formatados como:
    - Descrição: R$ Valor (Categoria)
    Se não houver nenhum gasto, avisa o usuário.
    """
    if len(gastos) == 0:
        print('Ainda não foram adicionados gastos na lista')
    else:
        for gasto in gastos:
            descricao = gasto['descricao']
            valor = gasto['valor']
            categoria = gasto['categoria']
            print(f'- {descricao}: R$ {valor:.2f} ({categoria})')


# --- Chamadas de teste (remover ou comentar depois que o menu estiver pronto) ---
adicionar_gasto()
listar_gastos()