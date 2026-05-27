# Rapport SAé 105 - Nathan Duval
---
## 1. Les choix faits :
#### → Choix sur les parties du sujet libre :
- Répertorier les boites de nuits à l'échelle de la France (environ 1150)
- Statistiques : 
    - horaires connus
    - site internet
    - établissement payant
    - espace fumeur
    - présence de karaoke (donnée faible)
    - aménagement pour personne à mobilité réduite

###### Cela permet surtout de mettre en lumière le manque de statistiques sur un type d'établissement précis, car beaucoup de ces établissements existants ne sont pas représentés sur OpenStreetMap, mais aussi parce que beaucoup de ceux qui y sont bien répertoriés n'ont que très peu de détails.

#### → Choix techniques qu'il est pertinent de mentionner :
- Attribution du nom de l'établissement à la fiche OSM de l'établissement en question (get_node_name()).
- Utilisation d'un escalier de boucles pour atteindre les éléments voulus dans le JSON.
- Mise en place de messages (avec les codes d'erreur par exemple) pour comprendre l'attente ou l'échec des requêtes.
- Intégration d'une feuille de style CSS dans "md_to_html.py" pour des rapports HTML plus lisibles
- Le script "infos_locales.py" permet une saisie interactive d'une requête Overpass par la console grace à un "input".

---
## 2. Les difficultés rencontrées et les éventuelles solutions trouvées :
- Lorsque l'API ne renvoie aucun résultat, le programme risquait de planter lors du calcul des statistiques. 
    - Solution : Utilisation de "sys.exit()" avec un message pour arrêter l'exécution du programme entier.
- Les requêtes à l'échelle nationale étaient lentes ou bloquées. 
    - Solution : Augmentation du timeout et ajout de boucles de répétition en cas d'erreur de connexion pour éviter à l'utilisateur de rentrer 3 fois une requète à la suite lors d'une erreur.
- Beaucoup de nœuds OSM n'ont pas de nom ou de tags complets. 
    - Solution : Mise en place de "tests de présence" (if "tags" in ...) et attribution d'une valeur par défaut pour éviter les erreurs.
- Fiche OSM ne fonctionne qu'avec les node et non les way et relation
    - Sans solution

---
## 3. L’état d’avancement du projet au moment du rendu.
# $------Terminé------$
except : Fiche OSM ne fonctionne qu'avec les node et non les way et relation

---