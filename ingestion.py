import matplotlib.pyplot as plt
import seaborn as sns

def validate_harmonization(df):
    """
    Exécute une batterie de tests visuels et statistiques sur le dataset unifié.
    """
    print(">>> Démarrage de la Validation de l'Harmonisation...\n")
    
    # --- TEST 1 : STATISTIQUES DESCRIPTIVES PAR SOURCE ---
    print("--- 1. Comparaison des Statistiques (Moyennes/Max) ---")
    cols_to_check = ['duration', 'src_pkts', 'src_bytes']
    
    # Groupby par source pour voir les écarts
    stats = df.groupby('dataset_source')[cols_to_check].describe(percentiles=[0.5])
    
    # Affichage simplifié (Moyenne et Max)
    for col in cols_to_check:
        print(f"\n[Metrique : {col}]")
        print(stats[col][['mean', '50%', 'max']])
        
    print("\n> INTERPRÉTATION : Vérifiez que les ordres de grandeur (mean) sont proches.")
    print("> Si CIC duration est ~1e-6 et TON ~10, la conversion microsecondes a échoué.")

    # --- TEST 2 : VISUALISATION (BOXPLOTS) ---
    print("\n--- 2. Génération des Graphiques de Distribution ---")
    
    # Configuration de la figure
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # On utilise une échelle logarithmique car les données réseaux ont souvent des pics énormes
    # Boxplot Duration
    sns.boxplot(x='dataset_source', y='duration', data=df, ax=axes[0], showfliers=False)
    axes[0].set_title("Distribution de la Durée (sans outliers extrêmes)")
    axes[0].set_ylabel("Secondes")

    # Boxplot Bytes (Log scale pour voir quelque chose)
    sns.boxplot(x='dataset_source', y='src_bytes', data=df, ax=axes[1])
    axes[1].set_yscale("log")
    axes[1].set_title("Volume d'Octets Source (Log Scale)")

    # Boxplot Packets (Log scale)
    sns.boxplot(x='dataset_source', y='src_pkts', data=df, ax=axes[2])
    axes[2].set_yscale("log")
    axes[2].set_title("Nombre de Paquets Source (Log Scale)")

    plt.suptitle("Comparaison Structurelle : CIC vs TON")
    plt.show()

    # --- TEST 3 : DISTRIBUTION DES PROTOCOLES ---
    print("\n--- 3. Vérification du Mapping des Protocoles ---")
    proto_counts = df.groupby(['dataset_source', 'protocol']).size().unstack(fill_value=0)
    print(proto_counts)
    print("> VÉRIFICATION : Vous ne devriez voir que des entiers (6, 17, 1).")
    print("> Si vous voyez 'tcp' ou 'UDP', le mapping a échoué.")

# --- EXÉCUTION ---
# Supposons que 'dataset_final' est le résultat de votre fonction d'ingestion précédente
# validate_harmonization(dataset_final)