# -*- coding: utf-8 -*-

from pprint import pprint
import matplotlib.pyplot as plt  # For graphics
# %matplotlib inline

from openfisca_core.simulations import Simulation
from framework import calculs, situations, al_reforms

figure = plt.figure(figsize=(12, 8))
for (name, situation) in situations.iteritems():
        results = {'Situation': name}
        line = {}

        for reform in al_reforms:
            results['Reform'] = reform['name']
            simulation_actuelle = Simulation(tax_benefit_system=reform['legislation'], simulation_json=situation)

            for calcul, periods in calculs.iteritems():
                results['Variable'] = calcul
                for period in periods:
                    results['Period'] = period
                    data = simulation_actuelle.calculate(calcul, period)
                    results['Value'] = data[0]
                    line[period] = data[0]

                plt.plot(calculs, line, label=reform['name'] + '.' + calcul)    

plt.xlabel(u'test')
plt.legend()
# plt.show(block=True)
figure.savefig('figure')
