# Phoenix_project
Projet d'implementation de cas d'usage en intelligence artificielle, ce projet a pour but de proposer une playlist de chansons a l'utilisateur en fonction de son état mental afin d'ameliorer son humeur et d'impacter positivement certain, troubles mentaux comme: la dépression, l'anxiété ...etc.
Ce projet se présente sous forme d'application web développé à l'aide du framework django pour la UI, nous avons utilisé un modèle d'arbre de décision de la bibliothéque sklearn afin de proposer une liste de chansons à l'utilisateur

## To test the app

1. install django on your machine with
```
pip install django
``` 
2. Create a fork repo then you can clone your fork on your machine with:
```
git clone git@github.com:'yourfork-repo'/Phoenix_project.git
```
3. enter into the project
```
cd Phoenix_project/merchex
```
4. start the local server to run the app
```
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
4. Switch your working copy to the "master" branch of the remote "upstream" repository
```
git checkout upstream/Master
```
5. then you can create a branch in your fork repo
