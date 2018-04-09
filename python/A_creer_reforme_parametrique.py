# -*- coding: utf-8 -*-

# Importez OpenFisca
import openfisca_france
from reforme_parametrique import MaReforme

# Consultez la situation actuelle
legislation_france = openfisca_france.FranceTaxBenefitSystem()

resultat_actuel = legislation_france.parameters.impot_revenu.bareme[1].rate

print "Résultat actuel"
print resultat_actuel

# Consultez la situation avec la reforme
legislation_reforme = MaReforme(legislation_france)

resultat_apres_reforme = legislation_reforme.parameters.impot_revenu.bareme[1].rate

print "Resultat après reforme"
print resultat_apres_reforme
