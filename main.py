categories = {
    "Nourriture"  : 0,
    "Transport"   : 0,
    "Abonnements" : 0,
    "Revenus"     : 0,
    "Autre"       : 0
}

with open("data/transactions.csv", "r", encoding="utf-8") as f:
    f.readline()        
    for ligne in f :
        l = ligne.strip()   
        l = l.split(",") 
        montant = float(l[2])
        if montant > 0 :
            categories["Revenus"] += montant
        elif ("UBER" in l[1]) or ("CARREFOUR" in l[1]):
            categories["Nourriture"] += montant
        elif ("RATP" in l[1]):
            categories["Transport"] += montant
        elif ("NETFLIX" in l[1]):
            categories["Abonnements"] += montant
        else :
            categories["Autre"] += montant

for cle in categories :
    print(cle, " : ", f"{categories[cle]:.2f}")

with open("output/resume.csv", "w", encoding="utf-8") as f:
    f.write("categorie,total,type\n")
    for cle in categories :
        if (categories[cle]<0) :
            nature = "depense"
        elif (categories[cle]>0) :
            nature = "revenu"
        else : 
            nature = "neutre"
        f.write(f"{cle},{categories[cle]:.2f},{nature}\n")