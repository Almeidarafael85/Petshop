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
   sql = "select * from funcionarios order by nome"
   cursor = conexao.cursor()
   cursor.execute(sql)
   for pessoa in cursor:
      print(pessoa)
except:
   print('Erro ao conectar!')   