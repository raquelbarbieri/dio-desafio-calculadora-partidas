
nickname = input("Digite o seu nickname para usar a Calculadora de Ranking: ")
print(f"Olá, herói {nickname}. Seja bem-vindo!")

import time
time.sleep(1)

print("Vamos começar?")

time.sleep(2)

vitorias = int(input("Primeiro, digite o seu número de vitórias: "))

derrotas = int(input("Agora digite o seu número de derrotas: "))

print("Legal! Estou calculando o seu saldo de vitórias e a sua posição no ranking...")

time.sleep(3)

resultado = vitorias - derrotas 

nivel = ""

if resultado <= 10:
  nivel = "Ferro"
elif 11 <= resultado <= 20:
  nivel = "Bronze"
elif 21 <= resultado <= 50:
  nivel = "Prata"
elif 51 <= resultado <= 80:
  nivel = "Ouro"
elif 81 <= resultado <= 90:
  nivel = "Diamante"
elif 91 <= resultado <= 100:
  nivel = "Lendário"
else: 
  nivel = "Imortal"  

print(f"O herói tem saldo de {resultado} e está no nível de {nivel}")

time.sleep(2)

posicao = ""

if nivel == "Ferro":
  posicao = 7
elif nivel == "Bronze":
  posicao = 6
elif nivel == "Prata":
  posicao = 5
elif nivel == "Ouro":
  posicao = 4
elif nivel == "Diamante":
  posicao = 3
elif nivel == "Lendário":
  posicao = 2
else:
  posicao = 1

print(f"{nickname} está na posição {posicao} no ranking.")
