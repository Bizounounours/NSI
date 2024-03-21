def tri_selection(tab):
    for i in range((len(tab)-1)):
        min=i
        for j in range(i+1,len(tab)):
            if tab[j]<tab[min]:
                min=j
        tab[i],tab[min]=tab[min],tab[i]
    return tab

def tri_insertion(tab):
    n=len(tab)
    
    for j in range(1,n):
        cle=tab[j]
        k=j-1
        while k>=0 and tab[k]>cle:
            tab[k+1]=tab[k]
            k=k-1
        tab[k+1]=cle
    return tab

def tri_a_bulles(tab):
    i=len(tab)-1  #indice du dernier Ã©lÃ©ment du tableau

    while i>=0:
        for j in range(i):
            if tab[j]>tab[j+1]:
                tab[j],tab[j+1]=tab[j+1],tab[j]
        i=i-1
    return tab