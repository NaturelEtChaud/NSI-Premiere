import codecs #pour lire en UTF8, n'est pas toujours nécessaire
import csv

joueurs = []

with codecs.open('top14.csv', 'r', 'utf-8') as fichier:
    csvtop14 = csv.DictReader(fichier, delimiter=',')
    for ligne in csvtop14:
        joueurs.append(dict(ligne))

# pour vérification on affiche le premier joueur
print(joueurs[0])

# fonction distance
def dist(A,B):
    '''
    A[0] est l'abscisse du point
    A[1] est l'ordonnée du point
    même chose pour le point B
    '''
    pass

# fonction pour déterminer les k plus proches voisins
def kpp(poids, taille, joueurs, k):
    '''
    renvoie la liste des postes des k plus proches voisins de l'individu ayant le poids et la taille donnés en argument
    '''
    pass
