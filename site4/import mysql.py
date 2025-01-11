import mysql.connector as cn

conexao=cn.connect(
    host='154.127.218.241',
    user='Todos',
    database='vendas',
    password=''
)
cursor=conexao.cursor()
query='SELECT* FROM producao'
cursor.execute(query)
r=cursor.fetchall()
conexao.commit()
cursor.close()
conexao.close()
print(r)