from func_util import *


############################################################################################
###############################     DEBUT DU PROJET SQL    ########################################
############################################################################################


for k in tabG:
    # k['Note'] = note_verification(k['Note'])
    k['Date'] = date(k['Date'])
    # print(k['Date'])


for i in range(0, len(data)):
    db = ps.connect(host="localhost", user="root",
                    password="passer", database="Projet_PythonCSV")
    curseur = db.cursor()
    numero = data[i].get('Numero')
    nom = data[i].get('Nom')
    prenom = data[i].get('Prénom')
    notes = data[i].get('Note')
    # requete = """INSERT INTO moyenne
    # (
    #     id_eleve INTEGER NOT NULL,
    #     moy VARCHAR(100) NOT NULL,
    #     id_classe INTEGER NOT NULL
    # )
    # """
    # # INSERTION DES EXAMENS
    # for note in notes.values():
    #     moyenne = moyenne_devoir(note)
    #     moy = moyenne[1]
    #     curseur.execute("INSERT INTO Notes(id_eleve,moy,id_classe) VALUES(%s)", (moy,))

    dates = data[i].get('Date')
    datas = [
        {
            "Nom": nom,
            "prenom": prenom,
            "Date": dates
        }
    ]
    for fiche in datas:
        # print(fiche)
        curseur.execute("INSERT INTO Eleve(nom,prenom,dates) VALUES (%(Nom)s,%(prenom)s,%(Date)s)", fiche)
    db.commit()
    db.close()


for i in range(0, len(data)):
    # print((i))
    db = ps.connect(host="localhost", user="root",
                    password="passer", database="Projet_PythonCSV")
    curseur = db.cursor()
    c = data[i].get('Classe')
    datas = [
        {
            "Classe": c
        }
    ]
    for fiche in datas:
        # print(fiche)
        curseur.execute("INSERT INTO Classe(nom) VALUES (%(Classe)s)", fiche)
    db.commit()
    db.close()

# print('Nice')

########## DEBUT TAB MATIERE ##########
db = ps.connect(host="localhost", user="root",
                password="passer", database="Projet_PythonCSV")
curseur = db.cursor()
query = "SELECT * FROM Matiere"
curseur.execute(query)
tabMat = curseur.fetchall()
# print(tabMat)

def idmat(mat):
    for tab in tabMat:
        if tab[0] == mat:
            return tab[1]


########## FIN TAB MATIERE ##########
db = ps.connect(host="localhost", user="root",password="passer", database="Projet_PythonCSV")
curseur = db.cursor()
for i in range(0, len(data)):
    
    note = data[i].get('Note')
    nume = data[i]['Numero']
    # print(nume)
    # print(note)
    for k in note:
        # print(note[k])
        comp = note[k][-1]
        id_mat = idmat(k)
        if id_mat is None:
            id_mat = 2
        # print(k, id_mat)
        # insert_compo = "INSERT INTO Notes(note_val,note_type,id_mat,numero) VALUES(%s,%s,%s,%s)", (int(comp), 2, id_mat, nume)
        curseur.execute("INSERT INTO Notes(note_val,note_type,id_mat,numero) VALUES(%s,%s,%s,%s)", (int(comp), 2, id_mat, nume))


        devoirs = note[k][:-1]
        for dev in devoirs:
            # print(dev)
            curseur.execute("INSERT INTO Notes(note_val,note_type,id_mat,numero) VALUES(%s,%s,%s,%s)",(int(round(float(dev))),1,id_mat,nume))
db.commit()           

"""
        for mat in tabMat:
            if mat[0] == k:
                id_mat = mat[1]
                # print(id_mat)

        devs = note[k][:-1]
        curseur.execute("INSERT INTO Notes(note_val,note_type,id_mat,numero) VALUES(%s,%s,%s,%s)", (int(comp), 2, id_mat, nume))


    for dev in devs:
        curseur.execute("INSERT INTO Notes(note_val,note_type,id_mat,numero) VALUES(%s,%s,%s,%s)",(int(round(float(dev))),1,id_mat,nume))


db.commit()




##################  Recgulation des matiéres avec éliminations dses doublons :############################
db = ps.connect(host="localhost", user="root",
                password="passer", database="Projet_PythonCSV")
curseur = db.cursor()
tabMatiere = []
for d in range(len(data)):
    notes = data[d].get('Note')
    for key in notes.keys():

        if key.startswith('F'):
            key = "Français"
        if key.startswith('A'):
            key = 'Anglais'

        if key.startswith('M'):
            key = 'Math'
        if key == 'Science_Physique':
            key = 'PC'

        if key not in tabMatiere:
            tabMatiere.append(key)
            # key = (key,)
            # curseur.execute("INSERT INTO Matiere(nom_matiere) VALUES(%s)",(key,))

# db.commit()
"""
# print(tabMatiere)

####################### Remplissage de la table Matiére #####################################

db = ps.connect(host="localhost", user="root",
                password="passer", database="Projet_PythonCSV")
curseur = db.cursor()
tabMatiere = []
for d in range(len(data)):
    notes = data[d].get('Note')
    for key in notes.keys():

        if key.startswith('F'):
            key = "Français"
        if key.startswith('A'):
            key = 'Anglais'

        if key.startswith('M'):
            key = 'Math'
        if key == 'Science_Physique':
            key = 'PC'

        if key not in tabMatiere:
            tabMatiere.append(key)
            curseur.execute(
                "INSERT INTO Matiere(nom_matiere) VALUES(%s)", (key,))
db.commit()

# print(tabMatiere)

################################  Remplissage de la table Eleve #######################################
for i in range(0, len(data)):
    # print((i))
    db = ps.connect(host="localhost", user="root",
                    password="passer", database="Projet_PythonCSV")
    curseur = db.cursor()
    numero = data[i].get('Numero')

    nom = data[i].get('Nom')
    prenom = data[i].get('Prénom')
    dates = data[i].get('Date')
    datas = [
        {
            "Nom": nom,
            "prenom": prenom,
            "Date": dates
        }
    ]
    for fiche in datas:
    	# print(fiche)
    	curseur.execute("INSERT INTO Eleve(nom,prenom,dates) VALUES (%(Nom)s,%(prenom)s,%(Date)s)", fiche)
db.commit()
db.close()
############################################## FIN DE SCRIPT #################################################
