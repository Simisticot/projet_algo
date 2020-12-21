"""
    Etude de graphs du Web
    Julie GASPAR
    Max HOFFER
    Laureline PARTONNAUD
    Simon PEREIRA
"""
import random
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
        return self.degreTotal()/self.nbSommets()

    def distribDegre(self):
        x = [] 
          
        for lessommets in self.sommets:
            x.append(self.sommets[lessommets].getDegre())

        plt.hist(x, range = (0, self.degreMax() + 1), density = True, edgecolor = 'black')

        plt.xlabel('x - Degre') 
        plt.ylabel('y - Frequence d\'apparition') 
        plt.title('Distribution des degrés') 
        plt.show() 

    def listeAdj(self):                 #affiche uns à uns les voisins des sommets du graphe
        lesvoisins = []
        for i in self.sommets:
            for j in self.sommets[i].adjacent():
                if j not in '[ ,]' :
                    lesvoisins.append([i, j])
        for i in lesvoisins:
            print (i)

    def stockGraphe(self, nomfichier):  #stocke le graphe dans un fichier texte sous forme de liste l'adjacence
        with open("./"+nomfichier+".txt", "w") as monfichier:
            for i in self.sommets:
                monfichier.write(str(i) + ''.join(self.sommets[i].adjacent()) + "\n")
            
    def stockGraphe2(self, nomfichier): #stocke le graphe dans un fichier texte (format différent)
        with open("./"+nomfichier+".txt", "w") as monfichier:
            for i in self.sommets:
                for j in self.sommets[i].adjacent():
                    if j not in '[ ,]' :
                        monfichier.write(str(i) + "," + str(j) + "\n")
   
    def afficheGraphe(self):            #affiche le graphe avec sa liste d'adjacence
        for x in self.sommets:
            print(self.getSommet(x))
    
    def analyseGraphe(self):            #lance l'analyse d'un graphe
        print ("nombre de sommets : " + str(self.nbSommets()))
        print ("nombre d\'aretes : " + str(self.nbAretes()))
        print ("degre maximal : " + str(self.degreMax()))
        print ("degre moyen : " + str(self.degreMoyen()))
        self.distribDegre()


def filetoGraph(path):            #transforme un fichier de listes des arêtes en graphe
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


# albert = genereBarabasiAlbert(2, 10)
# albert.analyseGraphe()
# albert.stockGraphe("fichieralbert")
# albert.stockGraphe2("fichieralbert2")

leGraphe = filetoGraph("./Wikipedia1.csv")
leGraphe.analyseGraphe()    