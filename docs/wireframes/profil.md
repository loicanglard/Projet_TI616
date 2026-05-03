# Wireframe — Mon profil (`/utilisateurs/profil`)

```
┌─────────────────────────────────────────────────────────────┐
│ NAV  TrailMémoire         Sentiers  Mon profil  Déconnexion │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Mon profil                                                 │
│                                                             │
│  INFORMATIONS                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Nom          : Alice Dupont                         │   │
│  │  E-mail       : alice@exemple.fr                    │   │
│  │  Niveau       : Intermédiaire                        │   │
│  │  Localisation : Grenoble (38)                        │   │
│  │  Membre depuis: 12/01/2025                           │   │
│  └──────────────────────────────────────────────────────┘   │
│  [Modifier mon profil]                                      │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  MES SORTIES  (12 au total)                                 │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  GR20 — Étape 1          14/09/2025  4h12  ★★★★★   │   │
│  │  Belledonne Nord         03/08/2025  5h40  ★★★★☆   │   │
│  │  Calanques — Morgiou     17/07/2025  2h15  ★★★☆☆   │   │
│  │  ...                                                 │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  [← Préc]  Page 1/1  (12 sorties)                          │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  MES SENTIERS AJOUTÉS  (3 au total)                         │
│                                                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  GR20 — Étape 1        Corse      [Voir] [Modifier]  │   │
│  │  Vercors — Grand Veymont  Drôme   [Voir] [Modifier]  │   │
│  │  Chartreuse — Pas de la Clé  Isère [Voir] [Modifier] │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  ZONE DANGER                                                │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  [Supprimer mon compte]                              │   │
│  │  Cette action est irréversible et supprimera toutes  │   │
│  │  vos sorties et sentiers.                            │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                      │
└─────────────────────────────────────────────────────────────┘
```

## Notes de conception

- **Sorties** : liste tabulaire sobre, triée par date décroissante, paginée
- **Sentiers ajoutés** : liste séparée, avec accès rapide à la modification
- **Zone danger** : visuellement distincte (bordure rouge subtile) mais pas agressive
- Le bouton "Supprimer mon compte" déclenche une confirmation JavaScript native
- Pas d'avatar, pas de photo de profil — données textuelles uniquement
