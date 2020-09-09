#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    Lettre = ''
    DecLettre = ''
    for lettre in mot:
        DecLettre=ord(lettre)
        if DecLettre <=122 & DecLettre>=97:
            Lettre-=32
        elif DecLettre <=90 & Dec_Lettre>=65:
            Lettre+= 32
        else:
            print("Not a letter")
        resultat += lettre
        
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
