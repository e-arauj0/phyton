
# def ola(nome):
#     print("olá {nome}")

# ola() #exibindo o que a função pede

# def ola(nome):
#     print(f"olá {nome}")

# nome_inserido = input("Digite seu nome: ")
# ola(nome_inserido) #chamando função especifica

#funçao de soma 
def somar(n1,n2):
    #escopo local
    operacao = n1 + n2
    return operacao 

#variaveis definidas dentro de uma função podem ser usadas apenas dentro da função, não pode ser utilizada fora dela, por isso criamos a variável resultado

#variaveis criadas fora da função podem ser usadas dentro delas, são chamadas de escopo global

resultado = somar(5,6) #chamando função especifica
print(f"resultado da soma: {resultado}")

#módulos
def comprimento(nome):
    print(f"olá {nome}")