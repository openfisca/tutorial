# -*- coding: utf-8 -*-

from openfisca_france import FranceTaxBenefitSystem


tbs = FranceTaxBenefitSystem()


def display_bareme(age, period):
    scenario_params = {
        "period": period,
        "parent1": {
            "age": age,
        },
        "axes": [
            dict(
                count = 10,
                min = 0,
                max = 50000,
                name = 'salaire_de_base',
            ),
        ],
    }
    scenario = tbs.new_scenario().init_single_entity(**scenario_params)
    simulation = scenario.new_simulation()
    graphs.draw_bareme(
        simulation = simulation,
        x_axis = "salaire_imposable",
        legend_position = 2,
        bbox_to_anchor = (1.05, 1),
    )

interact(
    display_bareme,
    age=widgets.IntSlider(min=0, max=130, step=1, value=30, continuous_update=False),
    period=fixed(periods.period("2015")),
)
# None  # Hide strange output

