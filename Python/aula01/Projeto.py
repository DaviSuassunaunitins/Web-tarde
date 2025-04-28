import random
numRandom = random.randint(1, 100)
num = 0
tentativas = 0
while num != numRandom:
    tentativas += 1
    num = int(input("Digite um número: "))
    if (num > numRandom):
        print("O número digitado é maior do que o sorteado.")
    elif (num < numRandom):
        print("O número digitado é menor do que o sorteado")
print("Você acertou o número!")
print("Você precisou de " + str(tentativas) + " tentativa(s)!")
