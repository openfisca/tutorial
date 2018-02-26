
years = [str(y).zfill(2) for y in range(2015, 2020)]
monthIds = [ str(m).zfill(2) for m in range(1,13) ]
allMonths = [y + '-' + m for y in years for m in monthIds]
months2018 = [ '2018-' + m for m in monthIds ]
months2019 = [ '2019-' + m for m in monthIds ]
year17 = '2017'
