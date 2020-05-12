import random
import math

def Ouverture_Fichier(nom_fichier):
    #ouverture et lecture du fichier
    fichier=open(nom_fichier,"r")
    liste=[]
    temp=[]
    for ligne in fichier:
        if (ligne != '\n'):
            temp = ligne.rstrip("\n").split(";")
            for i in range(4):
                temp[i]=float(temp[i])
            liste.append(temp)
    fichier.close()
    return liste
 
def Normalisation (tab,axe):

    liste = []
    for element in tab:
        liste.append(element[axe])
    
    result = []
    for valeur in liste:
        valeur_a_ajouter = (valeur-min(liste))/(max(liste)-min(liste))
        result.append(valeur_a_ajouter)
    
    for i in range(len(tab)):
        tab[i][axe] = result[i]
    return

def Trouver_les_k_voisins (tab,k,element):
    result = []
    liste_des_distances = []
    for point in tab:
        d0 = ((point[0]-element[0])**2)
        d1 = ((point[1]-element[1])**2)
        d2 = ((point[2]-element[2])**2)
        d3 = ((point[3]-element[3])**2)
        p0 = 1
        p1 = 1
        p2 = 1
        p3 = 1
        distance = math.sqrt( p0*d0 + p1*d1 + p2*d2 + p3*d3 )
        liste_des_distances.append(distance)
    
    

    for i in range(k):
        value_min = min(liste_des_distances)
        liste_des_index_des_minimums = []
        for element in liste_des_distances:
            if (element == value_min):
                liste_des_index_des_minimums.append(liste_des_distances.index(element))
        index_conserve = random.choice(liste_des_index_des_minimums)
        result.append([tab[index_conserve],liste_des_distances[index_conserve]])
        del tab[index_conserve]
        del liste_des_distances[index_conserve]

    return result

def Determination_de_element(liste_voisin_distance):

    A = 0
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    G = 0
    H = 0
    I = 0
    J = 0
    maxi = liste_voisin_distance[len(liste_voisin_distance)-1][1]
    for element in liste_voisin_distance:
        #! On veut mettre en avant la proximité des k voisins par rapport à l'élément testé
        #! On peut imaginer que notre élément à tester est au centre d'un cercle de rayon égal à la distance du k voisin le plus éloigné du centre
        #! Nous utilisons cette distance comme maxi plutôt que la distance maximum parmi TOUS les points afin d'éviter que les différences entre les k
        #! voisins soient gommées
        #! La différence entre le maxi et la distance de chaque k voisin est ensuite ajoutée à la valeur générale de probabilité du groupe
        #! Ainsi plus un voisin est proche de l'élément à tester, plus il va ajouter à la valeur de probabilité d'appartenance de l'élément à tester au groupe
        #! Le groupe avec la plus grande probabilité est désigné comme étant celui auquel appartient l'élément à tester
        if(element[0][4]== 'A'):
            A +=  maxi- element[1] 
        if(element[0][4]== 'B'):
            B +=  maxi- element[1]
        if(element[0][4]== 'C'):
            C +=  maxi- element[1]
        if(element[0][4]== 'D'):
            D +=  maxi- element[1]
        if(element[0][4]== 'E'):
            E +=  maxi- element[1]
        if(element[0][4]== 'F'):
            F +=  maxi- element[1]
        if(element[0][4]== 'G'):
            G +=  maxi- element[1]
        if(element[0][4]== 'H'):
            H +=  maxi- element[1]
        if(element[0][4]== 'I'):
            I +=  maxi- element[1]
        if(element[0][4]== 'J'):
            J +=  maxi- element[1]
    dico_reponse = {
    'A':A,
    'B':B,
    'C':C,
    'D':D,
    'E':E,
    'F':F,
    'G':G,
    'H':H,
    'I':I,
    'J':J
    }
    reponse = max(zip(dico_reponse.values(),dico_reponse.keys()))
    return reponse[1]


def Algorithme_K_Voisin_matrice (k):
    liste_base = Ouverture_Fichier('Ensemble_base.csv')
    liste_valeur_test= Ouverture_Fichier('Ensemble_base.csv')
    
    index_element_a_tester = random.randrange(len(liste_valeur_test))
    element_a_tester = liste_valeur_test[index_element_a_tester]
    del liste_base[index_element_a_tester]

    liste_des_k_vsn = Trouver_les_k_voisins(liste_base,k,element_a_tester)

    reponse = Determination_de_element(liste_des_k_vsn)

    return (reponse,element_a_tester[4])


def Matrice():  
    nb_bon = 0
    matrice_resultat = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    nb_eval = 1000 #on teste 50 fois car la loi des grands nombres est stable vers n=30
    k = 8 #k=6 semble être la valeur à partir de laquelle la précision reste stable

    #Calcul des nb_eval tests et entrées dans la matrice de confusion
    for i in range(nb_eval):
        tupl = Algorithme_K_Voisin_matrice(k)
        notre_resultat,vrai_result = tupl
        if(notre_resultat == vrai_result): nb_bon+=1


        if(notre_resultat=='A'): x=0
        if(notre_resultat=='B'): x=1
        if(notre_resultat=='C'): x=2
        if(notre_resultat=='D'): x=3
        if(notre_resultat=='E'): x=4
        if(notre_resultat=='F'): x=5
        if(notre_resultat=='G'): x=6
        if(notre_resultat=='H'): x=7
        if(notre_resultat=='I'): x=8
        if(notre_resultat=='J'): x=9

        if(vrai_result=='A'): y=0
        if(vrai_result=='B'): y=1
        if(vrai_result=='C'): y=2
        if(vrai_result=='D'): y=3
        if(vrai_result=='E'): y=4
        if(vrai_result=='F'): y=5
        if(vrai_result=='G'): y=6
        if(vrai_result=='H'): y=7
        if(vrai_result=='I'): y=8
        if(vrai_result=='J'): y=9
        matrice_resultat[x][y]+= 1

        
    print()
    print("Le taux de réussite de l'algorithme est de " + str((nb_bon/nb_eval)*100) + "% sur " + str(nb_eval) + " tentatives")
    print()
    print('A gauche on lit ce que nous avons trouvé, en haut ce que la réponse était')
    print()
    print('       A   |   B   |   C   |   D   |   E   |   F   |   G   |   H   |   I   |   J   |')
    print('___________________________________________________________________________________')
    print('A  |   ' + str(matrice_resultat[0][0]) + '   |   ' + str(matrice_resultat[0][1]) + '   |   ' + str(matrice_resultat[0][2]) + '   |   ' + str(matrice_resultat[0][3])+ '   |   ' + str(matrice_resultat[0][4])+ '   |   ' + str(matrice_resultat[0][5])+ '   |   ' + str(matrice_resultat[0][6])+ '   |   ' + str(matrice_resultat[0][7])+ '   |   ' + str(matrice_resultat[0][8])+ '   |   ' + str(matrice_resultat[0][9]))
    print('B  |   ' + str(matrice_resultat[1][0]) + '   |   ' + str(matrice_resultat[1][1]) + '   |   ' + str(matrice_resultat[1][2]) + '   |   ' + str(matrice_resultat[1][3])+ '   |   ' + str(matrice_resultat[1][4])+ '   |   ' + str(matrice_resultat[1][5])+ '   |   ' + str(matrice_resultat[1][6])+ '   |   ' + str(matrice_resultat[1][7])+ '   |   ' + str(matrice_resultat[1][8])+ '   |   ' + str(matrice_resultat[1][9]))
    print('C  |   ' + str(matrice_resultat[2][0]) + '   |   ' + str(matrice_resultat[2][1]) + '   |   ' + str(matrice_resultat[2][2]) + '   |   ' + str(matrice_resultat[2][3])+ '   |   ' + str(matrice_resultat[2][4])+ '   |   ' + str(matrice_resultat[2][5])+ '   |   ' + str(matrice_resultat[2][6])+ '   |   ' + str(matrice_resultat[2][7])+ '   |   ' + str(matrice_resultat[2][8])+ '   |   ' + str(matrice_resultat[2][9]))
    print('D  |   ' + str(matrice_resultat[3][0]) + '   |   ' + str(matrice_resultat[3][1]) + '   |   ' + str(matrice_resultat[3][2]) + '   |   ' + str(matrice_resultat[3][3])+ '   |   ' + str(matrice_resultat[3][4])+ '   |   ' + str(matrice_resultat[3][5])+ '   |   ' + str(matrice_resultat[3][6])+ '   |   ' + str(matrice_resultat[3][7])+ '   |   ' + str(matrice_resultat[3][8])+ '   |   ' + str(matrice_resultat[3][9]))
    print('E  |   ' + str(matrice_resultat[4][0]) + '   |   ' + str(matrice_resultat[4][1]) + '   |   ' + str(matrice_resultat[4][2]) + '   |   ' + str(matrice_resultat[4][3])+ '   |   ' + str(matrice_resultat[4][4])+ '   |   ' + str(matrice_resultat[4][5])+ '   |   ' + str(matrice_resultat[4][6])+ '   |   ' + str(matrice_resultat[4][7])+ '   |   ' + str(matrice_resultat[4][8])+ '   |   ' + str(matrice_resultat[4][9]))
    print('F  |   ' + str(matrice_resultat[5][0]) + '   |   ' + str(matrice_resultat[5][1]) + '   |   ' + str(matrice_resultat[5][2]) + '   |   ' + str(matrice_resultat[5][3])+ '   |   ' + str(matrice_resultat[5][4])+ '   |   ' + str(matrice_resultat[5][5])+ '   |   ' + str(matrice_resultat[5][6])+ '   |   ' + str(matrice_resultat[5][7])+ '   |   ' + str(matrice_resultat[5][8])+ '   |   ' + str(matrice_resultat[5][9]))
    print('G  |   ' + str(matrice_resultat[6][0]) + '   |   ' + str(matrice_resultat[6][1]) + '   |   ' + str(matrice_resultat[6][2]) + '   |   ' + str(matrice_resultat[6][3])+ '   |   ' + str(matrice_resultat[6][4])+ '   |   ' + str(matrice_resultat[6][5])+ '   |   ' + str(matrice_resultat[6][6])+ '   |   ' + str(matrice_resultat[6][7])+ '   |   ' + str(matrice_resultat[6][8])+ '   |   ' + str(matrice_resultat[6][9]))
    print('H  |   ' + str(matrice_resultat[7][0]) + '   |   ' + str(matrice_resultat[7][1]) + '   |   ' + str(matrice_resultat[7][2]) + '   |   ' + str(matrice_resultat[7][3])+ '   |   ' + str(matrice_resultat[7][4])+ '   |   ' + str(matrice_resultat[7][5])+ '   |   ' + str(matrice_resultat[7][6])+ '   |   ' + str(matrice_resultat[7][7])+ '   |   ' + str(matrice_resultat[7][8])+ '   |   ' + str(matrice_resultat[7][9]))
    print('I  |   ' + str(matrice_resultat[8][0]) + '   |   ' + str(matrice_resultat[8][1]) + '   |   ' + str(matrice_resultat[8][2]) + '   |   ' + str(matrice_resultat[8][3])+ '   |   ' + str(matrice_resultat[8][4])+ '   |   ' + str(matrice_resultat[8][5])+ '   |   ' + str(matrice_resultat[8][6])+ '   |   ' + str(matrice_resultat[8][7])+ '   |   ' + str(matrice_resultat[8][8])+ '   |   ' + str(matrice_resultat[8][9]))
    print('J  |   ' + str(matrice_resultat[9][0]) + '   |   ' + str(matrice_resultat[9][1]) + '   |   ' + str(matrice_resultat[9][2]) + '   |   ' + str(matrice_resultat[9][3])+ '   |   ' + str(matrice_resultat[9][4])+ '   |   ' + str(matrice_resultat[9][5])+ '   |   ' + str(matrice_resultat[9][6])+ '   |   ' + str(matrice_resultat[9][7])+ '   |   ' + str(matrice_resultat[9][8])+ '   |   ' + str(matrice_resultat[9][9]))


def Algorithme_K_Voisin(k,fichier_base,element_a_tester):

    liste_base = Ouverture_Fichier(fichier_base)
    


    liste_des_k_vsn = Trouver_les_k_voisins(liste_base,k,element_a_tester)

    reponse = Determination_de_element(liste_des_k_vsn)

    return (reponse)

def Creation_Fichier_Reponse(fichier_base,fichier_test,k):

    liste_test = Ouverture_Fichier(fichier_test)
    contenu = ''
    for element in liste_test:
        prediction = Algorithme_K_Voisin(k,fichier_base,element)
        ligne =  str(prediction) + '\n'
        contenu+=ligne
    file = open('RemiGUILLON_VincentPOUPET.txt','w')
    file.write(contenu)
    file.close()

def Pourcentage_Justesse(fichier_reponse,fichier_prediction):
    liste_prediction = Ouverture_Fichier(fichier_prediction)
    liste_reponse = Ouverture_Fichier(fichier_reponse)
    total_bon = 0
    for i in range(len(liste_prediction)):
        if(liste_prediction[i][4]==liste_reponse[i][4]): total_bon+=1
    pourcentage = float((total_bon/len(liste_prediction))*100)
    print('Le pourcentage de valeurs correctement prédites est '+str(pourcentage) +' %')
    return

Creation_Fichier_Reponse('Ensemble_base.csv','finalTest.csv',8)


#Matrice()
