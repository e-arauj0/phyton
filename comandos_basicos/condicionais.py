idade = int(input("Digite sua idade: "))

#condicional simples
if idade >= 18:
    print("liberado")

if idade < 0: 
    print("idade não existe")

else: 
    print("recusado")

#boleanos (verificação)
print(5 < 2) #false
print(5 > 2) #true 

#condicional de string
senha = "emily123"
tentativa_senha = input("Digite a senha: ")

if tentativa_senha == senha:
    print("senha correta")
else:
    print("senha incorreta")

#condicional elif

nota = float(input("Digite sua nota: "))

if nota >= 6:
    print("aprovado")
elif nota< 6 and nota >= 4:
    print("recuperação")
else:
    print("reprovado")


