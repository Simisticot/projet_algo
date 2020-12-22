"""
    Etude de graphs du Web
    Julie GASPAR
    Max HOFFER
    Laureline PARTONNAUD
    Simon PEREIRA
"""
import random
import math
import matplotlib.pyplot as plt 

random.seed()

class Sommet(object):
    """docstring for Sommet"""

    def __init__(self, id):             #initialisation du sommet avec son nom (id) et la liste de ses voisins
        super(Sommet, self).__init__()
        self.id = id
        self.voisins = []

    def ajouterVoisin(self, voisin):    #ajoute un voisin à la liste des voisins du sommet
        self.voisins.append(voisin)
        voisin.voisins.append(self)

    def __str__(self):                  #toString qui affiche le sommet et la liste de ses voisins
        return str(self.id) + " est voisin de " + str([x.id for x in self.voisins])

    def adjacent(self):                 #retourne les sommets adjactents
        return str([x.id for x in self.voisins])

    def getVoisins(self):               #recupere la liste des voisins d'un sommet
        return self.voisins

    def getId(self):                    #recupere l'id d'un sommet
        return self.id

    def getDegre(self):                 #recupere le degre d'un sommet
        return len(self.voisins)


class Graphe(object):
    """docstring for Graphe"""

    def __init__(self):                 #initialisation du graphe avec l'ensemble de ses sommets
        super(Graphe, self).__init__()
        self.sommets = {}

    def ajouterSommet(self, id):        #ajoute un sommet au graphe
        sommet = Sommet(id)
        self.sommets[id] = sommet

    def getSommet(self, id):            #recupere un sommet a l'id recherche s'il existe
        if id in self.sommets:
            return self.sommets[id]
        else:
            return None

    def __contains__(self, id):         #retourne vrai si un sommet appartient au graphe
        return id in self.sommets

    def ajouterArete(self, idDepart, idArrivee):    #ajoute une arete entre deux sommets
        if idDepart not in self.sommets:
            self.ajouterSommet(idDepart)
        if idArrivee not in self.sommets:
            self.ajouterSommet(idArrivee)
        self.sommets[idDepart].ajouterVoisin(self.sommets[idArrivee])

    def nbSommets(self):                #calcule le nombre de sommet du graphe
        return len(self.sommets)
    
    def nbAretes(self):                 #calcul le nombre d'aretes presentes dans le graphe
        L=[]
        k=0
        for s in self.sommets:
            L.append(s)
            for v in self.getSommet(s).voisins:
                if v.id not in L:
                    k=k+1
        return(k)

    def degreMax(self):                 #recupere le degre maximal du graphe
        lesdegres = []        
        for x in self.sommets:
            lesdegres.append(self.sommets[x].getDegre())
        return max(lesdegres)

    def degreTotal(self):               #calcule la somme des degres des sommets du graphe
        total = 0
        for x in self.sommets:
            total += self.sommets[x].getDegre()
        return total

    def degreMoyen(self):               #calcul le degré moyen du graphe
        return round(self.degreTotal()/self.nbSommets(), 3)

    def distribDegre(self):             #affiche la distribution des degres sous forme graphique
        x = [] 
        for lessommets in self.sommets:
            x.append(self.sommets[lessommets].getDegre())

        plt.hist(x, range = (0, self.degreMax() + 1), density = True, edgecolor = 'black')

        plt.xlabel('x - Degre') 
        plt.ylabel('y - Frequence d\'apparition') 
        plt.title('Distribution des degrés') 
        plt.show() 

    def stockGraphe(self, path):        #stocke le graphe dans un fichier texte depuis la liste d'adjacence
        with open(path+".txt", "w") as monfichier:
            for i in self.sommets:
                if (self.sommets[i].voisins == []):
                    monfichier.write(str(i) + "," + "\n")
                else:
                    for j in self.sommets[i].voisins:
                        monfichier.write(str(i) + "," + str(j.id) + "\n")
   
    def afficheGraphe(self):            #affiche le graphe avec sa liste d'adjacence
        for x in self.sommets:
            print(self.getSommet(x))
    
    def analyseGraphe(self):            #lance l'analyse d'un graphe
        print ("nombre de sommets : " + str(self.nbSommets()))
        print ("nombre d\'aretes : " + str(self.nbAretes()))
        print ("degre maximal : " + str(self.degreMax()))
        print ("degre moyen : " + str(self.degreMoyen()))
        self.distribDegre()


def filetoGraph(path):                  #transforme un fichier de listes des arêtes en graphe
    file = open(path,"r")
    lines = file.readlines()
    file.close()
    
    graphe = Graphe()
    
    for l in lines:
        i=0
        id=""
        c= l.strip()[i]
        while c!="[" and c!= "]" and c!="," and c!=" " and c!="\t" :
            id=id +c
            i=i+1
            c= l.strip()[i]
        
        id=int(id)
        
        if not(graphe.__contains__(id)):
            graphe.ajouterSommet(id)
        
        v =""
        for c in l.strip()[i:]:
            if c!="[" and c!= "]" and c!="," and c!=" " and c!="\t" :
                v=v+c
        
        if v!="" :
            v=int(v)
            if not(graphe.__contains__(v)):
                graphe.ajouterSommet(v)
            
            if v not in [x.id for x in graphe.sommets[id].voisins]:
                graphe.sommets[id].ajouterVoisin(graphe.sommets[v])

    return graphe

def genereRado(taille):                 #genene un graphe de Edgar Gilbert
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

def genereBarabasiAlbert(m, taille):    #genere un graph de Barabasi-Albert
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

def diametreGraphe(graphe):             #calcule le diametre du graphe
    D=floyd_warshall(graphetoMat(graphe))
    
    max=0
    for i in D:
        for j in i:
            if j != math.inf and j>max :
                max=j
    return(max)

def floyd_warshall(mat):                #renvoie la matrice de la plus petite distance pour chaque couple de sommets
    n = len(mat[0])
    distance = list(map(lambda i: list(map(lambda j: j, i)), mat))
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return(distance)

def graphetoMat(graphe):                #convertit le graphe en matrice
    M = [[math.inf for i in range(graphe.nbSommets())]for j in range(graphe.nbSommets())]
   
    for s in graphe.sommets:
        for v in graphe.getSommet(s).voisins:
            M[s-1][v.id-1]=1
    return(M)

# edgar1 = genereRado(10)
# edgar1.analyseGraphe()
# print("diamètre : " + str(diametreGraphe(edgar1)))
# edgar1.stockGraphe("./edgar1")

# edgar2 = genereRado(100)
# edgar2.analyseGraphe()
# edgar2.stockGraphe("./edgar2")

# edgar3 = genereRado(1000)
# edgar3.analyseGraphe()
# edgar3.stockGraphe("./edgar3")

# edgar4 = genereRado(2000)
# edgar4.analyseGraphe()
# edgar4.stockGraphe("./edgar4")

# edgar5 = genereRado(5000)
# edgar5.analyseGraphe()
# edgar5.stockGraphe("./edgar5")


albert1 = genereBarabasiAlbert(2, 10)
albert1.analyseGraphe()
albert1.stockGraphe("./albert1")

# albert2 = genereBarabasiAlbert(2, 100)
# albert2.analyseGraphe()
# albert2.stockGraphe("./albert2")

# albert3 = genereBarabasiAlbert(2, 1000)
# albert3.analyseGraphe()
# albert3.stockGraphe("./albert3")

# albert4 = genereBarabasiAlbert(2, 10000)
# albert4.analyseGraphe()
# albert4.stockGraphe("./albert4")

# albert5 = genereBarabasiAlbert(2, 15000)
# albert5.analyseGraphe()
# albert5.stockGraphe("./albert5")

leGraphe = filetoGraph("./albert1.txt")
leGraphe.analyseGraphe()