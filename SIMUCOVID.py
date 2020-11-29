#Programme crée par Thibault LOTH, L2 GROUPE F, pour le TAI de probabilité de L2 à EFREI Paris
#Groupe : Thibault LOTH, Vincent EUNG, Alexandre DELFOSSE, Maladèle WATT

#Importation tkinter & matplotlib + création fenêtre principale logiciel
from tkinter import*
import matplotlib.pyplot as plt

fenetre = Tk() 
fenetre.title("SimuCovid")
fenetre.geometry("500x500")

#Définition des fonctions

def fenetreaide2():
    #création de la fenêtre qui affiche les explications
    explication2 = Tk()
    explication2.title("SimuCovid : Explications")
    explication2.geometry("520x300")

    #affichage des explications
    labelexplication = Label(explication2, text = "VP signifie Vrai Positif, c'est à dire qu'un patient est malade, \n et que le test PCR l'indique postif au COVID-19\n")
    labelexplication.pack()
    labelexplication2 = Label(explication2, text = "VN signifie Vrai Négatif, c'est à dire qu'un patient est sain, \n et que le test PCR l'indique négatif au COVID-19\n")
    labelexplication2.pack()
    labelexplication3 = Label(explication2, text = "FP signifie Faux Positif, c'est à dire qu'un patient est sain, \n et que le test PCR l'indique postif au COVID-19 \n")
    labelexplication3.pack()
    labelexplication4 = Label(explication2, text = "FN signifie Faux Négatif, c'est à dire qu'un patient est malade, \n et que le test PCR l'indique négatif au COVID-19 \n")
    labelexplication4.pack()

    bouton_quitter = Button(explication2, text = "Fermer la fenêtre", command=explication2.destroy)
    bouton_quitter.pack()


def fenetreaide():
    #création de la fenêtre qui affiche les explications
    explication = Tk()
    explication.title("SimuCovid : Explications")
    explication.geometry("520x300")

    #affichage des explications
    labelexplication = Label(explication, text = "Ce petit programme a pour but de simuler les résultats de test PCR sur une population donnée\n")
    labelexplication.pack()
    labelexplication2 = Label(explication, text = "La prévalence est le rapport entre le nombre de cas totaux sur une population\n Il correspond à un pourcentage de la population infectée\n")
    labelexplication2.pack()
    labelexplication3 = Label(explication, text = "La sensibilité d'un test est le taux de personnes dites vrais positifs, \nc'est à dire qu'elles sont malades et que le test est positif \n On la traduit par P(positif|infecté) en probabilités conditionelles\n")
    labelexplication3.pack()
    labelexplication4 = Label(explication, text = "La spécificité d'un test est le taux de personnes dites vrais négatifs, \nc'est à dire qu'elles ne sont pas malades et que le test est négatif \n On la traduit par P(négatif|sain) en probabilités conditionelles\n")
    labelexplication4.pack()

    bouton_suivant = Button(explication, text = "Page suivante", command=fenetreaide2)
    bouton_suivant.pack()

    bouton_quitter = Button(explication, text = "Fermer la fenêtre", command=explication.destroy)
    bouton_quitter.pack()


def graph(w,x,y,z):
    name = ['TESTS VRAIS POSITIFS', 'TESTS VRAIS NEGATIFS', 'TESTS FAUX POSITIFS', 'TESTS FAUX NEGATIFS']
    data = [w,x,y,z]

    plt.title('Résultats des tests en fonction de leur véracité')
    plt.pie(data, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.axis('equal')
    plt.show()

def appelgraph():
    graph(var_vrai_positif,var_vrai_negatif,var_faux_positif,var_faux_negatif)


def simulation():
    #Définition des variables

    global var_pop 
    global var_prevalence
    global var_sensibilite
    global var_specificite

    global var_vrai_positif
    global var_vrai_negatif
    global var_faux_positif
    global var_faux_negatif

    
    #Création de la fenêtre qui reçoit les résultats de la simulation

    simulation = Tk()
    simulation.title("SimuCovid : Simulation")
    simulation.geometry("500x500")

    #Récupérations des différentes valeurs choisies par l'utilisateur

    var_pop=int(population.get())
    var_prevalence=int(prevalence.get())
    var_sensibilite=int(sensibilite.get())
    var_specificite=int(specificite.get())
    
    var_pop_infectee = int(var_pop* (0.01*var_prevalence)) #On détermine la partie de la population qui est infectée
    var_pop_saine = int(var_pop-var_pop_infectee) #On détermine la partie de la population qui est saine
    var_vrai_positif = int(var_pop_infectee * (0.01*(var_sensibilite))) #On détermine la partie des tests définis comme vrais positifs (malade et test positif)
    var_vrai_negatif = int(var_pop_saine * (0.01*(var_specificite))) #On détermine la partie des tests définis comme vrais négatifs (sains et test négatif)
    var_faux_positif = int(var_pop_saine * (1-(var_specificite/100)))#On détermine la parties des tests définis comme faux positifs (sain et tests positifs)
    var_faux_negatif = int(var_pop_infectee * (1-(var_sensibilite/100))) #On détermine la parties des tests définis comme faux négatifs (malade et tests négatifs)


    
    #Zone d'entrée pour le nombre de sujets pour la simulation
    #Population
    var_pop_text = str(var_pop)
    var_pop_text = var_pop_text + " individus\n"

    champ_pop1 = Label(simulation,text ="Population étudiée : ")
    champ_pop2 = Label(simulation,text =var_pop_text)
    champ_pop1.pack()
    champ_pop2.pack()

    #Population saine et infectée (formules à changer si on trouve mieux)

    pourcentage_infectee = str(100*(var_pop_infectee/var_pop))
    var_pop_inf_text = str(var_pop_infectee)
    var_pop_inf_text = var_pop_inf_text +" individus, soit "+pourcentage_infectee+" % de la population totale\n"

    champ_inf1 = Label(simulation,text ="Population infectée : ")
    champ_inf2 = Label(simulation,text =var_pop_inf_text)
    champ_inf1.pack()
    champ_inf2.pack()

    pourcentage_sain = str(100*(var_pop_saine/var_pop))
    var_pop_sain_text = str(var_pop_saine)
    var_pop_sain_text = var_pop_sain_text +" individus, soit "+pourcentage_sain+" % de la population totale\n"

    champ_sain1 = Label(simulation,text ="Population saine : ")
    champ_sain2 = Label(simulation,text =var_pop_sain_text)
    champ_sain1.pack()
    champ_sain2.pack()

    #Tests vrai postifs
    
    pourcentage_vp = str(100*(var_vrai_positif/var_pop))
    var_vp_text = str(var_vrai_positif)
    var_vp_text = var_vp_text+ " tests sont de vrais positifs, soit "+pourcentage_vp+" % des tests effectués\n"

    champ_vp1 = Label(simulation,text="Tests 'vrais positifs'")
    champ_vp2 = Label(simulation,text=var_vp_text)
    champ_vp1.pack()
    champ_vp2.pack()

    #Tests vrai négatifs
    
    pourcentage_vn = str(100*(var_vrai_negatif/var_pop))
    var_vn_text = str(var_vrai_negatif)
    var_vn_text = var_vn_text+ " tests sont de vrais négatifs, soit "+pourcentage_vn+" % des tests effectués\n"

    champ_vn1 = Label(simulation,text="Tests 'vrais négatifs'")
    champ_vn2 = Label(simulation,text=var_vn_text)
    champ_vn1.pack()
    champ_vn2.pack()

    #Tests faux positifs
    
    pourcentage_fp = str(100*(var_faux_positif/var_pop))
    var_fp_text = str(var_faux_positif)
    var_fp_text = var_fp_text+ " tests sont de faux positifs, soit "+pourcentage_fp+" % des tests effectués\n"

    champ_fp1 = Label(simulation,text="Tests 'faux positifs'")
    champ_fp2 = Label(simulation,text=var_fp_text)
    champ_fp1.pack()
    champ_fp2.pack()

    #Tests faux négatifs
    
    pourcentage_fn = str(100*(var_faux_negatif/var_pop))
    var_fn_text = str(var_faux_negatif)
    var_fn_text = var_fn_text+ " tests sont de faux négatifs, soit "+pourcentage_fn+" % des tests effectués\n"
    
    champ_fn1 = Label(simulation,text="Tests 'faux négatifs'")
    champ_fn2 = Label(simulation,text=var_fn_text)
    champ_fn1.pack()
    champ_fn2.pack() 
    #Bouton pour afficher des graphs

    bouton_graph = Button(simulation, text="Afficher les graphs", command = appelgraph)
    bouton_graph.pack()

    #Bouton pour fermer la fenêtre de simulation

    bouton_quitter = Button(simulation, text = "Fermer la fenêtre", command=simulation.destroy)
    bouton_quitter.pack()
    

 
#Zone d'entrée pour le nombre de sujets pour la simulation
champ_label1 = Label(fenetre,text ="Renseignez le nombre de personnes dans la population")
champ_label1.pack()

population = Entry(fenetre,width=40)
population.pack()

#Zone d'entrée pour la prévalence (% de la pop qui est infectée)
champ_label2 = Label(fenetre,text ="\nRenseignez la prévalence (en %)")
champ_label2.pack()

prevalence = Scale(fenetre, from_=0, to=100, orient=HORIZONTAL, length=350)
prevalence.pack()

#Zone d'entrée pour la sensibilité (taux de vrais positifs)
champ_label3 = Label(fenetre,text ="\nRenseignez la sensibilité (en %)")
champ_label3.pack()

sensibilite = Scale(fenetre, from_=0, to=100, orient=HORIZONTAL, length=350)
sensibilite.pack()

#Zone d'entrée pour la spécificité(taux de vrais négatifs)
champ_label4 = Label(fenetre,text ="\nRenseignez la spécificité (en %)")
champ_label4.pack()

specificite = Scale(fenetre, from_=0, to=100, orient=HORIZONTAL, length=350)
specificite.pack()

#Bouton pour lancer la simulation
bouton_simulation = Button(fenetre,text="Lancer la simulation",command=simulation)
bouton_simulation.pack()

#Bouton pour afficher une fenêtre d'aide
bouton_aide = Button(fenetre, text ="Explications",command=fenetreaide)
bouton_aide.pack()

#Bouton pour quitter le logiciel
bouton_quitter = Button(fenetre, text = "Quitter", command=fenetre.quit)
bouton_quitter.pack()



fenetre.mainloop()
