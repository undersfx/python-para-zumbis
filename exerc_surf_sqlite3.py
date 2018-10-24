import sqlite3

banco = sqlite3.connect("surfersDB.sdb")
banco.row_factory = sqlite3.Row
cursor = banco.cursor()
#cursor.execute("select * from surfers where age > 25")
cursor.execute('''
                select * 
                from surfers 
                where age > 20
                order by average desc
                ''')
linhas = cursor.fetchall()

for linha in linhas:
    print('Nome :', linha['name'])
    print('Pais :', linha['country'])
    print('Media :', linha['average'])
    print('Estilo :', linha['board'])
    print('Idade :', linha['age'])
    print()

cursor.close