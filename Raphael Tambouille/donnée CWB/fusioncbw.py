import pandas as pd
import numpy as np

# 1. Charger votre fichier nettoyé (celui avec les NaN)
df = pd.read_csv('donnees_cwb_nettoyees_non_concatene.csv')

# 2. Liste des colonnes à fusionner
cols_cwb = ['CWB2020', 'CWB2021', 'CWB2022', 'CWB2023', 'CWB2024']

# 3. Fusionner les colonnes
# La fonction 'bfill' (backfill) va chercher la seule valeur non-nulle sur la ligne
# parmi les colonnes CWB et la ramener dans une nouvelle colonne.
df['CWB_valeur'] = df[cols_cwb].bfill(axis=1).iloc[:, 0]

# 4. Nettoyage final : on supprime les anciennes colonnes CWB annuelles
# On ne garde que la colonne fusionnée 'CWB_valeur'
df_final = df.drop(columns=cols_cwb)

# 5. Sauvegarder le résultat final
df_final.to_csv('donnees_cwb_fusionnees.csv', index=False)

print("Fusion terminée ! Les colonnes annuelles ont été regroupées dans 'CWB_valeur'.")
print(df_final[['fid', 'year', 'CWB_valeur']].head())