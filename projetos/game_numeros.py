import time

dificuldade = int(input("Escolha a difiuldade: "))
sim_nao = input("Deseja continuar?: ")
erro = ""
palpite = int(input("Digite seu palpite"))

while erro != 1:
    numero_aleatorio = random.randint(1, 50)

    if numero_aleatorio 