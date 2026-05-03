# T.R.A.I.L — Proposition de valeur et cadrage produit

## Nom du projet

**T.R.A.I.L** — *Terrain Rando Alerte Info Live*

## Proposition de valeur

T.R.A.I.L est une plateforme communautaire sobre qui répond à une question simple et concrète :

> **"Ce sentier est-il praticable ce weekend ?"**

Les coureurs trail, VTTistes et randonneurs font face à un problème récurrent : les informations sur l'état réel des sentiers sont éparpillées (groupes Facebook, bouche-à-oreille, forums), souvent périmées, et inexistantes pour beaucoup de zones. Résultat : des déplacements inutiles, des sorties annulées ou, pire, des situations dangereuses.

T.R.A.I.L centralise des **rapports de conditions géolocalisés par sentier**, déposés par la communauté, avec **expiration automatique à 7 jours** pour garantir la fraîcheur des données.

## Besoin utilisateur réel

Avant une sortie, un pratiquant veut savoir :
1. Le sentier est-il **praticable, partiellement praticable ou fermé** ?
2. Quels sont les **obstacles actuels** (neige, boue, crue, arbre tombé, travaux) ?
3. Quel **type de pratique** est concerné (trail ≠ VTT ≠ rando sur un même sentier) ?
4. **Quand** l'information a-t-elle été déposée ? Est-elle encore valide ?

## Utilisateurs cibles

- **Coureurs trail** — souhaitent savoir si le sentier est sec/enneigé/boueux avant de partir
- **VTTistes** — sensibles à la boue et aux obstacles techniques (rochers, arbres tombés)
- **Randonneurs** — attentifs aux conditions météo et à la dangerosité (verglas, crue)
- **Organisateurs de sorties en club** — besoin d'information fiable pour valider un itinéraire

Âge : 18–60 ans. Pratiquants réguliers, connectés via smartphone.

## Différenciation

| | T.R.A.I.L | AllTrails / Komoot | Strava | Groupes Facebook |
|---|---|---|---|---|
| Conditions en temps réel | ✅ | ⚠ (rare, non structuré) | ❌ | ⚠ (dispersé) |
| Expiration automatique | ✅ | ❌ | — | ❌ |
| Multi-pratique (trail/VTT/rando) | ✅ | Partiel | ❌ | ❌ |
| Interface légère / sobre | ✅ | ❌ (lourd) | ❌ (lourd) | ❌ |
| Sans compte requis (lecture) | ✅ | ⚠ | ❌ | ⚠ |

## Périmètre du MVP

### Inclus dans le MVP

| Fonctionnalité | Justification |
|---|---|
| Inscription / connexion / déconnexion | Pré-requis pour déposer un rapport |
| CRUD utilisateurs (profil, modification, suppression) | Obligatoire (cahier des charges) |
| Consulter la liste des sentiers (pagination, filtre région / difficulté / type) | Fonctionnalité centrale — sans connexion |
| Voir le détail d'un sentier + rapports de conditions actifs | Valeur principale |
| Ajouter / modifier / supprimer un sentier | Contribution à la base |
| Déposer / modifier / supprimer un rapport de conditions | Cœur du service |
| Expiration automatique des rapports à 7 jours | Garantie de fraîcheur |
| Interface sobre, paginée, responsive | Critère Green IT |

### Hors MVP (versions futures)

- Notifications par e-mail si conditions changent sur un sentier favori
- Carte statique par région (image WebP)
- Export CSV de l'historique des rapports
- API publique pour intégration avec d'autres outils

## Rôles utilisateurs et permissions

| Action | Visiteur | Pratiquant connecté | Administrateur |
|---|---|---|---|
| Consulter les sentiers | ✅ | ✅ | ✅ |
| Consulter les rapports | ✅ | ✅ | ✅ |
| S'inscrire / se connecter | ✅ | — | — |
| Ajouter un sentier | ❌ | ✅ | ✅ |
| Modifier **son** sentier | ❌ | ✅ | ✅ |
| Supprimer **son** sentier | ❌ | ✅ | ✅ |
| Déposer un rapport | ❌ | ✅ | ✅ |
| Modifier **son** rapport | ❌ | ✅ | ✅ |
| Supprimer **son** rapport | ❌ | ✅ | ✅ |
| Modifier son profil | ❌ | ✅ | ✅ |
| Supprimer son compte | ❌ | ✅ | ✅ |
| Gérer tous les utilisateurs | ❌ | ❌ | ✅ |
| Modérer tout le contenu | ❌ | ❌ | ✅ |

## Données manipulées

### Entité 1 — Utilisateur (`user`)

| Champ | Type | Contrainte |
|---|---|---|
| id | INTEGER | PK |
| nom | VARCHAR(100) | NOT NULL |
| email | VARCHAR(150) | UNIQUE, NOT NULL |
| mdp_hash | VARCHAR(255) | NOT NULL (bcrypt) |
| niveau | ENUM | débutant / intermédiaire / expert |
| localisation | VARCHAR(100) | optionnel |
| is_admin | BOOLEAN | défaut : false |
| date_inscription | DATETIME | défaut : maintenant |

### Entité 2 — Sentier (`sentier`) — Référentiel des itinéraires

| Champ | Type | Contrainte |
|---|---|---|
| id | INTEGER | PK |
| nom | VARCHAR(150) | NOT NULL |
| region | VARCHAR(100) | NOT NULL |
| distance_km | REAL | > 0 |
| denivele_pos | INTEGER | >= 0 |
| difficulte | ENUM | facile / moyen / difficile / expert |
| types_pratique | TEXT | trail, vtt, rando, ski_rando (multi-valeur) |
| terrain | VARCHAR(100) | ex. montagne, forêt, côtier |
| saison_recommandee | VARCHAR(100) | ex. mai–octobre |
| description | TEXT | optionnel |
| user_id | INTEGER | FK → user.id |
| date_ajout | DATETIME | défaut : maintenant |

### Entité 3 — Rapport de conditions (`rapport`) — Entité métier principale

| Champ | Type | Contrainte |
|---|---|---|
| id | INTEGER | PK |
| user_id | INTEGER | FK → user.id |
| sentier_id | INTEGER | FK → sentier.id |
| date_rapport | DATETIME | défaut : maintenant |
| date_expiration | DATETIME | date_rapport + 7 jours |
| statut | ENUM | praticable / partiel / ferme |
| type_pratique | ENUM | trail / vtt / rando / ski_rando |
| obstacles | TEXT | valeurs séparées par virgule |
| commentaire | TEXT | optionnel |

Valeurs d'obstacles : `neige`, `verglas`, `boue`, `crue`, `arbre_tombe`, `travaux`, `secheresse`, `sentier_degrade`

### Relations

```
user (1) ──────< sentier (N)   un utilisateur peut créer plusieurs sentiers
user (1) ──────< rapport (N)   un utilisateur peut déposer plusieurs rapports
sentier (1) ───< rapport (N)   un sentier peut avoir plusieurs rapports actifs
```

### Données évitées (sobriété)

- Pas de photo (poids des médias)
- Pas de tracé GPS (stockage et traitement lourds)
- Pas de coordonnées GPS précises (région suffit)
- Pas d'historique illimité (expiration à 7 jours = base propre)
- Pas de notifications push (infrastructure lourde)
