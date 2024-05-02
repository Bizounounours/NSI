from timeit import*

def recherche_seq(tab,val):
    i=0
    n=len(tab)-1
    while i<=n and tab[i]!= val:
        i+=1
    if i<=n:
        '''
        print(tab[i])
    else:
        print(f"{val} n'est pas dans le tableau")
        '''
    return

def recherche_seq_for(tab,val):
    for i in range(len(tab)):
        if tab[i]==val:
            #print(val)
            return
    #print(f"{val} n'est pas dans le tableau")
    return

def recherche_seq_croissant(tab,val):
    for i in range(len(tab)):
        if tab[i]==val:
            #print(val)
            return
        elif tab[i]>val:
            #print(f"{val} n'est pas dans le tableau")
            return
    print(f"{val} n'est pas dans le tableau")
    return

def recherche_dichotomique(tab,val):
    gauche=0
    droite=len(tab)
    while gauche<=droite:
        milieu=(gauche+droite)/2
        milieu=round(number= milieu)
        if tab[milieu]==val:
            #print(val)
            return
        elif tab[milieu]>val:
            droite=milieu-1
        else:
            gauche=milieu+1
    #print(f"{val} n'est pas dans le tableau")
    return
'''
print(timeit(setup='from __main__ import recherche_dichotomique',
stmt=f"recherche_dichotomique([8,23,40,80],12)",
number=100))
'''
def calculer_temps(algo,tab,val,repet):
    print(timeit(setup=f'from __main__ import {algo}',
stmt=f"{algo}({tab},{val})",
number=repet))

liste=list(range(1000000))
val=960000.9
calculer_temps("recherche_dichotomique",liste,val,100)