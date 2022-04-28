# -*- coding : utf-8 -*-
import codecs #pour lire en UTF8, n'est pas toujours nécessaire
import csv

##############################################
# récupération des données
##############################################

heros = []

with codecs.open('characters.csv', 'r', 'utf-8') as fichier:
    csvheros = csv.DictReader(fichier, delimiter=',')
    for ligne in csvheros:
        heros.append(dict(ligne))

HtoC = []

with codecs.open('charactersToComics.csv', 'r', 'utf-8') as fichier:
    csvHtoC = csv.DictReader(fichier, delimiter=',')
    for ligne in csvHtoC:
        HtoC.append(dict(ligne))

comics = []

with codecs.open('comics.csv', 'r', 'utf-8') as fichier:
    csvcomics = csv.DictReader(fichier, delimiter=',')
    for ligne in csvcomics:
        comics.append(dict(ligne))

#pour vérification on affiche les premières données
#print(heros[:2])
#print(HtoC[:2])
#print(comics[:2])



##############################################
# recherche de l'id de Kitty Pryde
##############################################

i = 0
trouvee = False
while i<len(heros) and (trouvee == False) :
    if heros[i]['name'] == 'Kitty Pryde':
        trouvee = True
    else :
        i += 1

idKitty = heros[i]['characterID']
#vérification
print(idKitty)


##############################################
# recherche des idComics avec Kitty Pryde
##############################################
idComics = [h['comicID'] for h in HtoC if h['characterID']==idKitty]

#vérification
#print(idComics, len(idComics))


##############################################
# création de la liste  des comics avec Kitty Pryde
##############################################
comicsK = []

for id in idComics:
    i=0
    trouvee = False
    while i<len(comics) and (trouvee == False) :
        if comics[i]['comicID'] == id:
            trouvee = True
        else :
            i += 1
    comicsK.append(comics[i]['title'])

#vérification
print(comicsK[:5],len(comicsK))
