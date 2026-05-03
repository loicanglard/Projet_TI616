# TrailMémoire — Choix technologiques justifiés

## Tableau récapitulatif

| Composant | Technologie choisie | Alternatives écartées | Justification Green IT |
|---|---|---|---|
| **Back-end** | Python Flask 3.1 | Django, FastAPI, Node.js/Express | Micro-framework : seules les briques nécessaires sont importées. Aucun ORM lourd, pas de panneau d'administration généré automatiquement. |
| **Base de données** | SQLite 3 | PostgreSQL, MySQL, MongoDB | Fichier unique embarqué, zéro serveur séparé, zéro connexion réseau additionnelle. Parfaitement adapté au volume d'un projet étudiant. |
| **Moteur de templates** | Jinja2 (inclus Flask) | React, Vue.js, Angular | Rendu HTML côté serveur : le navigateur reçoit directement du HTML statique, sans moteur JS à télécharger et exécuter. Zéro JavaScript framework. |
| **Front-end CSS** | CSS natif (variables, flexbox, grid) | Tailwind CSS, Bootstrap, Bulma | Aucune dépendance externe. Feuille de style < 10 Ko. Polices système (`system-ui`) : 0 requête Google Fonts. |
| **Front-end JS** | Vanilla JS minimal (< 30 lignes) | Alpine.js, jQuery, HTMX | Un seul fichier, un seul rôle : confirmer les suppressions. Pas de framework JS chargé. |
| **Authentification** | Flask-Login + sessions côté serveur | JWT, OAuth2 | Sessions HTTP standards, pas de token JWT à gérer côté client, pas d'appel API tiers. |
| **Hashage des mots de passe** | bcrypt (bibliothèque `bcrypt`) | MD5, SHA-256, argon2 | Standard industriel, résistant aux attaques bruteforce. Bcrypt est recommandé par OWASP. |
| **Formulaires** | Flask-WTF (WTForms) | Validation manuelle | Protection CSRF intégrée, validation centralisée côté serveur, peu de code à écrire. |
| **Déploiement** | Render.com (plan gratuit) | Vercel, Heroku, Railway, VPS | Supporte Python natif, SQLite en lecture/écriture, CI/CD depuis GitHub, hébergement sobre. |
| **Versionnement** | Git + GitHub | GitLab, Bitbucket | Standard de l'industrie, intégration native avec Render pour le déploiement automatique. |
| **Lint / CI** | GitHub Actions + flake8 | Aucun outil | Vérification automatique de la qualité du code à chaque push sur main. |

## Dépendances totales (production)

```
flask==3.1.0          # framework web
flask-login==0.6.3    # gestion de session utilisateur
flask-wtf==1.2.2      # formulaires + protection CSRF
bcrypt==4.2.1         # hashage des mots de passe
```

**Total : 4 packages** — chacun justifié et indispensable.

Aucun ORM (SQLAlchemy, Tortoise), aucun gestionnaire de migrations (Alembic),
aucun framework CSS externe, aucune bibliothèque d'envoi d'e-mails.

## Pourquoi pas Django ?

Django est un excellent framework, mais il embarque un ORM complet, un panel
d'administration, un système d'authentification étendu et de nombreuses
fonctionnalités non utilisées dans ce projet. Pour TrailMémoire, Django serait
surdimensionné : davantage de code chargé, davantage de dépendances transitives,
une surface d'attaque plus large.

Flask permet de n'activer que ce dont on a besoin.

## Pourquoi SQLite et non PostgreSQL ?

PostgreSQL est préférable pour un service en production avec plusieurs dizaines
d'utilisateurs simultanés. Pour ce projet étudiant, le trafic sera très faible
(quelques dizaines d'utilisateurs au maximum). SQLite élimine :
- un serveur de base de données à maintenir
- une variable d'environnement `DATABASE_URL` complexe
- un coût de connexion réseau à chaque requête

La migration vers PostgreSQL serait triviale si nécessaire (même syntaxe SQL,
changement du driver uniquement).

## Pourquoi le rendu serveur (Jinja2) et non une SPA ?

Une SPA (Single Page Application avec React ou Vue) nécessiterait :
- le téléchargement d'un bundle JS (souvent > 100 Ko compressé)
- un moteur JavaScript exécuté dans le navigateur
- une API REST séparée (doublement du code)
- une gestion d'état côté client

Jinja2 renvoie du HTML pur. Le navigateur l'affiche directement, sans
interprétation supplémentaire. C'est plus rapide, plus sobre, plus accessible
(le contenu est présent sans JS activé).
