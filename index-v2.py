nickname = input("Digite o seu nickname para começar a aventura do ranking: ")

print("Olá, " + nickname + ". Seja bem-vindo!")

print("Vamos começar?")

vitorias = int(input("Primeiro, digite o seu número de vitórias: "))

derrotas = int(input("Agora, digite o seu número de derrotas: "))

resultado = vitorias - derrotas

if resultado <= 10:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Ferro")
elif 11 <= resultado <= 20:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Bronze")
elif 21 <= resultado <= 50:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Prata")
elif 51 <= resultado <= 80:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Ouro")
elif 81 <= resultado <= 90:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Diamante")
elif 91 <= resultado <= 100:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Lendário")
elif resultado >= 101:
    print("O herói de nome " + nickname + " tem saldo de " + str(resultado) + " e está no nível de Imortal")
