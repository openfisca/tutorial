# Foire Aux Questions

Cette page répertorie les questions fréquemment rencontrées au sujet de l'environnement technique d'OpenFisca.  
N'hésitez pas à l'[enrichir](https://github.com/openfisca/tutorial/edit/master/FAQ.md) de vos expériences ! :slightly_smiling_face: 


> Sous Windows, il est supposé que vous disposez d'un terminal bash (i.e [GitBash](https://gitforwindows.org) ou assimilé).


## Python OpenFisca

| QUESTION | CONTEXTE | SOLUTION      |
| -------- | -------- | ------------- |
| Comment faire appel à l'interprète Python lorsque le terminal renvoit `command not found` ? | Vous tentez d'appeler l'interprète du langage Python avec : `python un_fichier.py` | Mettre à jour la variable d'environnement `PATH` : </br>* Vérifier sa valeur avec : </br>`echo $PATH` </br>* Puis, retrouvez le répertoire où la version souhaitée de Python a été installée ; celui-ci varie d'un environnement à l'autre. </br>Exemple Windows : `/c/Python27`. </br>Exemple Unix : `/opt/local/bin/python` </br>* Mettre à jour la variable en indiquant le chemin vers l'interprète python. </br>Exemple Windows : `export PATH=/c/Python27:$PATH`. </br>Exemple Unix : `export PATH=/opt/local/bin:$PATH` </br></br>Afin que cette mise à jour soit permanente, il est conseillé d'ajouter cette commande d'export à la fin de votre fichier de configuration Bash `~/.bashrc`. |
| Comment corriger son environnement lorsqu'on obtient `ImportError: No module named openfisca_france` ? | Vous tentez d'exécuter un fichier python tel que `framework.py` de ce dépôt tutorial avec : </br>`python framework.py` </br></br>Vous obtenez l'`ImportError` alors que l'environnement fait bien référence à OpenFisca-France lorsque vous le vérifiez avec `pip list`. | Sortir de votre environnement virtuel (`exit`). En créer un nouveau avec `pew new nom_de_l_environnement` </br>et démarrer une nouvelle installation d'OpenFisca-France avec `pip install openfisca-france` |
| Comment appeler une version particulière de l'interprète Python dans un environnement virtuel `pew` ? | Vous avez installé la version de python que vous souhaitez utiliser mais dans votre environnement virtuel `python --version` indique une autre version. </br></br>Note : Se référer au [site officiel](https://www.python.org/downloads/) python pour l'ensemble des versions disponibles et leur installation. | Sortir de votre environnement virtuel (`exit`) et le redémarrer en indiquant la version de python souhaitée. Exemple pour la version 2.7 : </br>`pew workon nom_de_l_environnement --python=python27` |


## GIT

| QUESTION | CONTEXTE | SOLUTION      |
| -------- | -------- | ------------- |
| Comment pousser des modifications sur le serveur alors qu'on obtient `could not read from remote repository github` ? | Vous tentez de pousser votre travail en local sur le serveur avec : </br>`git push` | * S’assurer de l’existence d’une clef SSH avec `ls ~/.ssh/` </br>Attendu : une clef publique que nous nommerons `fichier_ssh.pub` et sa clef privée associée `fichier_ssh`. </br>* Le contenu de fichier_ssh.pub doit être référencé dans les settings du compte GitHub de l’usager. </br>* Ajouter la clef privée SSH à votre ssh-agent avec `ssh-add ~/.ssh/fichier_ssh` </br>Pour en savoir plus, voir l'[aide GitHub/SSH](https://help.github.com/articles/connecting-to-github-with-ssh/). |
| Comment s'identifier sur GitHub quand l'ajout d'une clef SSH produit `could not open a connection to your authentication agent` ? | Pour vous identifier auprès d'un service tel que GitHub, vous tentez d'exporter votre clef SSH en l'ajoutant au cache de votre agent SSH avec : </br>`ssh-add ~/.ssh/fichier_ssh` | * S’assurer de l’exécution du ssh-agent avec `eval $(ssh-agent)` </br></br>Et/OU </br></br>* S’assurer que l’adresse du dépôt n'est pas en HTTPS car elle doit être en SSH : `git remote -v`. </br>Le résultat attendu pour le dépôt tutorial est : </br>`origin	git@github.com:openfisca/tutorial.git (fetch)` </br>`origin	git@github.com:openfisca/tutorial.git (push)` </br>Pour en savoir plus, voir l'[aide GitHub](https://help.github.com/articles/changing-a-remote-s-url/#switching-remote-urls-from-ssh-to-https). |
