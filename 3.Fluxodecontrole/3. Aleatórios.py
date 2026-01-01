import random

pergunta = input("Me faça qualquer pergunta: ")

num = random.randint(1, 8)

if num == 1:
    resposta = "Sim - definitivamente"
elif num == 2:
    resposta = 'É bem assim'
elif num == 3:
    resposta = 'Sem dúvida'
elif num == 4:
    resposta = 'Resposta vaga, tente novamente'
elif num == 5:
    resposta = 'Pergunte mais tarde'
elif num == 6:
    resposta = 'Melhor não contar agora'
elif num == 7:
    resposta = 'Minhas fontes dizem não'
elif num == 8:
    resposta = 'Perspectiva não é boa'

print(f"Pergunta: {pergunta}")
print(f"Resposta: {resposta}")