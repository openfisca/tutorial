from periods import years

rupture_2017 = {
    'familles': {
        'f1': {
            'parents': ['Faustine']
        }
    },
    'foyers_fiscaux': {
        'ff1': {
            'declarants': ['Faustine']
        }
    },
    'individus': {
        'Faustine': {
            'salaire_imposable': {
                '2015': 12 * 1800,
                '2016': 12 * 1800,
                '2017': 12 * 1000,
                '2018': 12 * 1000,
                '2019': 12 * 1000
            }
        }
    },
    'menages': {
        'm1': {
            'personne_de_reference': ['Faustine'],
            'loyer': {
                '2015': 12 * 500,
                '2016': 12 * 500,
                '2017': 12 * 500,
                '2018': 12 * 500,
                '2019': 12 * 500
            },
            'statut_occupation_logement': {
                '2015': 'locataire_vide',
                '2016': 'locataire_vide',
                '2017': 'locataire_vide',
                '2018': 'locataire_vide',
                '2019': 'locataire_vide'
            }
        }
    }
}

hausse_2017 = {
    'familles': {
        'f1': {
            'parents': ['Dominique']
        }
    },
    'foyers_fiscaux': {
        'ff1': {
            'declarants': ['Dominique']
        }
    },
    'individus': {
        'Dominique': {
            'salaire_imposable': {
                '2015': 12 * 1000,
                '2016': 12 * 1000,
                '2017': 12 * 1800,
                '2018': 12 * 1800,
                '2019': 12 * 1800
            }
        }
    },
    'menages': {
        'm1': {
            'personne_de_reference': ['Dominique'],
            'loyer': {
                '2015': 12 * 500,
                '2016': 12 * 500,
                '2017': 12 * 500,
                '2018': 12 * 500,
                '2019': 12 * 500
            },
            'statut_occupation_logement': {
                '2015': 'locataire_vide',
                '2016': 'locataire_vide',
                '2017': 'locataire_vide',
                '2018': 'locataire_vide',
                '2019': 'locataire_vide'
            }
        }
    }
}

salaire_fluctuant_mensuel = {
    '01': 800,
    '02': 500,
    '03': 300,
    '04': 700,
    '05': 1500,
    '06': 1200,
    '07': 800,
    '08': 500,
    '09': 300,
    '10': 700,
    '11': 1500,
    '12': 1200,
}

salaire_fluctuant = { year + '-' + monthKey : value for monthKey, value in salaire_fluctuant_mensuel.iteritems() for year in years }

fluctuant_2017 = {
    'familles': {
        'f1': {
            'parents': ['Raoul']
        }
    },
    'foyers_fiscaux': {
        'ff1': {
            'declarants': ['Raoul']
        }
    },
    'individus': {
        'Raoul': {
            'salaire_imposable': salaire_fluctuant
        }
    },
    'menages': {
        'm1': {
            'personne_de_reference': ['Raoul'],
            'loyer': {
                '2015': 12 * 500,
                '2016': 12 * 500,
                '2017': 12 * 500,
                '2018': 12 * 500,
                '2019': 12 * 500
            },
            'statut_occupation_logement': {
                '2015': 'locataire_vide',
                '2016': 'locataire_vide',
                '2017': 'locataire_vide',
                '2018': 'locataire_vide',
                '2019': 'locataire_vide'
            }
        }
    }
}

situations = {
    'rupture_2017': rupture_2017,
    'fluctuant_2017': fluctuant_2017,
    'hausse_2017': hausse_2017
}
