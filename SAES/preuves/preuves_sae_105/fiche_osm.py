import sys
import requests
from md_to_html import convert
import math
from PIL import Image, ImageDraw

def get_node(id: int) -> dict:
    """Récupère les données brutes d'un nœud OpenStreetMap au format JSON via l'API officielle."""
    # NE FONCTIONNE QU'AVEC LES NOEUD ET NON LES WAY ET RELATION CAR PLUS COMPLIQUé DE TROUVER LES COORDONNéES etc...
    url = "https://api.openstreetmap.org/api/0.6/node/" + str(id) + ".json"
    response = requests.get(url)
    json_data = response.json()
    return json_data

def get_node_name(id: int) -> str:
    """Parcourt le JSON du nœud pour extraire la valeur du tag 'name'. Retourne l'id si le nom n'existe pas."""
    data = get_node(id)
    for titre, element in data.items():
        if titre == "elements":
            for objet in element:
                for cle, valeur in objet.items():
                    if cle == "tags" and type(valeur) == dict:
                        for tag_cle, tag_val in valeur.items():
                            if tag_cle == "name":
                                return tag_val
    return str(id)

def calculer_tuile(lat_deg:float, lon_deg:float, zoom:int):
    lat_rad = math.radians(float(lat_deg))
    n = 2.0 ** zoom
    x_tuile = (float(lon_deg) + 180.0) / 360.0 * n
    y_tuile = (1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n
    return x_tuile, y_tuile

def generer_carte(latitude:float, longitude:float, zoom:int, id:int):
    x, y = calculer_tuile(latitude, longitude, zoom)
    xf, yf = calculer_tuile(latitude, longitude, zoom)
    x = int(xf)
    y = int(yf)
    px = int((xf - x) * 256)
    py = int((yf - y) * 256)
    ville = get_ville(latitude, longitude)
    url_image = "https://tile.openstreetmap.org/" + str(zoom) + "/" + str(x) + "/" + str(y) + ".png"
    # Identification nécessaire pour télécharger l'image (info IA)
    entete = {'User-Agent': 'MonAppPython/1.0'}
    reponse_image = requests.get(url_image, headers=entete)
    nom_image = "carte_" + str(id) + ".png"
    if reponse_image.status_code == 200:
        with open(nom_image, "wb") as f_image:
            f_image.write(reponse_image.content)
        image = Image.open(nom_image).convert("RGBA")
        dessin = ImageDraw.Draw(image)
        rayon = 5
        dessin.regular_polygon((px, py-4, rayon), 3, rotation=180, fill="red", outline="red")
        dessin.circle((px, py-9), rayon-0.5, fill="white", outline="red", width=2)
        dessin.text((3, 0), ville, fill="black",font_size=25, stroke_width=0.7)
        image.save(nom_image)
        return nom_image
    return None

def get_ville(latitude: float, longitude: float) -> str:
    # aide IA
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {"lat": latitude,"lon": longitude,"format": "json","zoom": 10,"addressdetails": 1}
    entete = {'User-Agent': 'MonAppPython/1.0'}
    response = requests.get(url, params=params, headers=entete)
    response.raise_for_status()
    data = response.json()
    adresse = data.get("address")
    return (adresse.get("city") or adresse.get("town") or adresse.get("village") or adresse.get("municipality") or "Ville inconnue")

def node_to_md(data: dict, filename: str, nom_image_carte, id) -> None:
    """Prend les données JSON et écrit tous les tags (clés/valeurs) dans un fichier au format Markdown."""
    with open(filename, "w", encoding="utf-8") as fichier:
        for titre, element in data.items():
            if titre == "elements":
                for objet in element:
                    for cle, valeur in objet.items():
                        if cle == "tags" and type(valeur) == dict:
                            fichier.write("# **Infos sur :** ***" + get_node_name(id) + "*** \n\n")
                            for tag_cle, tag_val in valeur.items():
                                fichier.write("- " + tag_cle + " : " + tag_val + "\n")
                            if nom_image_carte != None:
                                fichier.write("\n\n ![Carte locale](" + nom_image_carte + ")\n\n")
                                fichier.write("---\n\n")
                fichier.write("\n")                

def fiche_osm(id: int) -> None:
    """Fonction maîtresse : récupère le nom, crée le fichier Markdown et le convertit en HTML."""
    donnees = get_node(id)
    latitude = 0
    longitude = 0
    for titre, element in donnees.items():
        if titre == "elements":
            for objet in element:
                latitude = objet.get("lat")
                longitude = objet.get("lon")
    image = generer_carte(latitude, longitude, 12, id)
    nom_fichier = get_node_name(id)
    nom_fichier_propre = ""
    for i in nom_fichier:
        if i != " ":
            nom_fichier_propre += i
    node_to_md(donnees, nom_fichier + ".md", image, id)
    convert(nom_fichier + ".md", nom_fichier_propre + ".html")
    print("-> Fiche créée pour " + nom_fichier)
    print("----------------------------------------")

#-------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : ipython fiche_osm.py *id*")
    else:
        node_id = int(sys.argv[1])
        print("----------------------------------------")
        print("Nom de l'établissement :", get_node_name(node_id))
        fiche_osm(node_id)


#----------------------------------------------------------------------------------------------------------------------------------------------------------


#print(get_node(7991140667))
#print(get_node_name(7991140667))
#node_to_md(get_node(7991140667), "node_7991140667.md")
#fiche_osm(7991140667)

