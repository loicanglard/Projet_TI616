# Wireframe — Page d'accueil (`/`)

```
┌─────────────────────────────────────────────────────────────┐
│ NAV                                                          │
│ T.R.A.I.L                 Sentiers  Connexion  [S'inscrire] │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  HERO                                                       │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                                                       │  │
│  │  Ce sentier est-il praticable aujourd'hui ?           │  │
│  │                                                       │  │
│  │  Consultez et partagez l'état réel des sentiers       │  │
│  │  trail, VTT et randonnée.                             │  │
│  │  Rapports communautaires — valides 7 jours.           │  │
│  │                                                       │  │
│  │  [ Consulter les sentiers ]  [ Déposer un rapport ]   │  │
│  │                                                       │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  SECTION — Signalements récents                             │
│                                                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  ✓ PRATICABLE  [TRAIL]              il y a 3 heures   │  │
│  │  GR20 — Étape 1                                       │  │
│  │  Corse — signalé par @alice                           │  │
│  │  "Conditions parfaites, sentier sec."                 │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │  ⚠ PARTIEL     [VTT]               il y a 1 jour     │  │
│  │  Belledonne — Crête Nord                              │  │
│  │  Isère — signalé par @bob                             │  │
│  │  "Neige dès 1400m, glissant."                        │  │
│  ├───────────────────────────────────────────────────────┤  │
│  │  ✗ FERMÉ       [RANDO]             il y a 2 jours    │  │
│  │  Calanques — Morgiou                                  │  │
│  │  PACA — signalé par @marc                             │  │
│  │  "Arrêté préfectoral — risque incendie."             │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
│  → Voir tous les sentiers                                   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  ENCART GREEN IT                                            │
│  Site Green IT — Pages < 200 Ko · 0 tracker                 │
│  Rapports expirés auto après 7 jours · EcoIndex : A         │
├─────────────────────────────────────────────────────────────┤
│ FOOTER                                                      │
│  T.R.A.I.L — Terrain Rando Alerte Info Live                 │
│  EFREI TI616 2025-2026 | Code source GitHub                 │
└─────────────────────────────────────────────────────────────┘
```

## Code couleur des statuts

| Statut | Couleur | Icône |
|---|---|---|
| Praticable | Vert `#d8f3dc` / `#1b4332` | ✓ |
| Partiel | Orange `#fff3cd` / `#6d4c00` | ⚠ |
| Fermé | Rouge `#fde8e0` / `#7b1d0e` | ✗ |

## Notes de conception

- **Hero** : texte uniquement, aucune image — poids zéro
- Le bouton "Déposer un rapport" redirige vers /auth/connexion si non connecté
- Les signalements sont limités aux **rapports non expirés** (`date_expiration > now`)
- Affichage de l'**ancienneté relative** ("il y a 3h", "il y a 1 jour") — calculé côté serveur
- Aucune animation, aucun carousel, aucune image
