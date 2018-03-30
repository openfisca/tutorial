# Foire Aux Questions

## GIT

| ERREUR        | CONTEXTE      | SOLUTION  |
| ------------- | ------------- | --------- |
| `could not read from remote repository github` | Commande `git push` | * S’assurer de l’existence d’une clef SSH avec `ls ~/.ssh/` </br>Attendu : fichier_ssh et fichier_ssh.pub </br>* Le contenu de fichier_ssh.pub doit être référencé dans les settings du compte GitHub de l’usager. </br>* Ajouter la clef SSH avec `ssh-add ~/.ssh/fichier_ssh` |
| `could not open a connection to your authentication agent` | Commande `ssh-add ~/.ssh/fichier_ssh` | * S’assurer de l’exécution du ssh agent avec `eval $(ssh-agent)` </br>Et/OU </br>* S’assurer que l’adresse du dépôt est en SSH (pas en https) via `git remote -v`. </br>Le résultat attendu pour le dépôt tutorial est : </br>`origin	git@github.com:openfisca/tutorial.git (fetch)` </br>`origin	git@github.com:openfisca/tutorial.git (push)` |


## Python OpenFisca

| ERREUR        | CONTEXTE      | SOLUTION  |
| ------------- | ------------- | --------- |
| `ImportError: No module named openfisca_france` | Commande `python framework.py` </br>Répertoire tutorial & virtualenv complets. | Création d’un nouvel espace virtuel </br>et `pip install openfisca-france` |
