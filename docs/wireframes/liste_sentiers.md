# Wireframe — Liste des sentiers (`/sentiers/`)

```
┌─────────────────────────────────────────────────────────────┐
│ NAV  TrailMémoire         Sentiers  Mon profil  Déconnexion │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Sentiers trail                          [+ Ajouter]        │
│                                                             │
│  FILTRES                                                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │ Région : [____________▼]  Difficulté : [____________▼] │ │
│  │                                          [Filtrer]     │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  42 sentiers trouvés                                        │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  GR20 — Étape 1 : Calenzana → Ortu di u Piobbu       │   │
│  │  Corse · 16 km · D+ 1 200 m · [Difficile]           │   │
│  │  Terrain : montagne — Saison : juin–oct.             │   │
│  │  Ajouté par @marc · 3 sorties enregistrées           │   │
│  │                                          [Voir →]    │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  Belledonne — Crête Nord                             │   │
│  │  Isère · 22 km · D+ 1 800 m · [Expert]              │   │
│  │  Terrain : montagne — Saison : juil.–sept.           │   │
│  │  Ajouté par @alice · 7 sorties enregistrées          │   │
│  │                                          [Voir →]    │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │  ...                                                 │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  PAGINATION                                                 │
│  [← Préc]  [1]  [2]  [3]  ...  [Suiv →]                   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                      │
└─────────────────────────────────────────────────────────────┘
```

## Notes de conception

- **Filtres** : formulaire GET simple, pas de JavaScript requis
- **Bouton "+ Ajouter"** : visible uniquement si l'utilisateur est connecté
- **Liste** : vue tableau sobre, pas de cartes avec ombres ni images
- Chaque ligne affiche le nombre de sorties → indicateur de popularité communautaire
- **Pagination** : liens `?page=N` purs, pas de scroll infini
- 20 résultats par page maximum
