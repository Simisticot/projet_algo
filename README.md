# Projet - Outils pour la conception d'algorithmes
## Etudes de graphes du web


Tous les fichiers générés, lus et analysés, utilisés pour le rapport se situent dans le même dossier que notre code source. 

Notre projet a été réalisé en Python. Lors de son exécution, il génère automatiquement 5 graphes de type Edgar Gilbert, 5 graphes de type Edgar Gilbert et 5 autres de type Barabasi-Albert. Ces 10 graphes sont de tailles différentes. Après cette génération, notre programme les analyse (calcule des nombre de sommets et d'arêtes, des degré maximal et moyen et affiche la distribution des degrés).

De plus, il lit et analyse de la même manière les grands graphes de Stanford. 

Pour créer un nouveau graphe, il suffit de lui attribuer une taille (nombre de sommets).
Pour l'enregistrer, il faut appeler la fonction de stockage en précisant le chemin et le nom du fichier dans lequel le graphe sera enregistré (il n'est pas nécessaire de préciser l'extension). Le graphe est directement stocké en ```.txt```.

Pour lire un nouveau graphe depuis un fichier (```.txt```ou```.csv```), il faut appeler la fonction ```filetoGraph()```en précisant le chemin où se situe ce fichier.

Pour la lecture des grands graphes de Stanford, nous avons modifié les fichiers en retirant les lignes comprenant du texte pour ne garder que les voisins des différents sommets.

Nous avons remarqué qu'au-delà de 5000 sommets pour les graphes Edgar Gilbert et de 15000 sommets pour les graphes Barabasi-Albert, les temps de calcul (notamment le nombre d’arêtes) sont trop long (plus de 10 min). 
En se basant sur cette limite, nous avons trouvé que la taille maximum des graphes de Edgar Gilbert est de 10000 sommets et de 20000 sommets pour les graphes de Barabasi-Albert. Avec ces tailles, il est impossible de calculer les paramètres.

#### Réalisé par : 
Julie GASPAR
Max HOFFER
Laureline PARTONNAUD
Simon PEREIRA