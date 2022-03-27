---------------------------------------------------------------------
# English

# Openclassrooms Project 9
Develop a web application using Django

## LITReview

Main features :
- Create, answer book reviews
- Follow users

## Installation

Python (version 3.8.10)
* [Download Python](https://www.python.org/downloads/) 

Download the application
```
git clone https://github.com/Mathieusc/openclassrooms_project_9.git
```

Create a virutal environment
```
python -m venv .env
```

Linux :
```
source .env/bin/activate
```

Windows :
```
.\env\Scripts\Activate
```

Install dependecies
```
pip install -r requirements.txt
```

Create the database
```
python manage.py migrate
```

Create the admin account
```
python manage.py createsuperuser
```

or Use the existing admin account
```
username : mathieu
password : oc-admin
```



## Using the application

Log-in locally with a web brower
```
localhost:8000
```
## Authentification

- Create a user account
- Log-in with an existing account


## Homepage

- Create a ticket for a book
- Create a review for a book
- Answer to a ticket
- Display posts from the followed users

## Posts

- Modify / Delete the user's posts

## Subscribers

- Follow a user by writing its name
- Unfollow a user
- Display who the user is following
- Display the followers


## Created with

Python version 3.8.10
* [Visual Studio Code](https://code.visualstudio.com/) 


---------------------------------------------------------------------
# Français

# Openclassrooms Projet 9
Développez une application Web en utilisant Django

## LITReview

Application web permettant de :
- Créer et/ou de répondre à des critiques de livres
- Suivre des utilisateurs

## Installation

Python (version 3.8.10)
* [Télécharger Python](https://www.python.org/downloads/) 

Télécharger l'application
```
git clone https://github.com/Mathieusc/openclassrooms_project_9.git
```

Créer un environnement virtuel :
```
python -m venv .env
```

Linux :
```
source .env/bin/activate
```

Windows :
```
.\env\Scripts\Activate
```

Installer les dépendances
```
pip install -r requirements.txt
```

Créer la base de données
```
python manage.py migrate
```

Créer le compte admin
```
python manage.py createsuperuser
```

Ou utiliser le compte admin existant
```
nom d'utilisateur : mathieu
mpt de passe : oc-admin
```


## Utilisation de l'application

Se connecter en local
```
localhost:8000
```
## Authentification

- Créer un compte utilisateur
- S'inscrire sur un compte existant


## Page d'accueil

- Créer une demande de critique (ticket)
- Créer une critique de livre (review)
- Répondre à une critique
- Liste des posts des utilisateurs suivis

## Posts

- Modifier/Supprimer ses posts

## Abonnements

- Suivre un utilisateur
- Cesser de suivre un utilisateur
- Liste des utilisateurs qui nous suivent


## Créer avec

Python version 3.8.10
* [Visual Studio Code](https://code.visualstudio.com/) 
