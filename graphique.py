# importing the required module 
import matplotlib.pyplot as plt 
  


def affGraphique(stats):
    x = [] 
    y = [] 
    # plotting the points  
    for cle, val in stats.items():
        x.append(int(cle))
        y.append(int(val))


    plt.plot(x, y) 
    
    # naming the x axis 
    plt.xlabel('x - degret') 
    # naming the y axis 
    plt.ylabel('y - freq') 
    
    # giving a title to my graph 
    plt.title('Apparition des sommets!') 
    
    # function to show the plot 
    plt.show() 



donnee={}
donnee[1]=5
donnee[2]=8
donnee[3]=1
donnee[4]=2
donnee[5]=6
affGraphique(donnee)