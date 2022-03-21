
import mysql.connector as ps
import csv
tabG = []
with open('Mine.csv', 'r') as f:
    fichier = csv.DictReader(f)
    for i in fichier:
        tabG.append(i)
# print(tabG)


def note_verification(n):
    char = ":;"
    sep = "# "
    sequence = n
    if ',' in n:
        n = n.replace(",", ".")
    for elem in n:
        if elem in char:
            n = n.replace(elem, ",")

    for elem in n:
        if elem in sep:
            n = n.replace(elem, "")
    if str(n):
        n = (" ").join(n.split("["))
        n = (" ").join(n.split("]"))
        n = n.split()
    if len(n) % 2 == 0:
        dictionnaire = {n[i]: [(n[i + 1])] for i in range(0, len(n), 2)}
        dic = {}
        for mat in dictionnaire:
            s = dictionnaire[mat]
            # s1 = dictionnaire['la moyenne est :'] = moy(mat)
            dic[mat] = [e for e in ("").join(s).split(",")if e != '']
        return dic
    else:
        return sequence

# Validité d'une date
def verify_date(c):
    c = c.strip()
    if len(c) == 0:
        return False
    else:
        c = c.split("-")
        # Condition de validité de la date
        # avec si on a pas un jour superieur à 31 et inferieur à 1 etc...
        if int(c[0]) < 1 or int(c[0]) > 31 or int(c[1]) < 1 or int(c[1]) > 12 or ((c[1] == 2) and (int(c[0]) > 29) and (
                (int(c[2]) % 4 == 0 and int(c[2]) % 100 != 0) or int(c[2]) % 400 == 0)) or (
                (int(c[1]) == 2) and (int(c[0]) > 28) and ((int(c[2]) % 4 != 0 or int(c[2]) % 100 == 0) and int(c[2]) % 400 != 0)):
            return False
        return True

# print(note_verification(tabG[0]['Note']))

def date(chaine):
    separator = "/-.,:;_- @]{çà#]}'"
    mois = {"ja": "1", "f": "2", "mars": "3", "av": "4", "mai": "5", "juin": "6",
            "juil": "7", "ao": "8", "sep": "9", "oct": "10", "nov": "11", "dec": "12"}
    chaine = chaine.strip()
    for elem in chaine:
        if elem in separator:
            chaine = chaine.replace(elem, "/")
    chaine = chaine.split("/")
    chaine = [chaine[i] for i in range(len(chaine)) if len(chaine[i]) != 0]
    # print(chaine)
    for keys in mois:
        if len(chaine) > 0:
            if str(chaine[1].lower()).startswith(keys):
                chaine[1] = mois[keys]
                break
    return "-".join(chaine)

def num(c):
    number = [str(i) for i in range(10)]
    if len(c) == 7:
        if c.isupper() and c.isalnum():
            for elem in c:
                if elem in number:
                    True
                    break
    else:
        False
    return c

# verification de la validité du nom d'étudiant

def valide_nom(prenom, nom):
    n = 0
    m = 0
    if (prenom[0].isalpha and nom[0].isalpha):
        for n in nom:
            if n.isalpha:
                n += 1
        for p in prenom:
            if p.isalpha:
                m += 1
        if n >= 2 and m >= 3:
            return True
    else:
        return False

# Fonction pour verifier si un chaine contient une lettre

def lettre(chaine):
    p = 0
    for elem in range(len(chaine)):
        if chaine[elem].isalpha():
            p += 1
    if p >= 1:
        return True
    else:
        return False

def verf(num):
    p = 0
    for elem in num:
        if elem == ".":
            p += 1
    if p >= 2:
        return True
    else:
        return False

def classe(chaine):
    chaine = chaine.strip()
    if len(chaine) == 0:
        return False
    else:
        if chaine[0] in [str(i) for i in range(3, 7)] and chaine[-1] in ["A", "B"]:
            return True
        else:
            return False

def moyenne():
    for notes in [tuple(data[i].get('Note').values()) for i in range(len(data))]:
        for note in notes:
            # print(note)
            n = len(note)-1
            s = 0
            for i in range(0,n):
                s = s + float(note[i])
            moy = s/(i+1)
            moy_G = (moy + 2*int(note[-1]))/3
            return 'Moyenne devoir :',round(moy,2),'Moyenne Generale :', round(moy_G,2)
#
def moyenne_devoir(l):
    n = len(l)-1
    s = 0
    for i in range(0,n):
        s = s + float(l[i])
    moy = s/(i+1)
    moy_G = (moy + 2*int(l[-1]))/3
    return 'M_d :',round(moy,2),'M_G :',round(moy_G,2)

# La validation des conditions
valide = []
invalide = []

for i in range(1, len(tabG)):
    # print(data[i][0])

    if tabG[i]['Note'] != "":
        tabG[i]['Note'] = note_verification(tabG[i]['Note'])
        # print(tabG[i]['Note'])
    if tabG[i]['Date'] != "":
        tabG[i]['Date'] = date(tabG[i]['Date'])
        # print(data[i][3])

    if num(tabG[i]['Numero']) and verify_date(tabG[i]['Date']) and classe(tabG[i]['Classe']):
        if type(tabG[i]['Note']) == str:
            invalide.append(tabG[i])
        else:
            vide = []
            p = 0
            for elem in tabG[i]['Note'].values():
                vide.extend(elem)
            for s in vide:
                if verf(s):
                    p = p + 1
            if p >= 1:
                invalide.append(tabG[i])
            else:
                valide.append(tabG[i])
                # print(valide)
    else:
        invalide.append(tabG[i])
data = valide.copy()
# print(data)



###################################################################################################
###############################     DEBUT DU PROJET SQL    ########################################
###################################################################################################


def Classe_table(datas):
    for i in range(0, len(data)):
        db = ps.connect(host="localhost", user="root",
                password="passer", database="Projet_PythonCSV")
        curseur = db.cursor()
    c = data[i].get('Classe')
    # datas = [
    #     {
    #         "Classe": c
    #     }
    # ]
    datas = [
        {"Classe": '6emeA'},
        {"Classe": '6emeB'},
        {"Classe": '5emeA'},
        {"Classe": '5emeB'},
        {"Classe": '4emeA'},
        {"Classe": '4emeB'},
        {"Classe": '3emeA'},
        {"Classe": '3emeB'},
        {"Classe": 'Tle S2'},
        {"Classe": 'Tle S1'},
        {"Classe": 'Tle l2'},
        {"Classe": "Tle l'"}
]
    for fiche in datas:
        # print(fiche)
        
        curseur.execute("INSERT INTO Classe(nom) VALUES (%(Classe)s)", fiche)
    db.commit()
    # db.close()
Classe_table(data)


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
def Notes_table(data):
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
            curseur.execute("INSERT INTO Notes(note_val,note_type,id_mat) VALUES(%s,%s,%s)", (int(comp), 2, id_mat))


            devoirs = note[k][:-1]
            for dev in devoirs:
                # print(dev)
                curseur.execute("INSERT INTO Notes(note_val,note_type,id_mat) VALUES(%s,%s,%s)",(int(round(float(dev))),1,id_mat))

    db.commit()           

# print(tabMatiere)

####################### Remplissage de la table Matiére #####################################

def Matiere_table(data):
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
def Eleve_table(data):
    for i in range(0, len(data)):
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
# db.close()


def remplir_table():
    try:
        Eleve_table(data)
        Matiere_table(data)
        Notes_table(data)
        Classe_table(data)
    except Exception as e:
        print(e)
############################################## FIN DE SCRIPT #################################################
################################################# TRIGGERS ###################################################

