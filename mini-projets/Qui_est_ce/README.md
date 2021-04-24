# Mini-projjet - Qui est-ce ?

En s'inspirant du célbère jeu *Qui est-ce ?* on peut construire le tableau de dictionnaires suivant :

```
kiestce = [
    {'nom':'Julie', 'genre':'fille', 'yeux':'bleus', 'cheveux':'longs',
     'col_cheveux':'brun', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Nicolas', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'chauve',
     'col_cheveux':'blanc', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'oui', 'chapeau':'non'},

    {'nom':'Michel', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'roux', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Daniel', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'chatain', 'nez':'gros', 'barbe':'moustache',
     'lunettes':'non', 'chapeau':'oui'},

    {'nom':'Jacques', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'blanc', 'nez':'petit', 'barbe':'moustache',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Nathalie', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'blanc', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Emilie', 'genre':'fille', 'yeux':'bleus', 'cheveux':'longs',
     'col_cheveux':'blanc', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'oui', 'chapeau':'non'},

    {'nom':'David', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'chauve',
     'col_cheveux':'roux', 'nez':'petit', 'barbe':'barbe',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Claude', 'genre':'garçon', 'yeux':'bleus', 'cheveux':'courts',
     'col_cheveux':'roux', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'oui', 'chapeau':'non'},

    {'nom':'Alex', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'brun', 'nez':'gros', 'barbe':'aucune',
     'lunettes':'oui', 'chapeau':'oui'},

    {'nom':'Marie', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'blond', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Corinne', 'genre':'fille', 'yeux':'bleus', 'cheveux':'longs',
     'col_cheveux':'chatain', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Sylvain', 'genre':'garçon', 'yeux':'bleus', 'cheveux':'courts',
     'col_cheveux':'blond', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Cécile', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'blond', 'nez':'gros', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Anne', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'roux', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'oui'},

    {'nom':'Valérie', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'brun', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'oui', 'chapeau':'non'},

    {'nom':'Léa', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'chatain', 'nez':'gros', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Elodie', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'roux', 'nez':'gros', 'barbe':'aucune',
     'lunettes':'oui', 'chapeau':'non'},

    {'nom':'Thomas', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'brun', 'nez':'petit', 'barbe':'barbe',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Marc', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'blond', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'oui'},

    {'nom':'Martin', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'chauve',
     'col_cheveux':'brun', 'nez':'petit', 'barbe':'barbe',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Caroline', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'blond', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'non'},

    {'nom':'Mathilde', 'genre':'fille', 'yeux':'marrons', 'cheveux':'longs',
     'col_cheveux':'chatain', 'nez':'petit', 'barbe':'aucune',
     'lunettes':'non', 'chapeau':'oui'},

    {'nom':'Philippe', 'genre':'garçon', 'yeux':'marrons', 'cheveux':'courts',
     'col_cheveux':'blanc', 'nez':'petit', 'barbe':'barbe',
     'lunettes':'non', 'chapeau':'non'}
]
```

Sachant que pour chaque clef suivante, on a l'une de ces valeurs :
* 'genre' :  'garçon', 'fille'
* 'yeux' : 'marrons', 'bleus'
* 'cheveux' : 'courts', 'longs',  'chauve'
* 'couleurs de cheveux' : 'blanc','brun','roux','blond','chatain'
* 'nez' : 'petit','gros'
* 'barbe' : 'aucune', 'moustache', 'barbe'
* 'lunettes' : 'non', 'oui'
* 'chapeau' : 'non', 'oui'
