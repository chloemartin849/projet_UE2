import pandas as pd
import numpy as np

# 1. Charger vos données
# Remplacez 'votre_fichier.csv' par le nom réel de votre fichier
df = pd.read_csv('Raphael Tambouille\CWB_allnontraite.csv')

# 2. Liste des colonnes CWB extraites de vos nouveaux headers
cols_cwb = ['CWB2020', 'CWB2021', 'CWB2022', 'CWB2023', 'CWB2024']

def filtrer_par_annee(row):
    # On récupère l'année de l'observation (ex: 2020)
    annee_obs = str(int(row['year']))
    
    # On parcourt chaque colonne CWB
    for col in cols_cwb:
        # Si le nom de la colonne ne contient pas l'année de l'observation, on vide la cellule
        if annee_obs not in col:
            row[col] = np.nan # Équivalent de NULL en Python/Pandas
            
    return row

# 3. Appliquer le nettoyage sur chaque ligne
df_nettoye = df.apply(filtrer_par_annee, axis=1)

# 4. Sauvegarder le résultat dans un nouveau fichier
df_nettoye.to_csv('donnees_cwb_nettoyees_non_concatene.csv', index=False)

print("Le fichier a été nettoyé. Seule la colonne CWB correspondant à l'année est conservée par ligne.")