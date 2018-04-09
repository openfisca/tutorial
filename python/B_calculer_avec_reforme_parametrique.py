# -*- coding: utf-8 -*-

import openfisca_france
from openfisca_core.simulations import Simulation
from reforme_parametrique import MaReform



####### Décrivez les entités ###########
situation = {
  "familles": {
    "famille_1": {
      "enfants": [
        "Janet"
      ],
      "parents": [
        "Alex",
        "Sam"
      ]
    }
  },
  "foyers_fiscaux": {
    "foyer_fiscal_1": {
      "declarants": [
        "Alex",
        "Sam"
      ],
      "personnes_a_charge": [
        "Janet"
      ]
    }
  },
  "individus": {
    "Alex": {
      "salaire_de_base": {
        "2017": 20000
      }
    },
    "Sam": {
      "salaire_de_base": {
        "2017": 30000
      }
    },
    "Janet": {}
  },
  "menages": {
    "menage_1": {
      "conjoint": [
        "Sam"
      ],
      "enfants": [
        "Janet"
      ],

      "personne_de_reference": [
        "Alex"
      ]
    }
  }
}

####### Calcule la situation actuelle de la legislation française ##############
legislation_france = openfisca_france.FranceTaxBenefitSystem()
simulation_actuelle = Simulation(tax_benefit_system=legislation_france, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'impots_directs')
# ainsi que la periode sur laquelle vous souaitez la calculer (ex : '2017')
resultat_actuel = simulation_actuelle.calculate('impots_directs', '2017')

print "Résultat actuel"
print resultat_actuel

####### Calcule la situation avec la réforme ##############
legislation_reforme = MaReform(legislation_france)
simulation_reforme = Simulation(tax_benefit_system=legislation_reforme, simulation_json=situation)

# Insérez ci-dessous la variable que vous souhaitez calculer (ex : 'impots_directs')
# ainsi que la periode sur laquelle vous souaitez la calculer (ex : '2017')
resultat_reforme = simulation_reforme.calculate('impots_directs', '2017')

print "Resultat après reforme"
print resultat_reforme
