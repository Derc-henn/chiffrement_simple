#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sun Aug 11 08:43:51 2024

@author: Derc'henn
"""

# On peut complexifier encore plus :
#     mélanger les lettres dans alphanums, 
#     changer l'ordre des rajouts dans resultat (avant ou après), etc etc 

alphanums = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

symbols = "@!#$%?"

# -----------------------------------------------------------------------------
def fonction_de_chiffrement(x):    
    return 3*x + 2*x**2 + x**3              

# -----------------------------------------------------------------------------
def chiffrement(ma_pass_phrase):    
    
    global alphanums    
    global symbols    
    
    erreur = False    
    
    n = len(ma_pass_phrase)    
    
    len_alphanums = len(alphanums)    
    
    resultat = ""    
    
    for i in range(n):        
        
        recherche = True        
        rang = 0;        
        
        if(ma_pass_phrase[i] == "'") or (ma_pass_phrase[i] == " "):
            pass
        else:        
            
            # recherche du rang de la lettre dans alphanums
            while((recherche == True) and (rang != len_alphanums)) :       #while(recherche)                
                if(ma_pass_phrase[i] == alphanums[rang]):
                    recherche = False
                else:
                    rang = rang + 1;          
                    
            # encodage dans une autre lettre dans alphanums            
            if(recherche == True) : 
                print(f" ! {ma_pass_phrase[i]} : Lettre de la pass_phrase non reconnue dans alphanums")
                erreur = True
                break
            else :             
                nouveau_rang = (fonction_de_chiffrement(rang))%len_alphanums            
                resultat = alphanums[nouveau_rang] + resultat 
                if(i%3 == 0) : print(resultat)  #pour voir l'evolution, mais inutile
                
    if(erreur == False) :    
        # on rajoute un symbol 
        resultat = symbols[n%len(symbols)] + resultat    
        
        print(f"\n\n pass_phrase d'origine : \n  {ma_pass_phrase} \n mot de passe en sortie  : \n\n           {resultat} \n")        
        
# -----------------------------------------------------------------------------

ma_pass_phrase = "Le carre de l'hypotenuse est egal a la somme des carres des 2 autres cotes"

chiffrement(ma_pass_phrase)





