# Objetivos:
# - Saber o que é conjunto;
# - Metodos: união, intersecção, diferença e diferença simétrica
# - remoção de duplicidade de listas utilizando conjuntos

# conjunto = {1, 2, 3, 4}
# conjunto.add(5) # método .add adiciona valores no conjunto
# conjunto.discard(2) # método .discard retira valores do conjunto
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) # método .union serve para unir dois conjuntos
print('União: {}'.format(conjunto_uniao))
conjunto_intersec = conjunto.intersection(conjunto2) # método .intersection serve para mostrar os valores iguais nos conjuntos
print('Interesecção: {}'.format(conjunto_intersec))
conjunto_diferenca1 = conjunto.difference(conjunto2) # método .difference mostra apenas os valores diferentes do conjunto referenciado com relação ao outro
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença1: {}'.format(conjunto_diferenca1))
print('Diferença2: {}'.format(conjunto_diferenca2))
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2) # método .symetric_difference mostra apenas os valores diferentes entre um conjuto e outro
print('Diferença Simérica: {}'. format(conjunto_dif_simetrica))

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b) # método .issubset verifica se o conjunto_a está contido no conjunto_b
conjunto_superset = conjunto_b.issuperset(conjunto_a) # método .issuperset verifica se o conjunto_b é um super conjunto do conjunto_a
print(conjunto_superset)

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print('lista inicial: {}'.format(lista))
conjunto_animais = set(lista) # método set() converte em conjunto
print('Conjunto de Animais: {}'.format(conjunto_animais))
lista_animais = list(conjunto_animais) #método list() converte em lista
print('Lista de animais: {}'.format(lista_animais))