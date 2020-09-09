#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    resultat = ''
    for lettre in mot:
        lettre=ord(lettre)
        lettre-=32
        resultat += chr(lettre)
        
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
