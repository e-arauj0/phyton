# #while
# contador = 10

# while contador >= 1:
#     print(f"contagem atual: {contador}")
#     contador -= 1


# senha = "emily123"
# tentativa_senha = ""

# while tentativa_senha != senha:
#     tentativa_senha = input("Digite a senha: ")

#     if tentativa_senha != senha:
#         print("senha incorreta, digite novamente")
#     else:
#         print("senha correta")

# #for
# compras = ["arroz", "feijão", "macarrão"]
# for item in compras:
#     print(f"voce precisa comprar {item}")

num = [6, 5, 13, 14, 15, 16, 17, 18, 19, 20]

for numero in num:
    if numero %2 == 0:
        continue
    print(numero)
    # else:
    #     print(f"o número {numero} é impar")