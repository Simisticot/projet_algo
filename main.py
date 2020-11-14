import random

random.seed()

class Sommet(object):
    """docstring for Sommet"""

    def __init__(self, id):
        super(Sommet, self).__init__()
        self.id = id
        self.voisins = []

    def ajouterVoisin(self, voisin):
        self.voisins.append(voisin)
        voisin.voisins.append(self)

    def __str__(self):
        return str(self.id) + " est voisin de " + str([x.id for x in self.voisins])

    def getVoisins(self):
        return self.voisins

    def getId(self):
        return self.id

    def getDegre(self):
        return len(self.voisins)


class Graphe(object):
    """docstring for Graphe"""

    def __init__(self):
        super(Graphe, self).__init__()
        self.sommets = {}

    def ajouterSommet(self, id):
        sommet = Sommet(id)
        self.sommets[id] = sommet

    def getSommet(self, id):
        if id in self.sommets:
            return self.sommets[id]
        else:
            return None
    def __contains__(self, id):
        return id in self.sommets
    def ajouterArete(self, idDepart, idArrivee):
        if idDepart not in self.sommets:
            self.ajouterSommet(idDepart)
        if idArrivee not in self.sommets:
            self.ajouterSommet(idArrivee)
        self.sommets[idDepart].ajouterVoisin(self.sommets[idArrivee])

    def degreTotal(self):
        total = 0
        for x in self.sommets:
            total += self.sommets[x].getDegre()
        return total


def genereRado(taille):
    graphe = Graphe()
    for x in range(1, taille+1, 1):
        graphe.ajouterSommet(x)

    for x in graphe.sommets:
        for y in graphe.sommets:
            if x < y:
                rand = random.randrange(0,2,1)
                if rand == 1:
                    graphe.ajouterArete(x,y)
    return graphe

def genereBarabasiAlbert(m, taille):
    graphe = Graphe()
    for x in range(1, 4, 1):
        graphe.ajouterSommet(x)
    graphe.sommets[1].ajouterVoisin(graphe.sommets[2])
    graphe.sommets[1].ajouterVoisin(graphe.sommets[3])
    graphe.sommets[3].ajouterVoisin(graphe.sommets[2])
    for x in range(4, taille+1, 1):
        graphe.ajouterSommet(x)
        deg = graphe.degreTotal()
        for y in graphe.sommets:
            i = 0
            if x != y and i < m:
                rand = random.randrange(0, deg, 1)
                if rand <= graphe.getSommet(y).getDegre():
                    graphe.getSommet(y).ajouterVoisin(graphe.getSommet(x))
                    i += 1
    return graphe


albert = genereBarabasiAlbert(2, 100)

for x in albert.sommets:
    print(albert.getSommet(x))