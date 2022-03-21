import mysql.connector as ps
from func_util import *

def Rollback(data_base):
    db = ps.connect(host="localhost", user="root",
            password="passer", database=f"{data_base}")
    curseur = db.cursor()
    print("""
        1- Pour vider une table
        2- Pour vider toutes les tables
    """)
    choix = int(input(''))
    if choix == 1:
        table = input('Entrer la table à vider\n')
        try:
            curseur = db.cursor()
            r = f"TRUNCATE {table}"
            curseur.execute(r)
            print(f'La table {table} a été vider avec succés')
        except Exception as e:
            print(f"la {table} n'existe pas ",e)
    elif choix == 2:
        try:
            table = []
            i = 1
            while i<5:
                t = input(f'Entrer la {i}e table à vider\n')
                table.append(t)
                if i == 5:
                    break
                i = i + 1
            print(table)
            for i in table:
                print(i)
                curseur = db.cursor()
                curseur.execute(f"TRUNCATE {i}")
            db.commit()
            print('Les tables ont été vidé avec succés')
        except Exception as e:
            print(e)

