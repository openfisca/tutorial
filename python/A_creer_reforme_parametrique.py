# -*- coding: utf-8 -*-

import openfisca_france
from reforme_parametrique import MaReform

####### Consulter la situation actuelle ##############
legislation_france = openfisca_france.FranceTaxBenefitSystem()

resultat_actuel = legislation_france.parameters.impot_revenu.bareme[1].rate

print "Résultat actuel"
print resultat_actuel

####### Consulter la situation avec la reforme ##############
legislation_reforme = MaReform(legislation_france)

resultat_apres_reforme = legislation_reforme.parameters.impot_revenu.bareme[1].rate

print "Resultat après reforme"
print resultat_apres_reforme
