# TrailMémoire — Note sur la sobriété numérique

## Principe directeur

TrailMémoire est un projet dédié à la pratique du trail, une discipline en pleine
nature. Il serait paradoxal que l'outil numérique qui lui est consacré contribue
à dégrader les ressources que les coureurs s'évertuent à préserver. La sobriété
numérique n'est donc pas une contrainte imposée par le cahier des charges : c'est
une cohérence de fond avec la philosophie du projet.

## Décisions d'architecture orientées sobriété

### 1. Rendu côté serveur
Le serveur Flask génère du HTML complet via Jinja2. Le navigateur reçoit une page
prête à afficher, sans exécuter de framework JavaScript. Cette approche réduit :
- la charge CPU du terminal client (moins de batterie consommée)
- le volume de données transférées (pas de bundle JS > 100 Ko)
- la complexité du système (un seul langage, côté serveur)

### 2. Zéro ressource externe au chargement
Aucune requête vers des serveurs tiers lors du chargement des pages :
- Polices système (`system-ui`) — 0 requête Google Fonts
- Pas de CDN pour les scripts ou styles
- Pas de trackers analytiques (Google Analytics, Hotjar, etc.)
- Pas de boutons de partage réseaux sociaux

### 3. Base de données légère et requêtes optimisées
SQLite est un fichier local — chaque requête est une lecture disque, pas un aller-
retour réseau. De plus, les requêtes SQL sont conçues pour :
- sélectionner uniquement les colonnes nécessaires (`SELECT col1, col2` et non `SELECT *`)
- paginer systématiquement les résultats (`LIMIT 20 OFFSET n`)
- utiliser des index sur les colonnes fréquemment filtrées (région, difficulté)
- éviter les N+1 queries (jointures plutôt que boucles de requêtes)

### 4. Pas de médias lourds
Le projet ne stocke pas d'images, de vidéos ni de fichiers audio. Les informations
sont textuelles. Ce choix est justifié par la nature du service (carnet de données
chiffrées) et élimine à lui seul la principale source de poids des pages web.

### 5. Interface sobre
- Pas d'animations CSS ni JavaScript
- Mode sombre automatique via `prefers-color-scheme` (réduit la consommation sur
  écrans OLED)
- Listes paginées (pas de scroll infini qui charge en continu)
- Hiérarchie visuelle claire avec un minimum d'éléments graphiques

### 6. Dépendances minimales
4 packages Python en production. Chaque package supplémentaire représente :
- des dépendances transitives potentiellement inutiles
- un risque de sécurité supplémentaire
- du code exécuté à chaque requête

## Indicateurs cibles

| Indicateur | Objectif |
|---|---|
| Poids total d'une page | < 200 Ko |
| Nombre de requêtes HTTP par page | < 10 |
| Score EcoIndex | A ou B |
| Score Lighthouse Performance | > 85 / 100 |
| First Contentful Paint (FCP) | < 1,5 s |
| Largest Contentful Paint (LCP) | < 2,0 s |
| Empreinte CO₂ / visite | < 0,05 g |

## Ce que TrailMémoire ne fera pas

- Pas de carte interactive (Leaflet, Google Maps) — une carte statique suffira si besoin
- Pas de téléchargement de fichiers GPX
- Pas de notifications push
- Pas de mode hors-ligne (PWA)
- Pas de publicités
- Pas de cookies tiers
- Pas de fonctionnalité sociale (likes, partages, followers)

Ces fonctionnalités apporteraient de la complexité sans valeur ajoutée proportionnelle
pour le périmètre défini.

## Référentiel consulté

Les décisions de ce projet s'appuient sur les recommandations du
[Référentiel d'éco-conception web](https://www.eco-conception-web.com/conseils-pro-eco-conception-web/)
ainsi que sur les principes du [GreenIT Analysis](https://www.greenit.fr).
