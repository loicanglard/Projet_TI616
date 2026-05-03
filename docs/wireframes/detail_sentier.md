# Wireframe — Détail d'un sentier (`/sentiers/<id>`)

```
┌─────────────────────────────────────────────────────────────┐
│ NAV  T.R.A.I.L            Sentiers  Mon profil  Déconnexion │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ← Retour à la liste                                        │
│                                                             │
│  GR20 — Étape 1 : Calenzana → Ortu di u Piobbu             │
│  Ajouté par @marc le 12/03/2025                             │
│  Pratiques : [TRAIL] [RANDO]                                │
│                                                             │
│  CARACTÉRISTIQUES                                           │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Région     : Corse                                  │   │
│  │  Distance   : 16 km · D+ 1 200 m                     │   │
│  │  Difficulté : [Difficile]                            │   │
│  │  Terrain    : Montagne, rochers, forêt               │   │
│  │  Saison     : Juin à octobre                         │   │
│  └──────────────────────────────────────────────────────┘   │
│  Voir sur OpenStreetMap →                                   │
│                                                             │
│  [Modifier ce sentier]  [Supprimer ce sentier]  ← si proprio│
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ÉTAT ACTUEL — 3 rapports actifs          [+ Déposer]       │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  ✓ PRATICABLE  [TRAIL]            il y a 3 heures    │   │
│  │  @alice — Obstacles : aucun                          │   │
│  │  "Conditions parfaites, sentier sec et bien balisé." │   │
│  │                              [Modifier] [Supprimer]  │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  ⚠ PARTIEL     [TRAIL]            il y a 2 jours     │   │
│  │  @bob — Obstacles : neige, boue                      │   │
│  │  "Neige résiduelle au-dessus de 1500m."              │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  ✓ PRATICABLE  [RANDO]            il y a 4 jours     │   │
│  │  @marc — Obstacles : aucun                           │   │
│  │  "RAS pour la randonnée, chemin bien dégagé."        │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ─ ─ ─ Rapports expirés non affichés ─ ─ ─                 │
│                                                             │
│  [← Préc]  Page 1/1                                         │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                      │
└─────────────────────────────────────────────────────────────┘
```

## Notes de conception

- **Statuts en couleur** : praticable=vert, partiel=orange, fermé=rouge — immédiatement lisible
- **Lien OpenStreetMap** : `<a>` externe simple, 0 ressource chargée
- **Badges type pratique** sur chaque rapport : permet de voir que trail ≠ rando sur le même sentier
- **Rapports expirés** : jamais affichés, mention discrète "rapports expirés non affichés" pour transparence
- **Bouton "+ Déposer"** : visible si connecté ; sinon texte "Connectez-vous pour déposer un rapport"
- **Modifier/Supprimer** : visibles uniquement pour le propriétaire du rapport (contrôle serveur + template)
- Confirmation JavaScript native `confirm()` avant suppression
