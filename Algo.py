
def Vehiculescore(nomdelavoiture, carburant, nbKyloParAn):
    #tout le score de la voiture
    citadine = 8
    cabriolet = 6
    berline = 6.5
    suv = 4
    totalscore = 0
    if nomdelavoiture == "Citadine":
        totalscore = totalscore + citadine
    if nomdelavoiture == "Cabriolet":
        totalscore = totalscore + cabriolet
    if nomdelavoiture == "Berline":
        totalscore = totalscore + berline
    if nomdelavoiture == "SUV":
        totalscore = totalscore + suv

    
    essence = 5
    electrique = 9
    gaz = 6
    diesel = 4
    hybride = 7
    if carburant == "Essence":
        totalscore = totalscore + essence
    if carburant == "Electrique":
        totalscore = totalscore + electrique
    if carburant == "Gaz":
        totalscore = totalscore + gaz
    if carburant == "Diesel":
        totalscore = totalscore + diesel
    if carburant == "Hybride":
        totalscore = totalscore + hybride
  
    if nbKyloParAn == "5000 - 10000 km":
        totalscore = totalscore + 9
    if nbKyloParAn == "10000 - 15000 km":
        totalscore = totalscore + 7
    if nbKyloParAn == "15000 - 20000 km":
        totalscore = totalscore + 5
    if nbKyloParAn == "20000 - 25000 km":
        totalscore = totalscore + 3
    if nbKyloParAn == "25000 - 30000 km":
        totalscore = totalscore + 1
 
    return totalscore
def Years(whatYear, nomdelavoiture, carburant, nbKyloParAn):
    score = Vehiculescore(nomdelavoiture, carburant, nbKyloParAn) 
    #On ajoute au score le nombre en fonction de l'anné de construction   
    if whatYear == "1960-1970":
        score += 1
    if whatYear == "1970-1990":
        score += 2
    if whatYear == "1990-2000":
        score += 4
    if whatYear == "2000-2010":
        score += 5
    if whatYear == "Après 2010":
        score += 7
    return score

#Avant dernier du calcul taux
def Eval(whatYear, nomdelavoiture, carburant, nbKyloParAn):
    score = Years(whatYear, nomdelavoiture, carburant, nbKyloParAn)
    print(score)
    if score <= 10:
        taux = 3
    if score > 10 and score <= 15:
        taux = 2.74
    if score > 15 and score <= 25:
        taux = 2.52
    if score > 25 and score <= 33:
        taux = 2.10
    if score > 33 and score < 40:
        taux = 1.85
    return taux

#Dernier calcul de taux
def AddPassager(nbpassager,whatYear, nomdelavoiture, carburant, nbKyloParAn):
    taux = Eval(whatYear, nomdelavoiture, carburant, nbKyloParAn)
    
    if nbpassager == "1":
        taux += 0.11
    if nbpassager == "2":
        taux -= 0.17
    if nbpassager == "3":
        taux -= 0.29
    if nbpassager == "4":
        taux -= 0.53   
    return taux
#print(AddPassager("1","Après 2010", "Citadine", "Essence", "520000 - 25000 km"))