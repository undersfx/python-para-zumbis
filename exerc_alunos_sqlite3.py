import sqlite3

#Conexão com banco SQLite
con = sqlite3.connect("alunos.bd")

#Criação de Cursor para requisoções SQL
cur = con.cursor()

#Querys
#cur.execute('create table alunos(login varchar(8), ra integer)')
#cur.execute('insert into alunos values("massanori", 42)')
#cur.execute('insert into alunos values("thiago", 1)')
cur.execute('select * from alunos')

#Pegar todos valores da última chamada
for x in cur.fetchall():
    print(x)
    
cur.close()

#Salva alterações (nos caso de create e insert)
con.commit()

con.close()