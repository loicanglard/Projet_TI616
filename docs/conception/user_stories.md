# T.R.A.I.L — User Stories

Format : *En tant que [rôle], je veux [objectif], afin de [bénéfice].*

---

## Gestion des utilisateurs

**US-01**
En tant que **visiteur**, je veux **m'inscrire avec un nom, une adresse e-mail et
un mot de passe**, afin de **rejoindre la communauté T.R.A.I.L et pouvoir déposer
des rapports de conditions**.

*Critères d'acceptance :*
- Le formulaire valide le format de l'e-mail côté serveur.
- Le mot de passe est hashé (bcrypt) avant stockage — jamais en clair.
- Un e-mail déjà utilisé retourne un message d'erreur explicite.
- Après inscription réussie, l'utilisateur est redirigé vers la liste des sentiers.

---

**US-02**
En tant que **pratiquant connecté**, je veux **modifier mes informations de profil
(nom, niveau, localisation)**, afin de **maintenir un profil représentatif de
ma pratique actuelle**.

*Critères d'acceptance :*
- Seul l'utilisateur concerné peut modifier son profil.
- Un message de confirmation s'affiche après sauvegarde réussie.

---

**US-03**
En tant que **pratiquant connecté**, je veux **supprimer mon compte**, afin de
**garder le contrôle total sur mes données personnelles**.

*Critères d'acceptance :*
- Une confirmation explicite est demandée avant suppression.
- La suppression efface en cascade tous les rapports et sentiers de l'utilisateur.
- L'utilisateur est déconnecté et redirigé vers l'accueil.

---

**US-04**
En tant qu'**administrateur**, je veux **consulter la liste paginée des utilisateurs
et pouvoir supprimer un compte**, afin de **modérer la communauté**.

*Critères d'acceptance :*
- La page est accessible uniquement aux utilisateurs `is_admin = true`.
- Tout accès non autorisé renvoie un code HTTP 403.
- La liste affiche 20 utilisateurs par page maximum.

---

## Entité métier — Sentiers et Rapports de conditions

**US-05**
En tant que **visiteur**, je veux **consulter la liste des sentiers filtrés par
région, difficulté et type de pratique (trail / VTT / rando)**, afin de **trouver
rapidement un itinéraire adapté à ma pratique et ma région**.

*Critères d'acceptance :*
- La liste est paginée (20 résultats par page).
- Les filtres région, difficulté et type sont cumulables.
- Chaque résultat affiche le statut du dernier rapport actif (couleur verte/orange/rouge).
- Accessible sans connexion.

---

**US-06**
En tant que **pratiquant connecté**, je veux **ajouter un sentier** (nom, région,
distance, dénivelé, types de pratique, terrain, saison, description), afin de
**enrichir la base communautaire avec des itinéraires que je connais**.

*Critères d'acceptance :*
- Tous les champs obligatoires sont validés côté serveur.
- Au moins un type de pratique doit être sélectionné.
- Après création, l'utilisateur est redirigé vers le détail du sentier.

---

**US-07**
En tant que **pratiquant connecté**, je veux **déposer un rapport de conditions
sur un sentier** (statut praticable/partiel/fermé, type de pratique, obstacles
identifiés, commentaire), afin d'**informer la communauté de l'état réel du
terrain avant qu'ils ne s'y engagent**.

*Critères d'acceptance :*
- Le statut est obligatoire (praticable / partiel / fermé).
- Le type de pratique est obligatoire et doit correspondre à un type du sentier.
- La date d'expiration est calculée automatiquement : date_rapport + 7 jours.
- Le rapport apparaît immédiatement sur la fiche du sentier.

---

**US-08**
En tant que **visiteur ou pratiquant connecté**, je veux **consulter tous les
rapports actifs d'un sentier** (non expirés, triés du plus récent au plus ancien),
afin de **prendre une décision éclairée avant ma sortie**.

*Critères d'acceptance :*
- Seuls les rapports dont `date_expiration > maintenant` sont affichés.
- Chaque rapport affiche : statut (coloré), type de pratique, obstacles, commentaire, auteur, ancienneté.
- Accessible sans connexion.

---

## Sobriété numérique

**US-09**
En tant qu'**utilisateur**, je veux que **chaque page se charge en moins de
2 secondes sur connexion mobile 3G**, afin de **pouvoir consulter les conditions
depuis le parking avant une sortie, sans consommer inutilement de données**.

*Critères d'acceptance :*
- Poids total de chaque page < 200 Ko.
- Moins de 10 requêtes HTTP par page.
- Score Lighthouse Performance > 80.
- Aucune police externe chargée.

---

**US-10**
En tant qu'**utilisateur**, je veux **que le site affiche son empreinte carbone
estimée par visite**, afin de **rendre concrets les engagements Green IT du projet
et sensibiliser à l'impact du numérique**.

*Critères d'acceptance :*
- La valeur CO₂/visite (issue de Website Carbon Calculator) est affichée en pied de page.
- La valeur est mise à jour après chaque optimisation significative.
