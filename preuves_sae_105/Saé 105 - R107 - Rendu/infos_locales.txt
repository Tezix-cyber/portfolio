import requests
import time
import json
from md_to_html import convert
import sys

def get_dataset(query: str) -> dict:
    tentatives_max = 5
    for i in range(tentatives_max):
        url = "https://overpass-api.de/api/interpreter?data=" + query
        reponse = requests.get(url)
        if reponse.status_code == 200:
            donnees = reponse.json()
            if not donnees.get("elements"):
                # Pour "faire crasher" proprement sans message d'erreur
                sys.exit("---------- Aucun résultat trouvé pour cette zone. ---------- ")
            with open("dataset.json", "w", encoding="utf-8") as fichier:
                json.dump(donnees, fichier, indent=4)
            print("Tentative " + str(i+1) + " : succés !")
            print("-> Fichier result.md et result.html créé")
            return donnees
        elif reponse.status_code == 429:
            print("Tentative " + str(i+1) + " : Trop de requêtes, attente plus longue...")
            time.sleep(10)
        elif reponse.status_code == 504:
            print("Tentative " + str(i+1) + " : serveur surchargé, attendez un instant.")
            time.sleep(5)
        else:
            print("Erreur code " + str(reponse.status_code))
            return
    print("Échec après " + str(tentatives_max) + " tentatives.")

def compute_statistics(f_dataset)->str:
    """
    Analyse les données récupérées pour calculer des statistiques.
    """
    with open(f_dataset, 'r', encoding='utf-8') as fichier:
        data = json.load(fichier)
    # On récupère la liste de tous les établissements trouvés
    liste_clubs = data.get("elements", [])
    # On prépare nos compteurs pour les différentes infos qu'on veut analyser
    total = 0
    nb_horaires = 0
    nb_web = 0
    nb_payant = 0
    nb_fumeur = 0
    nb_karaoke = 0
    nb_hand = 0
    # On parcourt chaque établissement un par un
    for club in liste_clubs:
        total += 1
        # On vérifie si l'établissement a des informations (tags) associées
        if "tags" in club:
            tags = club["tags"]
            # On regarde si les horaires d'ouverture sont renseignés
            if "opening_hours" in tags:
                nb_horaires += 1          
            # On vérifie s'il y a un site web, page Facebook ou autre présence en ligne
            if "website" in tags or "contact:website" in tags or "contact:facebook" in tags:
                nb_web += 1          
            # On compte combien d'établissements sont payants à l'entrée
            if "fee" in tags and tags["fee"] == "yes":
                nb_payant += 1          
            # On regarde si l'établissement autorise de fumer (tout sauf "no")
            if "smoking" in tags and tags["smoking"] != "no":
                nb_fumeur += 1
            # On compte ceux qui proposent du karaoke (info assez rare)
            if "karaoke" in tags and tags["karaoke"] == "yes":
                nb_karaoke += 1
            # On vérifie si l'endroit est accessible aux personnes à mobilité réduite
            if "wheelchair" in tags and tags["wheelchair"] != "no":
                nb_hand += 1
    # Si on a trouvé au moins un établissement, on calcule les pourcentages
    if total > 0:
        # On transforme nos compteurs en pourcentages pour mieux visualiser
        pourcentage_horaires = (nb_horaires / total) * 100
        pourcentage_web = (nb_web / total) * 100
        pourcentage_payant = (nb_payant / total) * 100
        pourcentage_fumeur = (nb_fumeur / total) * 100
        pourcentage_karaoke = (nb_karaoke / total) * 100
        pourcentage_hand = (nb_hand / total) * 100
        # On rassemble toutes les statistiques dans un dictionnaire
        statistiques = {
            "total": total,
            "nb_horaires": nb_horaires,
            "pourcentage_horaires": round(pourcentage_horaires, 2),
            "nb_web": nb_web,
            "pourcentage_web": round(pourcentage_web, 2),
            "nb_payant": nb_payant,
            "pourcentage_payant": round(pourcentage_payant, 2),
            "nb_fumeur": nb_fumeur,
            "pourcentage_fumeur": round(pourcentage_fumeur, 2),
            "nb_karaoke": nb_karaoke,
            "pourcentage_karaoke": round(pourcentage_karaoke, 2),
            "nb_hand": nb_hand,
            "pourcentage_hand": round(pourcentage_hand, 2)
        }
        return statistiques
    else:
        # Si on n'a rien trouvé, on prévient l'utilisateur (message déjà transmis lors de la levée d'exception plus haut)
        print("Aucune boîte de nuit trouvée dans cette zone.")
        return None

def dataset_to_md(dataset: dict, filename: str) -> None:
    # On charge les données JSON depuis le fichier
    with open(dataset, 'r', encoding='utf-8') as f:
        data = json.load(f)
    # On récupère toutes les statistiques calculées
    stats = compute_statistics(dataset) 
    # On commence à écrire notre fichier Markdown avec tous les résultats
    with open(filename, "w", encoding="utf-8") as fichier:
        # Entête du document
        fichier.write("# Résultat : \n\n --- \n\n")
        # Si on a des statistiques à afficher (donc des établissements trouvés)
        if stats:
            fichier.write("## Statistiques : \n\n")            
            # Le nombre total d'établissements trouvés
            fichier.write("### **Nombre de boîtes de nuit trouvées :** " + str(stats["total"]) + "\n\n")          
            # Infos sur les horaires d'ouverture
            fichier.write("##### Nombre d'établissement avec **horaires connus** : " + str(stats["nb_horaires"]) + "\n")
            fichier.write("##### Pourcentage d'établissement avec horaires connus : " + str(stats["pourcentage_horaires"]) + "%" + "\n\n")           
            # Infos sur la présence web
            fichier.write("##### Nombre d'établissement avec **site internet** _RÉFÉRENCÉ_ : " + str(stats["nb_web"]) + "\n")
            fichier.write("##### Pourcentage d'établissement avec site internet : " + str(stats["pourcentage_web"]) + "%" + "\n\n")           
            # Infos sur les établissements payants
            fichier.write("##### Nombre d'établissement **payant** _RÉFÉRENCÉ_ : " + str(stats["nb_payant"]) + "\n")
            fichier.write("##### Pourcentage d'établissement payant : " + str(stats["pourcentage_payant"]) + "%" + "\n\n")           
            # Infos sur les espaces fumeurs
            fichier.write("##### Nombre d'établissement avec **espace fumeur** _RÉFÉRENCÉ_ : " + str(stats["nb_fumeur"]) + "\n")
            fichier.write("##### Pourcentage d'établissement avec espace fumeur : " + str(stats["pourcentage_fumeur"]) + "%" + "\n\n")           
            # Infos sur le karaoke
            fichier.write("##### Nombre d'établissement avec **karaoke** _RÉFÉRENCÉ_ : " + str(stats["nb_karaoke"]) + "\n")
            fichier.write("##### Pourcentage d'établissement avec karaoke : " + str(stats["pourcentage_karaoke"]) + "%" + "\n\n")           
            # Infos sur l'accessibilité handicapés
            fichier.write("##### Nombre d'établissement avec un **aménagement pour personne à mobilité réduite** _RÉFÉRENCÉ_ : " + str(stats["nb_hand"]) + "\n")
            fichier.write("##### Pourcentage d'établissement avec un aménagement pour personne à mobilité réduite : " + str(stats["pourcentage_hand"]) + "%" + "\n\n")           
            # Petit message d'avertissement important pour bien interpréter les résultats (car certains manque de données)
            fichier.write("#### ***Attention*** Les pourcentages faibles indiquent souvent un manque de données sur OpenStreetMap." + "\n\n")
        # Séparateur avant la liste détaillée
        fichier.write("\n---\n\n## Liste des établissements\n\n") 
        # On affiche maintenant tous les établissements avec leurs détails
        elements = data.get("elements")
        for club in elements:
            tags = club.get("tags")           
            # On récupère le nom ou on met "Sans nom" si pas de nom renseigné
            if "name" in tags:
                nom = tags.get("name")
            else:
                nom = "Sans nom"            
            # Titre de l'établissement avec son ID
            fichier.write("#### " + str(nom) + " (ID: " + str(club.get("id")) + ")\n")          
            # On liste toutes les informations disponibles pour cet établissement
            if tags:
                for cle, valeur in tags.items():
                    fichier.write("- **" + str(cle) + "** : " + str(valeur) + "\n")            
            # Espace entre chaque établissement pour la lisibilité
            fichier.write("\n")

def infos_locales(query) -> None:
    get_dataset(query)
    dataset_to_md("dataset.json", "result.md")
    convert("result.md", "result.html")


#--------------------------------------------------------------------------------------------------------------------------------------------------

# boulangeries à Ifs
#ma_requete = '[out:json];area["name"="Ifs"]->.a;(node["shop"="bakery"](area.a););out;'

#-------------------------

# Boîtes de nuit en Normandie
#ma_requete = '[out:json];area["name"="Normandie"]->.a;(node["amenity"="nightclub"](area.a);way["amenity"="nightclub"](area.a););out;'

#-------------------------

# Boîtes de nuit en France
#ma_requete = '[out:json];area["name"="France"]["admin_level"="2"]->.zone;(node["amenity"="nightclub"](area.zone);way["amenity"="nightclub"](area.zone);relation["amenity"="nightclub"](area.zone););out geom;'

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""
if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Utilisation : ipython info_locales.py")
    else:
        infos_locales(ma_requete)
"""
#-------------------------

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("----------ERREUR----------")
        print("Utilisation : ipython info_locales.py")
        print("Vous pouvez ensuite entrez une zone après la demande")
        print("--------------------------")
    else:
        zone = input("Entrez une zone/ville/département/région/pays : ")
        ma_requete_custom = ('[out:json];area["name"="'+zone+'"]->.zone;(node["amenity"="nightclub"](area.zone);way["amenity"="nightclub"](area.zone);relation["amenity"="nightclub"](area.zone););out geom;')
        infos_locales(ma_requete_custom)
