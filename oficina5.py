import numpy as np

# Seja bem-vindo ao nosso sistema de análise de atendimento do nosso supermercado!

print("Seja bem-vindo ao nosso sistema de avaliação de atendimento do nosso supermercado!")

# Tempo passado nas filas de atendimento
# Função para coletar informações do aluno

def coletar_informacoes(): 
    dados_historicos = {}

    nome = input("Digite seu nome: ")
    while True:
         try:
             tempo_nas_filas = int(input("Quanto tempo você gasta permanecendo nas filas de atendimento (em minutos)?"))
             tempo_permanencia = int(input("Quanto tempo você gasta permancendo em nosso supermercado (em minutos)?"))
             tempo_saida = int(input("Quanto tempo você leva para sair do seu atendimento (em minutos)?"))
             break
         except ValueError:
              print("Por favor, tente novamente, inserindo um número válido.")

    tempo_total = tempo_nas_filas + tempo_permanencia + tempo_saida
    print(f"Tempo total gasto nas filas de atendimento: {tempo_total}minutos")
  
    dados_historicos['nome'] = nome
    dados_historicos['tempo_nas_filas'] = tempo_nas_filas
    dados_historicos['tempo_permanencia'] = tempo_permanencia
    dados_historicos['tempo_saida'] = tempo_saida
    dados_historicos['tempo_total'] = tempo_total
    
    return dados_historicos 
   
#Função para exibir os dados
def exibir_dados_historicos(dados_historicos):
     print("\nDados Inseridos:") 
     for chave, valor in dados_historicos.items(): 
          print(f"{chave}: {valor}")    

# Coletar informações
informacoes = coletar_informacoes()
exibir_dados_historicos(informacoes)

# Satisfação com o atendimento

satisfacao = int(input("Qual sua satisfação com o atendimento? (de 1 a 10)"))

if satisfacao >= 7:
    print("Obrigado por utilizar nossos serviços!")
else: 
      print("Que pena! Tentaremos melhorar nossos serviços.")           
   
# Feedback dos clientes sobre nossos serviços

resposta = str(input("Deseja nos dar um feedback sobre nossos serviços?"'Sim ou Não'))

if resposta.lower == "Sim":
    feedback = input("Por favor nos diga seu feedback:  ")
    print(f"Obrigado pelo seu feedback: {feedback}")
else: 
   sugestao = input("Obrigado por utilizar nossos serviços! Alguma sugestão? ") 
   print(f"Obrigado pela sua sugestão: {sugestao}")

print("Obrigado pela sua resposta!")

# Respostas dos clientes sobre a nova politica
str(input("Você gostou da nossa nova politica de atendimento?"'Sim ou Não'))
print("Obrigado pela sua contribuição!")

# Dados históricos (hipóteticos) de tempo nas filas de atendimento (em minutos)
dados_historicos = [6, 7, 10, 18, 23]

# Calcular a probabilidade de um cliente esperar mais de 10 minutos na fila
tempos_acima_de_10 =[tempo for tempo in dados_historicos if tempo > 10]
probabilidade_acima_de_10 = len(tempos_acima_de_10) / len(dados_historicos)

print(f"Probabilidade de esperar mais de 10 minutos na fila: {probabilidade_acima_de_10:.2%}")
