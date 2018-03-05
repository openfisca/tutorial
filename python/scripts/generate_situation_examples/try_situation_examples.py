# -*- coding: utf-8 -*-

from openfisca_france import CountryTaxBenefitSystem
from openfisca_core.simulations import Simulation
from situation_examples import celibataire

tax_benefit_system = CountryTaxBenefitSystem()
simulation = Simulation(tax_benefit_system = tax_benefit_system, simulation_json = celibataire)

print (simulation.calculate('revenu_disponible', '2016'))
