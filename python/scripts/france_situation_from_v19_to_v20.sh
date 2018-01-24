#!/bin/bash

# Update an OpenFisca situation in JSON format:
# updates some enumerations from openfisca-france v19 to v20.

if [ -z "$1" ]
then
    echo "[USAGE] sh france_situation_from_v19_to_v20.sh file.json"
    echo "        Where 'file.json' is an OpenFisca situation in JSON format."
else
    # INPUT

    JSON_SITUATION="$1"

    # ACTIONS

    gsed -i 's/Gir 5/gir_5/g' $JSON_SITUATION
    gsed -i 's/Gir 6/gir_6/g' $JSON_SITUATION

    gsed -i 's/Célibataire/celibataire/g' $JSON_SITUATION
    gsed -i 's/Marié/marie/g' $JSON_SITUATION

    gsed -i 's/Retraité/retraite/g' $JSON_SITUATION

    gsed -i "s/Locataire ou sous-locataire d'un logement loué vide non-HLM/locataire_vide/g" $JSON_SITUATION
    gsed -i "s/Propriétaire (non accédant) du logement/proprietaire/g" $JSON_SITUATION
fi
