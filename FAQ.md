# Foire Aux Questions

Cette page répertorie les questions fréquemment rencontrées au sujet de l'environnement technique d'OpenFisca.

> Sous Windows, il est supposé que vous disposez d'un terminal bash (i.e [GitBash](https://gitforwindows.org) ou assimilé).

## GIT

| ERREUR        | CONTEXTE      | SOLUTION  |
| ------------- | ------------- | --------- |
| `could not read from remote repository github` | Vous tentez de pousser votre travail en local sur le serveur avec `git push` | * S’assurer de l’existence d’une clef SSH avec `ls ~/.ssh/` </br>Attendu : une clef publique que nous nommerons `fichier_ssh.pub` et sa clef privée associée `fichier_ssh`. </br>* Le contenu de fichier_ssh.pub doit être référencé dans les settings du compte GitHub de l’usager. </br>* Ajouter la clef privée SSH à votre ssh-agent avec `ssh-add ~/.ssh/fichier_ssh` </br>Pour en savoir plus, voir l'[aide GitHub/SSH](https://help.github.com/articles/connecting-to-github-with-ssh/). |
| `could not open a connection to your authentication agent` | Pour vous identifier auprès d'un service tel que GitHub, vous tentez d'exporter votre clef SSH en l'ajoutant au cache de votre agent SSH avec `ssh-add ~/.ssh/fichier_ssh` | * S’assurer de l’exécution du ssh agent avec `eval $(ssh-agent)` </br></br>Et/OU </br></br>* S’assurer que l’adresse du dépôt n'est pas en HTTPS car elle doit être en SSH : `git remote -v`. </br>Le résultat attendu pour le dépôt tutorial est : </br>`origin	git@github.com:openfisca/tutorial.git (fetch)` </br>`origin	git@github.com:openfisca/tutorial.git (push)` </br>Pour en savoir plus, voir l'[aide GitHub](https://help.github.com/articles/changing-a-remote-s-url/#switching-remote-urls-from-ssh-to-https). |

## Python OpenFisca

| ERREUR        | CONTEXTE      | SOLUTION  |
| ------------- | ------------- | --------- |
| `ImportError: No module named openfisca_france` | Vous tentez d'exécuter un fichier python tel que `framework.py` de ce dépôt tutorial avec `python framework.py` </br>Cela alors que l'environnement fait bien référence à OpenFisca-France lorsque vous le vérifiez avec `pip list`. | Création d’un nouvel espace virtuel </br>et `pip install openfisca-france` |
| Vous n'appelez pas la version souhaitée de l'interprète Python | Vous avez installé la version de python que vous souhaitez utiliser mais dans votre environnement virtuel `python --version` indique une autre version. | Sortez de votre environnement virtuel (`exit`) et redémarrez le en indiquant la version de python souhaitée. Exemple pour la version 2.7 : `pew workon nom_de_l_environnement --python=python27` |
