def rendu_monnaie(somme_a_rendre,systeme_monnaie):
    liste_piece=[]
    i=len(systeme_monnaie)-1
    while somme_a_rendre>0:
        valeur=systeme_monnaie[i]
        if somme_a_rendre<valeur:
            i-=1
        else:
            liste_piece.append(valeur)
            somme_a_rendre=somme_a_rendre-valeur
    print(liste_piece)
    return
#rendu_monnaie(133,[1,2,5,10,20,50,100,500])

def int_to_bin(n,nb):
    ch=""
    while n>0:
        r=n%2
        n=n//2
        ch=str(r)+ch
    ch=(nb-len(ch))*'0'+ch
    print(ch)
    return 
int_to_bin(7,8)