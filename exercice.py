#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    Dec_Lettre = ''
    for lettre in mot:
        Dec_Lettre=ord(lettre)
        if Dec_Lettre <=122 & Dec_Lettre>=97:
            Lettre-=32
        elif Dec_Lettre <=90 & Dec_Lettre>=65:
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
