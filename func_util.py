
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
# print(moyenne())
# def moyenne(liste=[]) :
#     somme = sum(liste[:-1])
#     nb_elements = len(liste[:-1])
#     moyenne = (somme / nb_elements + 2* int(liste[-1]))/3
#     return 'moyenne_devoir :', moyenne

def moyenne_devoir(l):
    n = len(l)-1
    s = 0
    for i in range(0,n):
        s = s + float(l[i])
    moy = s/(i+1)
    moy_G = (moy + 2*int(l[-1]))/3
    return 'M_d :',round(moy,2),'M_G :',round(moy_G,2)


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