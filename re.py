# -*- coding: utf-8 -*-

import re

def tel():
    #Fonction permettant de vérifier qu'un numéro correspond à un certain format
    chaine = ""
    expression = r"^0[0-9]([ .-]?[0-9]{2}){4}$"
    while re.search(expression, chaine) is None:
        chaine = input("Saisissez un numéro de téléphone (valide) :")
    return chaine

def mdp():
    #Fonction permettant de vérifier qu'un mot de passe correspond à un certain format
    #en utilisant une expression compilée
    chn_mdp = r"^[A-Za-z0-9]{6,}$"
    exp_mdp = re.compile(chn_mdp)
    mot_de_passe = ""
    while exp_mdp.search(mot_de_passe) is None:
        mot_de_passe = input("Tapez votre mot de passe : ")
    return mot_de_passe