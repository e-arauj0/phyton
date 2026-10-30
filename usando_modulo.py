# A partir de um arquivo .py podemos puxar outros arquivos
import funcoes

funcoes.comprimento("emily")


from funcoes import comprimento, somar # Importando apenas funções especificas

comprimento("emily")
print(somar(4,5))

# from funcoes import * 
# Está importando todas as funções do arquivo

from minhas_funcoes import funcoes # Quando o arquivo está dentro de uma pasta

from minhas_funcoes.funcoes import somar # Importando funçao especifica de um arquivo numa pasta


