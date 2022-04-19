# Objetivos:
# - Aprofundar nas sintaxes básicas;
# - Aprender a utilizar laços de repetição;
# - Criar programas com condicional e laço de repetição

# for x in range(100):
#     print(x)

# método para verificar se um numero é primo
# a = int(input('entre com um número: '))
# div = 0
# # nesse caso o range está incluindo os numero entre o 1 e o a+1
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div += 1
# # um numero para ser considerado primo, ele só poderá ser divisivel por ele mesmo e por 1
# if div == 2:
#     print('número {} é primo' .format(a))
# else:
#     print('número {} não é primo' .format(a))

# # verificar quais numeros são primos
# a = int(input('entre com um valor: '))
# for num in range(a):
#     div = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             div +=1
#     if div == 2:
#         print(num)

a = float(input('primeiro bimestre: '))
while a > 10:
    a = float(input('você digitou errado. \nPrimeiro bimestre: '))
b = float(input('segundo bimestre: '))
while b > 10:
    b = float(input('você digitou errado. \nSegundo bimestre: '))
c = float(input('terceiro bimestre: '))
while c > 10:
    c = float(input('você digitou errado. \nTerceiro bimestre: '))
d = float(input('quarto bimestre: '))
while d > 10:
    d = float(input('você digitou errado. \nQuarto bimestre: '))
media = (a + b + c + d) / 4
if media >= 7:
    print('O aluno foi APROVADO com média: {}'. format(media))
else:
    print('O aluno foi REPROVADO com média: {}'. format(media))