# -*- coding: utf-8 -*-

from pprint import pprint
import matplotlib.pyplot as plt  # For graphics
# %matplotlib inline

from openfisca_core.simulations import Simulation
from framework import calculs, situations, al_reforms

def draw():
    i=0
    for (name, situation) in situations.iteritems():
        figure = plt.figure(figsize=(12, 8))

        # for reform in al_reforms:
        reform = al_reforms[0]
        simulation_actuelle = Simulation(tax_benefit_system=reform['legislation'], simulation_json=situation)
            
        for calcul, periods in calculs.iteritems():
            x_axis = []
            x_axis_labels = []
            y_axis = []
            for period in periods:
                if period not in x_axis:
                    x_axis_labels.append(period)
                    x_axis.append(len(x_axis_labels))  # 1, 2, 3, ...

                data = simulation_actuelle.calculate(calcul, period)
                y_axis.append(data[0])

            print "x_axis"
            print len(x_axis)
            print x_axis
            print x_axis_labels


            print "y_axis"
            print len(y_axis)
            print y_axis

        
            plt.plot(x_axis, y_axis, label=reform['name'] + '.' + calcul)

        plt.xticks(x_axis, x_axis_labels)
        plt.xlabel(u'periods')
        plt.legend()
        plt.show(block=True)
        figure.savefig('figure_' + str(i))
        i += 1

draw()
