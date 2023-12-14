# Phoenix_project
Projet d'implementation de cas d'usage en intelligence artificielle, ce projet a pour but de proposer une playlist de chansons a l'utilisateur en fonction de son état mental afin d'ameliorer son humeur et d'impacter positivement certain, troubles mentaux comme: la dépression, l'anxiété ...etc.
Ce projet se présente sous forme d'application web développé à l'aide du framework django pour la UI, nous avons utilisé un modèle d'arbre de décision de la bibliothéque sklearn afin de proposer une liste de chansons à l'utilisateur

## To test the app

1. Create a fork repo then you can clone your fork on your machine with:
```
git clone git@github.com:'yourfork-repo'/Phoenix_project.git
```
2. enter into the project
```
cd Phoenix_project
```
3. Install and activate your virtual environment
```
python3 -m venv env

source env/bin/activate  # For Unix ou MacOS
env\Scripts\activate     # For Windows
```
4. Install the libraries needed to run the application
```
pip install -r requirements.txt
``` 
5. start the local server to run the app
```
cd merchex
python manage.py runserver
```

## To contribute
1. Create a fork repo then you can clone your fork on your machine with:
```
git clone git@github.com:'yourfork-repo'/Phoenix_project.git
```
2. Then add another Git repository as a remote repository to keep your fork synchronized with the original repository with:
```
cd Phoenix_project
git remote add upstream git@github.com:arezki4/Phoenix_project.git
```
3. To retrieve changes from the remote repository, use:
```
git fetch upstream
```
4. then you can create a branch in your fork repo
```
git branch nom_de_la_branche
git checkout nom_de_la_branche
```
5. Switch your working copy to the "master" branch of the remote "upstream" repository after you push a merged code 
```
git checkout upstream/Master
```
6. To update your repo from the remote repo
```
git fetch upstream
git merge upstream/Master
```
