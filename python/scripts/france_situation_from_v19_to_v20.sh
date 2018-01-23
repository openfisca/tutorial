#!/bin/bash

# Given a json situation on input, updates some enums from openfisca-france v19 to v20.

## INPUT
JSON_SITUATION="$1"

## ACTIONS

gsed -i 's/Gir 5/gir_5/g' $JSON_SITUATION
gsed -i 's/Gir 6/gir_6/g' $JSON_SITUATION

#"aah_non_calculable":{"2018-01": de "" à "calculable"}
#"rsa_non_calculable":{"2018-01": de "" à "calculable"}
#KO
#SRC="\"2018-01\": \"\""
#DEST="\"2018-01\": \"calculable\""
#gsed -i 's/$SRC/$DEST/g' $JSON_SITUATION

gsed -i 's/Célibataire/celibataire/g' $JSON_SITUATION
gsed -i 's/Marié/marie/g' $JSON_SITUATION

gsed -i 's/Retraité/retraite/g' $JSON_SITUATION

gsed -i "s/Locataire ou sous-locataire d'un logement loué vide non-HLM/locataire_vide/g" $JSON_SITUATION
gsed -i "s/Propriétaire (non accédant) du logement/proprietaire/g" $JSON_SITUATION
