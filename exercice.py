#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''

    for lettre in mot:
        Dec_Lettre=ord(lettre)
        if Dec_Lettre <=122 & Dec_Lettre>=97:
            New_Lettre=Dec_Lettre-32
        elif Dec_Lettre <=90 & Dec_Lettre>=65:
            New_Lettre=Dec_Lettre+32

        
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
