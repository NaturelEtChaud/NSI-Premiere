from random import randint
import codecs

def syllabe():
    """
    Entrée :
        None
    Sortie :
        syl est une chaîne de caractères
    Post-conditions :
        syl est une syllabe qui respecte les règles pour la création d'un nom d'un ewok
    """
    voyelles = 'aeiouy'
    consonnes = 'bcdfghjklmnpqrstvwxz'
    c = randint(0,19)
    v1 =  randint(0,5)
    v2 =  randint(0,5)
    return consonnes[c] + voyelles[v1] + voyelles[v2]

def ewok_masculin():
    """
    Entrée :
        None
    Sortie :
        nom est une chaîne de caractères
    Post-conditions :
        nom doit être le nom masculin d'un ewok
    """
    voyelles = 'aeiouy'
    consonnes = 'bcdfghjklmnpqrstvwxz'
    nom = ''
    for i in range(2):
        nom = nom + syllabe()
    # on a une chance sur deux de rajouter une consonne
    if randint(0,1)==0 :
        c = randint(0,19)
        nom = nom + consonnes[c]
    return nom

def ewok_feminin():
    """
    Entrée :
        None
    Sortie :
        nom est une chaîne de caractères
    Post-conditions :
        nom doit être le nom féminin d'un ewok
    """
    nom = ''
    nb_syllabes = randint(2,3)
    for i in range(nb_syllabes):
        nom = nom + syllabe()
    return nom

################################
# Création de la liste dans un fichier
################################
f = codecs.open('ewoks.txt', 'w', 'utf-8')

f.write("Liste de 40 noms d'Ewoks créés alétoirement\r\n")
f.write("\r\n"*2)
f.write("20 noms féminins :\r\n")
f.write('\r\n')
for i in range(20):
    nom = ewok_feminin()
    f.write(nom+'\r\n')
f.write("\r\n"*2)
f.write("20 noms masculins :\r\n")
f.write('\r\n')
for i in range(20):
    nom = ewok_masculin()
    f.write(nom+'\r\n')
f.close()