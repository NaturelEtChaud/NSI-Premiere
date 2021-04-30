# Projet - Message caché

Ce projet va être donné à mes élèves début mai 2021. Il est pour le moment en *work in progress*.

Je depose ici ma version de ce travail que je vais effectuer en parallèle de leur travaux.

### Mots-clefs
Python, module pillow, Chaîne de caractères, Binaire, Opérateurs logiques, Cryptographie, Image, Composante (R,V,B) d'un pixel, Stéganographie

## Première étape (TODO) <br />
Lire un fichier texte, supprimer tous les espaces et les sauts de ligne. <br />
Remplacer les majuscules par des minuscules. <br />
Remplacer tous les caractères accentuées par les caractères correspondant de l'alphabet.<br />
Par exemple les 'é', 'è' et 'ê' sont remplacés par un 'e'. Le 'ç' est remplacé par un 'c'.....

## Deuxième étape (TODO) <br />
Effectuer un chiffrement (par exemple le chiffre de César ou le chiffre de Vigenère) <br />
Cette étape est peut-être à échanger avec la deuxième. <br />
https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage <br />
https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re

## Troisième étape (TODO) <br />
Convertir chaque caractère en un nombre binaire.

## Quatrième étape (TODO) <br />
Stéganographie (1/2) <br />
Utilsation du module `pillow` <br />
Récupérer la composante de Rouge, Vert et Bleu de chaque pixel d'une image au format `.bmp`. <br />
Convertir ces composantes en binaire et supprimer des bits de poids faibles. <br />
Faire des essais pour déterminer le plus grand nombre de bits de poids faibles que l'on peut supprimer sans dénaturer la qualité de l'image. <br />
https://fr.wikipedia.org/wiki/Bit_de_poids_faible

## Cinquième étape (TODO) <br />
Stéganographie (2/2) <br />
Remplacer dans l'image les bits de poids faibles par le texte crypté converti en binaire.

## Sixième étape (TODO) <br />
Faire le procéder inverse pour récupếrer puis déchiffer le message.

## Remarque
Il peut être intéressant d'utiliser un masque et quelques opérateurs logiques lorsque l'on travaillera sur les bits de poids faibles.
