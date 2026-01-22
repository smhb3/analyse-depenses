\# Analyse de dépenses



Outil Python permettant d’analyser un fichier CSV de transactions bancaires et de produire un résumé par catégorie, en distinguant dépenses, revenus et montants neutres.



Ce projet est orienté analyse de données et constitue une base évolutive pour un outil plus complet de traitement de données financières.



---



\## Fonctionnalités



\- Lecture d’un fichier CSV de transactions bancaires

\- Catégorisation des transactions (Nourriture, Transport, Abonnements, Revenus, Autre)

\- Distinction entre dépenses, revenus et montants neutres (+-0€)

\- Agrégation des montants par catégorie

\- Génération d’un fichier de sortie 'resume.csv'



---



\## Structure du projet



analyse-depenses/

├── data/

│ └── transactions.csv

├── output/

│ └── resume.csv

├── main.py

└── README.md





\- 'data/transactions.csv' : fichier d’entrée contenant les transactions

\- 'output/resume.csv' : fichier généré contenant le résumé par catégorie

\- 'main.py' : script principal



---



\## Utilisation



Depuis la racine du projet, exécuter : python main.py

Le programme :

\- lit les données depuis `data/transactions.csv`

\- effectue l’analyse et la catégorisation

\- génère automatiquement le fichier `output/resume.csv`



---



\## Format du fichier d’entrée



Le fichier CSV d’entrée doit contenir au minimum les colonnes suivantes : 

date,libelle,montant



---



\## Exemple de sortie



categorie,total,type

Nourriture,-77.52,depense

Transport,-2.10,depense

Abonnements,-13.99,depense

Revenus,1200.00,revenu

Autre,0.00,neutre





---



\## État du projet



Le projet est en cours de développement.  

Il constitue une première version fonctionnelle servant de base pour des évolutions futures, notamment :

\- paramétrage du fichier d’entrée et de sortie

\- règles de catégorisation configurables

\- interface en ligne de commande (CLI)

\- tests automatisés

\- amélioration de la robustesse sur des données réelles



---



\## Objectif pédagogique



Ce projet a pour objectif de :

\- pratiquer Python par des cas concrets

\- apprendre à structurer un projet de traitement de données

\- mettre en place des bonnes pratiques (organisation, versionnement, documentation)











