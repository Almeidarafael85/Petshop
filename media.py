#Faça calculo da média para cada aluno e informe se o mesmo esta aprovado, se a média for maior ou igual a 7, senão, vai escrever reprovado
# Pedro 5 - 9 - cálculo da média - Situação

import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='escola',
        port=3306
    )
    print('Conectado com Sucesso!')

    cursor = conexao.cursor()
    cursor.execute("SELECT nome, nota1, nota2, nota3 FROM aluno")

    for nome, nota1, nota2, nota3 in cursor:
        media = (nota1 + nota2 + nota3) / 3
        status = "Aprovado" if media >= 7 else "Reprovado"
        print(f"{nome} - Média: {media:.2f} - {status}")

    cursor.close()
    conexao.close()

except mysql.connector.Error as erro:
    print(f'Erro ao conectar: {erro}')
