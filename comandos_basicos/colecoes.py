#listas
frutas = ["maçã", "banana", "laranja", "uva"]

print(frutas[0])  # Acessando o primeiro elemento da lista
print(frutas[1])  # Acessando o segundo elemento da lista

frutas[1] = "abacaxi"  # Modificando o segundo elemento da lista
print(frutas)  # Printando a lista modificada

frutas.append("morango") # Adicionando item a lista (entra no fim)
print(frutas)

frutas.insert(0, "kiwi") # Adicionando item a lista (entra no começo)

frutas.remove("abacaxi") # Removendo item da lista (remove o primeiro item que encontrar)
print(frutas)

if "uva" in frutas:  # Verificando se o item está na lista
    print("uva está na lista")

#tupla (é imutável)
cores = ("vermelho", "azul", "verde")

if "vermelho" in cores:
    print("vermelho está nas cores")

#cores[1] = rosa 
# Isto resulta em um erro pois a tupla é imutável

minhas_tuplas = [("maça", "banana", "abacaxi"), ("vermelho", "azul", "rosa")]

print(minhas_tuplas)

print(minhas_tuplas[0][1])  # Acessando o segundo elemento da primeira tupla'

#dicionários
dados = {"nome": "emily", "idade": 20}
print(dados) # Exibe o dicionário criado
print(dados["nome"]) # Acessando o valor associado à chave "nome"
print(dados["idade"]) # Acessando o valor associado à chave "idade"

dados["idade"] = 23 # Modificando o valor associado à chave "idade"
print(dados) # Exibe o dicionário atualizado

