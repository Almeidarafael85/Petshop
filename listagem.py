#Crie um script que fará a listagem de alunos

import mysql.connector

try:
   conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'escola',
    port = '3306',
   )
   print('Conectado com Sucesso!')
   sql = "select * from aluno order by nome desc"
   cursor = conexao.cursor(dictionary=True)
   cursor.execute(sql)
   for aluno in cursor:
      print(f'{aluno["nome"]}')
      print(f'{aluno["nota1"]} - {aluno["nota2"]}') 
except:
   print('Erro ao conectar!')
finally:
   if conexao != None:
      conexao.close()
