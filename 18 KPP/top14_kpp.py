import codecs #pour lire en UTF8, n'est pas toujours nécessaire
import csv

joueurs = []

with codecs.open('top14.csv', 'r', 'utf-8') as fichier:
    csvtop14 = csv.DictReader(fichier, delimiter=',')
    for ligne in csvtop14:
        joueurs.append(dict(ligne))

#pour vérification on affiche le premier joueur
print(joueurs[0])

#fonction distance
def dist(A,B):
    '''
    A[0] est l'abscisse du point
    A[1] est l'ordonnée du point
    '''
    calcul = (B[0]-A[0])**2 + (B[1]-A[1])**2
    calcul = calcul**0.5
    return calcul

def kpp(poids, taille, joueurs,k):
    #liste des kpp
    voisins = [[100000,"coupeur de citron"] for i in range(k)]
    #l'idée est que cette liste sera toujours ordonnée dans l'ordre croissant
    #donc le dernier élément est à la plus grande distance

    A = [poids, taille]
    for j in joueurs :
        B = [int(j['Poids']),int(j['Taille'])]
        calcul = dist(A,B)
        if calcul < voisins[k-1][0] :
            #j est plus proche que le voisin le plus éloigné
            #il devient un nouveau voisin
            voisins[k-1][0] = calcul
            voisins[k-1][1] = j['Poste']
        #on reordonne la liste des voisins
        voisins.sort()
    return [v[1] for v in voisins]
