#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        lettre=ord(lettre)
        if lettre <=122 & lettre>=97:
            lettre-=32
        elif lettre <=90 & lettre>=65:
            lettre+= 32
        else:
            print("Pas une lettre")
        resultat += chr(lettre)
        mot 
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
