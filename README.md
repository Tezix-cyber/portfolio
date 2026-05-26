# 📂 Portfolio Universitaire — BUT Réseaux & Télécommunications

Bienvenue sur le dépôt du portfolio numérique de **Nathan Duval**, étudiant en **BUT Réseaux & Télécommunications** (Promotion 2025–2028) à l'IUT d'Ifs (Campus 3, Université de Caen), spécialisé en **Cybersécurité**.

Ce portfolio documente mon parcours académique, mes compétences acquises selon le référentiel national BUT R&T, ainsi que mes travaux pratiques et projets phares (SAÉ).

---

## 🌟 Caractéristiques & Fonctionnalités

Le site a été conçu de A à Z en intégrant des standards web modernes :
*   **Design Premium & Moderne** : Thème sombre/clair minimaliste et soigné, inspiré des interfaces professionnelles.
*   **Mode Sombre Persistant** : Bascule du thème gérée en JavaScript avec sauvegarde automatique de la préférence dans le stockage local (`localStorage`).
*   **Effet 3D Interactif & Glow** : Micro-animations dynamiques sur les cartes de compétences et de projets au survol de la souris (technologie CSS Grid & JS Variables).
*   **Barre de Progression de Lecture** : Indication visuelle de la progression de défilement (Scroll Progress Bar) intégrée en haut de chaque page.
*   **Copie Rapide d'E-mail** : Un clic sur un bouton de contact copie automatiquement l'adresse e-mail dans le presse-papiers tout en affichant un indicateur de succès.
*   **Accessibilité et Standardisation** : Structure sémantique HTML5 validée par le W3C et respect des contrastes de lisibilité WCAG.

---

## 📁 Structure du Projet

Le projet est organisé de manière modulaire :

```text
portfolio/
├── index.html                  # Page d'accueil du portfolio
├── presentation.html           # Présentation du profil (parcours, bac NSI/SI, objectifs)
├── competences.html            # Synthèse et bilan par compétences du BUT (C1, C2, C3, C4)
├── bilan.html                  # Bilan global et projection professionnelle
├── README.md                   # Ce fichier de documentation (README)
├── css/
│   └── style.css               # Feuille de style globale (variables, resets, thèmes, media queries)
├── js/
│   └── script.js               # Logique JS (Mode sombre, effet 3D tilt, copie d'e-mail, scroll progress)
├── doc_image/
│   ├── CV.pdf                  # Curriculum Vitae téléchargeable
│   └── favicon.svg             # Favicon vectorielle du site
├── image/
│   └── photo_moi.png           # Photo de profil
├── SAES/
│   ├── saes.html               # Page d'index répertoriant tous les projets
│   ├── sae-102.html            # Détail SAÉ 1.2 — S'initier au réseau informatique
│   ├── sae-103.html            # Détail SAÉ 1.3 — Découverte d'un dispositif de transmission
│   ├── sae-104.html            # Détail SAÉ 1.4 — Se présenter sur Internet
│   └── sae-105.html            # Détail SAÉ 1.5 — Traitement de données
└── preuves_sae_*/              # Livrables, schémas de topologie et rapports PDF des projets
```

---

## 🛠️ Projets Académiques Documentés (SAÉ)

1.  **[SAÉ 1.2 — S'initier au réseau informatique](SAES/sae-102.html)** : Restructuration complète d'un LAN d'entreprise avec routage inter-VLAN (Cisco L3), virtualisation Proxmox d'un serveur Debian 13 (DNS, DHCP, Samba) et durcissement SSH selon l'ANSSI.
2.  **[SAÉ 1.3 — Découverte d'un dispositif de transmission](SAES/sae-103.html)** : Caractérisation de lignes cuivre (coaxial, RJ45) par réflectométrie (DTF) et bilan de puissance d'une liaison fibre optique (photométrie).
3.  **[SAÉ 1.4 — Se présenter sur Internet](SAES/sae-104.html)** : Création d'un site vitrine responsive et accessible sur la Musique Assistée par Ordinateur (MAO), avec gestion de projet (WBS, Gantt, Kanban).
4.  **[SAÉ 1.5 — Traitement de données](SAES/sae-105.html)** : Scripting Python interrogeant l'API Overpass (OpenStreetMap) pour compiler des statistiques de complétude sur les établissements en France.

---

## 🚀 Lancement Local

Pour visualiser le portfolio en local :
1.  Clonez ce dépôt ou téléchargez le ZIP :
    ```bash
    git clone https://github.com/Tezix-cyber/portfolio.git
    ```
2.  Ouvrez le fichier `index.html` dans le navigateur de votre choix.

---

## 👨‍💻 Auteur

*   **Nathan Duval**
    *   BUT Réseaux & Télécommunications, Promo 2025–2028
    *   GitHub : [@Tezix-cyber](https://github.com/Tezix-cyber)
    *   LinkedIn : [Profil LinkedIn](https://www.linkedin.com/in/nathan-duval-485265410/)
