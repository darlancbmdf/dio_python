# para que haja interação com usuário usasse o comand input(), conforme exemplo abaixo
a = eval(input('entre com o valor de a: '))
b = eval(input('entre com o valor de b: '))
soma = a + b
sub = a - b
mult = a * b
div = a / b
rest = a % b
# o comando "type" mostra qual tipo de dado a variável está guardando
print(type(soma))
# quanto você define o tipo de dado como no exemplo abaixo "print('soma: ' + str(soma))", 
# você convertea variável do tipo int para str
print('soma: ' + str(soma))
# no caso de interagir duas varáveis de tipo diferente, se não houver conversão
# haverá um erro. A solução é fazer a conversão da variável em tempo de execução
x = '1'
soma2 = int(x) + 1
print(soma2)
# o comando "format(var)" é utilizado para concatenar na string sem necessidadede conversão da variável
resultado = f'Soma: {soma} \tSubtracao: {sub} \tMultiplicação: {mult} \tDivisão: {div} \tResto: {rest}'
print(resultado)
