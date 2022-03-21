from func_util import *
import mysql.connector as ps
from func_util import Classe_table, Eleve_table, Matiere_table, Notes_table
from Rollback import *

# Connection à la base de données
db = ps.connect(host="localhost", user="root",password="passer", database="Projet_PythonCSV")
curseur = db.cursor()
# Appel des fonctions pour l'insertion à la base de données
print("""
        ######### #   ##   ######  ##    ##  ##       #  #######  ##    ##  ##     #  #######
        ###        #  ##   ##      ###   ##   ##     #   ##       ###   ##  ##     #  ##
        ######### #   ##   #####   ## #  ##    ##   #    ######   ## #  ##  ##     #  #####      
        ###        #  ##   ##      ##  # ##     ## #     ##       ##  # ##  ##     #  ##
        ###########   ##   ######  ##   ###      ##      #######  ##   ###  ########  #######
    """)

try: 
    c = 'Y'
    while c == 'Y' or c == 'y' or c == 'yes':
        print("""
            1- Afficher les tables disponibles
            2- Pour voir le menu principale en detail
        """)
        choix = int(input('Faites le choix\n'))
        if choix == 1:
            curseur.execute("SHOW TABLES")
            show_table = curseur.fetchall()
            for tables in show_table:
                print('==>',tables[0])
            db.commit()
        elif choix == 2:
            print("""
                1- Afficher la table 
                2- Faire le Vidance des tables au choix
                3- Remplir les tables
                4- Pour Quitter
            """)
            choice = int(input('')) 
            if choice == 1:
                TAB = input('Choisir la table à voir\n')
                requete = f"SELECT * FROM {TAB}"
                curseur.execute(requete)
                show_table = curseur.fetchall()
                for element in show_table:
                    print('==> ',element)
                db.commit()
            elif choice == 2:
                Rollback("Projet_PythonCSV")
            elif choice == 3:
                remplir_table()
            elif choice == 4:
                break
        c = input('Voulez-vous continuer à explorer le menu \nTaper (Y|y) pour dire yes | N pour dire non\n')
except Exception as e:
    print(e)
