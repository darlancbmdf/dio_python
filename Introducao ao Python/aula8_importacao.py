from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste #importando método diretamente

if __name__ == '__main__':
  televisao = Televisao()
  print(televisao.ligada)
  televisao.power()
  print(televisao.ligada)
  calculadora = Calculadora(5,10)
  print(calculadora.soma())
  televisao.diminui_canal()
  televisao.aumenta_canal()
  print(f'o canal altual é:{televisao.canal}')
  lista = ['cachorro', 'gato', 'elefante']
  print(contador_letras(lista))
  print(teste())