# Objetivos:
# - Saber como criar, manipular e realizar operações com listas;
# - Saber o que uma tuplas, interagir com tuplas;
# - Conversões de listas e tuplas

lista = [1, 3, 5, 7]
# print(sum(lista))#realiza a soma dos itens da lista
# print(max(lista))#verifica qual o maior numero da lista
# print(min(lista))#verifica qual o menor numero da lista
lista_animal = ['cachorro', 'gato', 'elefante']
# print(max(lista_animal)) #vai immprimir "gato" pois começa com G
# print(lista_animal[1]) # imprime item especifico da lista
# for x in lista_animal:# irá imprimir todos os itens da lista
#     print(x)

# soma = 0
# for x in lista:#passará por todos itens a lista e somará ao valor da variável "soma"
#     soma +=x
# print(soma)

# if 'lobo' in lista_animal: #é possível fazer um if desta forma
#     print('exixte um lobo na lista')
# else:
#     print('não existe um lobo na lista. será incluido.')
#     lista_animal.append('lobo')#adiciona um valor na lista_animal

# # lista_animal.pop()  # retira um valor da lista conforme indice ex: lista_animal.pop(0) 
#                     # vai retirar o cachorro. se não especificar retira-rá o último.

# # lista_animal.remove('elefante') # para remover um item que já seja conhecido use o .remove('valor')

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
# lista_animal.reverse()

tupla = (1, 10, 12, 14) #a tupla é uma lista entre parenteses e não podem ser alterados
print(len(lista))
print(len(lista_animal))
tupla_animal = tuple(lista_animal) # conversao de lista em tupla
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla) # conversao de tupla em lista
print(type(lista_numerica))
lista_numerica[0] = 100 # modificando o valor no indice [0]
print(lista_numerica)