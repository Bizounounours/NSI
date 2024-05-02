def int_to_bin(n,nb):
    ch=""
    while n>0:
        r=n%2
        n=n//2
        ch=str(r)+ch
    ch=(nb-len(ch))*'0'+ch
    return ch

videos=[('Vidéo 1',114,4570),('Vidéo 2',32,630),('Vidéo 3',20,1650),('Vidéo 4',4,85),('Vidéo 4',18,2150),('Vidéo 6',80,2710),('Vidéo 7',5,320)]

def ens_des_parties(ensemble):
    nb=len(ensemble)
    n=2**nb
    parties=[]
    for i in range(1,n):
        ch=int_to_bin(i,nb)
        partie=[]
        for j in range(len(ch)):
            if ch[j]=='1':
                partie.append(ensemble[j])
        parties.append(partie)
    return parties
#print(ens_des_parties(videos))

def duree_totale(liste):
    d=0
    for i in liste:
        d=d+i[1]
    return d

def taille_totale(liste):
    t=0
    for i in liste:
        t=t+i[2]
    return t

def recherche(ens_parties,contrainte):
    duree_max=0
    solution=[]
    for partie in ens_parties:
        duree=duree_totale(partie)
        taille=taille_totale(partie)
        if taille<=contrainte and duree>duree_max:
            duree_max=duree
            solution=partie
    return solution,duree_max,min

#print(recherche(ens_des_parties(videos),5000))

def force_brute(fichiers,taille_max):
    parties = ens_des_parties(fichiers)
    return recherche(parties,taille_max)

#print(force_brute(videos,5000))

