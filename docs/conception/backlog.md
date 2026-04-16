# T.R.A.I.L — Mini Backlog Produit

Priorités : **Haute** = MVP bloquant / **Moyenne** = utile pour la démo / **Basse** = nice-to-have
Difficulté : **F** = Facile (< 2h) / **M** = Moyen (2–4h) / **D** = Difficile (> 4h)

---

## Authentification et gestion des utilisateurs

| ID    | Fonctionnalité | Priorité | Difficulté | US liée |
|-------|----------------|----------|------------|---------|
| AU-01 | Formulaire d'inscription avec validation e-mail et hash bcrypt | Haute | F | US-01 |
| AU-02 | Page de connexion avec gestion de session Flask-Login | Haute | F | US-01 |
| AU-03 | Déconnexion et invalidation de session | Haute | F | US-01 |
| AU-04 | Page « Mon profil » : infos + liste de mes rapports + mes sentiers | Moyenne | F | US-02 |
| AU-05 | Modification du profil (nom, niveau, localisation) | Moyenne | F | US-02 |
| AU-06 | Suppression du compte avec confirmation et cascade | Basse | F | US-03 |
| AU-07 | Page admin — liste paginée des utilisateurs avec suppression | Basse | M | US-04 |

## Sentiers

| ID    | Fonctionnalité | Priorité | Difficulté | US liée |
|-------|----------------|----------|------------|---------|
| SE-01 | Liste des sentiers paginée avec filtres région, difficulté, type de pratique + statut actuel | Haute | M | US-05 |
| SE-02 | Page de détail : infos sentier + rapports actifs (non expirés) colorés | Haute | M | US-08 |
| SE-03 | Formulaire d'ajout de sentier (multi-type de pratique) avec validation serveur | Haute | M | US-06 |
| SE-04 | Modification d'un sentier (propriétaire uniquement) | Moyenne | F | US-06 |
| SE-05 | Suppression d'un sentier avec confirmation (propriétaire uniquement) | Moyenne | F | US-06 |

## Rapports de conditions

| ID    | Fonctionnalité | Priorité | Difficulté | US liée |
|-------|----------------|----------|------------|---------|
| RA-01 | Formulaire de dépôt de rapport (statut, type pratique, obstacles checkboxes, commentaire) | Haute | M | US-07 |
| RA-02 | Calcul automatique date_expiration = date_rapport + 7 jours (côté serveur) | Haute | F | US-07 |
| RA-03 | Filtrage des rapports expirés dans toutes les requêtes (`date_expiration > NOW`) | Haute | F | US-08 |
| RA-04 | Modification d'un rapport (propriétaire uniquement) | Moyenne | F | US-07 |
| RA-05 | Suppression d'un rapport avec confirmation | Moyenne | F | US-07 |

## Green IT et qualité

| ID    | Fonctionnalité | Priorité | Difficulté | US liée |
|-------|----------------|----------|------------|---------|
| GR-01 | Interface HTML/CSS natif sobre, responsive, mode sombre automatique, statuts colorés | Haute | M | US-09 |
| GR-02 | Minification CSS en production | Basse | F | US-09 |
| GR-03 | Mesures EcoIndex + Lighthouse avant/après optimisations | Moyenne | F | US-09 |
| GR-04 | Affichage CO₂/visite en pied de page (Website Carbon) | Basse | F | US-10 |
| GR-05 | Déploiement Render.com avec CI/CD depuis la branche main | Haute | M | — |
| GR-06 | GitHub Actions : lint Python (flake8) à chaque push | Basse | F | — |

---

## Récapitulatif

| Priorité | Nombre de tâches |
|----------|-----------------|
| Haute    | 10              |
| Moyenne  | 8               |
| Basse    | 5               |
| **Total**| **23**          |

## Ordre de développement suggéré

1. **AU-01, AU-02, AU-03** — authentification (base de tout)
2. **SE-01, SE-02** — lecture des sentiers avec statut (démo rapide possible)
3. **SE-03, SE-04, SE-05** — CRUD sentiers complet
4. **RA-01, RA-02, RA-03** — dépôt de rapport + expiration (cœur du service)
5. **RA-04, RA-05** — modification/suppression rapports
6. **AU-04, AU-05, AU-06** — profil utilisateur
7. **GR-01** — interface sobre avec statuts colorés (en parallèle)
8. **GR-03, GR-04, GR-05** — Green IT, mesures et déploiement
9. **AU-07, GR-02, GR-06** — admin et automatisation
