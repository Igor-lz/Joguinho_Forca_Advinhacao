print("bem vindo ao jogo de advinhação!")

numero_secreto = 42

chute = input("Digite o seu número")
print("Você digitou: ", chute)
chute = int(chute)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto!")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto!")
