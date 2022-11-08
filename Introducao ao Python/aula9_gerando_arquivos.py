import shutil

def escrever_arquivo(nome_arquivo, texto):
  arquivo = open(nome_arquivo, 'w') #  'w" => write (criação do arquivo, limpa o arquivo e insere as novas informações)
  arquivo.write(texto)
  arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
  arquivo = open(nome_arquivo, 'a') # 'a' => add (adicionar no arquivo, não limpa o que tem no arquivo)
  arquivo.write(texto)
  arquivo.close()

def ler_arquivo(nome_arquivo):
  arquivo = open(nome_arquivo, 'r') # 'r' => read (lê o que tem no arquivo)
  texto = arquivo.read()
  print(texto)

def media_notas(nome_arquivo):
  arquivo = open(nome_arquivo, 'r')
  aluno_nota = arquivo.read()
  # print(aluno_nota)
  aluno_nota = aluno_nota.split('\n')
  # print(aluno_nota)
  lista_media = []
  for x in aluno_nota:
    lista_notas = x.split(',')
    aluno = lista_notas[0]
    lista_notas.pop(0)
    media = lambda notas: sum([int(i) for i in notas])/4
    # print(aluno)
    # print(media(lista_notas))
    lista_media.append({aluno:media(lista_notas)})
  return lista_media

def copia_arquivo(nome_arquivo): #método resposável por fazer cópia do arquivo em uma outra pasta
  shutil.copy(nome_arquivo, '/pastanova')

def move_arquivo(nome_arquivo): #método resposável por mover o arquivo para uma outra pasta
  shutil.move(nome_arquivo, '/pastanova')


if __name__ == '__main__':
  copia_arquivo('notas.txt')
  # move_arquivo('notas.txt')
  # lista_media = media_notas('notas.txt')
  # print(lista_media)
  # escrever_arquivo('teste.txt', 'Primeira linha. \n')
  # aluno = 'Bernardo4, 10, 10, 9, 9'
  # atualizar_arquivo('notas.txt', aluno)
  # ler_arquivo('teste.txt')