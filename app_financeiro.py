import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

# Login
usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")
data = input("Digite a data de hoje (dd/mm/aaaa): ")

# Verifica se o usuário e senha estão corretos
if usuario == 'Tigrão' and senha == 'admin':
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos. Tente novamente.")
    exit()

# Lista de pessoas que estão devendo
pessoas_devendo = []

# Lista de pagamentos registrados com valores
pagamentos = []

# Funções para gerenciar lista de devedores

def adicionar_pessoa_devendo(pessoa):
    if pessoa not in pessoas_devendo:
        pessoas_devendo.append(pessoa)
        print(f"{pessoa} adicionada à lista de devedores.")
    else:
        print(f"{pessoa} já está na lista de devedores.")
def adicionar_pagamentos(pessoa,valor):
    pagamentos.append((pessoa,valor))
    
def exibir_pagamentos():
    if len(pagamentos) == 0:
        print("Nenhum pagamento registrado.")
    else:
        print("Pagamentos registrados:")
        for pagamento in pagamentos:
            print(f"{pagamento[0]} pagou R$ {pagamento[1]:.2f}")

def remover_pessoa_devendo(pessoa):
    if pessoa in pessoas_devendo:
        pessoas_devendo.remove(pessoa)
        print(f"{pessoa} removida da lista de devedores.")
    else:
        print(f"{pessoa} não está na lista de devedores.")

def exibir_pessoas_devendo():
    if len(pessoas_devendo) == 0:
        print("Nenhuma pessoa devendo.")
    else:
        print("Pessoas devendo:")
        for pessoa in pessoas_devendo:
            print(f"- {pessoa}")

def pagar_pessoa_devendo(pessoa, valor):
    if pessoa in pessoas_devendo:
        pagamentos.append((pessoa, valor))
        remover_pessoa_devendo(pessoa)
        print(f"Pagamento de R$ {valor:.2f} registrado para {pessoa}.")
    else:
        print(f"{pessoa} não está na lista de devedores.")

# Menu de opções
while True:
    print("\nMenu:")
    print("1. Adicionar pessoa devendo")
    print("2. Remover pessoa devendo")
    print("3. Exibir pessoas devendo")
    print("4. Adicionar pagamento")
    print("5. Exibir pagamentos")
    print("6. Sair")
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        pessoa = input("Digite o nome da pessoa devendo: ")
        adicionar_pessoa_devendo(pessoa)
    elif opcao == '2':
        pessoa = input("Digite o nome da pessoa a remover: ")
        remover_pessoa_devendo(pessoa)
    elif opcao == '3':
        exibir_pessoas_devendo()
    elif opcao == '4':
        pessoa = input("Digite o nome da pessoa que efetuou o pagamento: ")
        valor = float(input("Digite o valor pago: "))
        adicionar_pagamentos(pessoa, valor)
    elif opcao == '5':
        exibir_pagamentos()
    elif opcao == '6':
        print("Salvando e saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Saldo inicial
saldo_inicial = float(input("Digite o saldo inicial: "))
print(f"Saldo Inicial: R$ {saldo_inicial:.2f}")

# Saldo atual
saldo_atual = saldo_inicial + sum(pagamento[1] for pagamento in pagamentos)
print(f"Saldo Atual: R$ {saldo_atual:.2f}")

# Criação do DataFrame
dados = pd.DataFrame(columns=['Data', 'Descrição', 'Valor'])

# Adicionando transações ao DataFrame
dados.loc[len(dados)] = [data, 'Saldo Inicial', saldo_inicial]
for pagamento in pagamentos:
    dados.loc[len(dados)] = [data, f"Pagamento de {pagamento[0]}", pagamento[1]]

# Exibindo o DataFrame
print("\nDados financeiros:")
print(dados)

# Salvando o DataFrame em CSV
dados.to_csv('dados_financeiros.csv', index=False)
print("Dados salvos no arquivo 'dados_financeiros.csv' com sucesso!")

# Exibindo gráfico
plt.plot(dados.index, dados['Valor'], marker='o')
plt.xlabel('Transações')
plt.ylabel('Valor (R$)')
plt.title('Movimentação Financeira')
plt.grid()
plt.show()

# Carregando o DataFrame de um arquivo CSV
dados_carregados = pd.read_csv('dados_financeiros.csv')

# Exibindo o DataFrame carregado
print("\nDados carregados:")
print(dados_carregados)

# Salvando o DataFrame em um arquivo Excel
dados_carregados.to_excel('dados_financeiros.xlsx', index=False)
print("Dados salvos para Excel com sucesso!")
