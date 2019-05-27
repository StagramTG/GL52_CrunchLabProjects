# GL52_CrunchLabProjects
Projet à réaliser dans le cadre de l'UV GL52

**Auteurs** : Romain Huyvaert, Sofiane Tiou, Thomas Gredin et Lucas Demouy

## Installation
- Cloner le dépôt git
- Faire les migrations avec `python manage.py migrate`
- Les deux en parallèle :
    + Lancer le serveur de dev python avec la commande `python manage.py runserver`
    + Lancer le serveur de dev NPM depuis le dossier static/js `npm run serve`

## ToDo
- Gestion des utilisateurs :
    + Données :
        - Informations sur la personne
        - Rôle sur la plateforme
        - Comptes attachés
    + Vues :
        - Page principale de gestion du compte
        - Page de gestion des comptes
        - Page de gestion des projets
        - Page de gestion des informations personnelles
    + **/!\ Mettre en place une API REST pour l'application Vue.js /!\ :**
        - lien utile --> https://www.techiediaries.com/django-vuejs-api-views/
        - Suppléments à installer :
            * Django REST Framework
            * Django Cors Headers (Requête AJAX côté serveur)
            * Vue-Router (Routing côté client)
            * Axios (Requête AJAX côté client)
            * VueX (Store de données côté client)
        - Gestion de l'authentification