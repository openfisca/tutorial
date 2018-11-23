# Tutorial Notebooks

## How to use the notebooks

In your console, run:

```
make install
```

And have fun.

## How to test the notebooks

In your console, run:

```
make test
```

If all goes according to plan, you should see a nice `OK. No error detected in tested notebook(s).` 😃

Otherwise, you'll receive really handy feedback telling you where it doesn't work, and why:

```
---------------------------------------------------------------------------
<ipython-input-2-6c6f6a2075ab> in <module>()
----> 1 simulation.calculate('af', '2015')

/Users/hyperion/.pyenv/versions/tutoriel/lib/python2.7/site-packages/openfisca_core/simulations.pyc in calculate(self, variable_name, period, **parameters)
    153             self.tracer.record_calculation_start(variable.name, period, **parameters)
    154
--> 155         self._check_period_consistency(period, variable)
    156
    157         extra_params = parameters.get('extra_params', ())

/Users/hyperion/.pyenv/versions/tutoriel/lib/python2.7/site-packages/openfisca_core/simulations.pyc in _check_period_consistency(self, period, variable)
    288                 variable.name,
    289                 period
--> 290                 ).encode('utf-8'))
    291
    292         if variable.definition_period == periods.YEAR and period.unit != periods.YEAR:

ValueError: Unable to compute variable 'af' for period 2015: 'af' must be computed for a whole month. You can use the ADD option to sum 'af' over the requested period, or change the requested period to 'period.first_month'.
```
