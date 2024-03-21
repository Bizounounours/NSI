from listes import*
from tris import*
from timeit import*
import pylab

def temps_de_tri(n):
    print(timeit(setup='from tris import tri_selection; from listes import cree_liste_melangee',
    stmt=f'tri_selection(cree_liste_melangee({n}))',
    number=100))
    return

def temps_de_tri_interm(n):
    L=[]
    for i in range (1,n+1):
        L.append(timeit(setup='from tris import tri_selection; from listes import cree_liste_melangee',
        stmt=f'tri_selection(cree_liste_melangee({i}))',
        number=100))
    print(L)
    return

def courbe_tri(n):
    x=[i for i in range(1,n+1)]
    y=[timeit(setup='from tris import tri_selection; from listes import cree_liste_melangee',
        stmt=f'tri_selection(cree_liste_melangee({j}))',
        number=100) for j in range(1,n+1)]
    pylab.plot(x,y)
    pylab.title('Temps du tri par sélection (pour {:d} essais)'.format(n))
    pylab.xlabel('taille des listes')
    pylab.ylabel('temps en secondes')
    pylab.grid()
    pylab.show()
courbe_tri(10)