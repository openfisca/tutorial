# -*- coding: utf-8 -*-

import json
import sys

from pprint import pprint

extension_specifics = {
    'openfisca-brestmetropole': {
        'individus': [ 'brest_metropole_transport' ],
    },
    'openfisca-paris': {
        'familles': [
            'parisien',
            'paris_complement_sante',
            'paris_energie_famille',
            'paris_logement_plfm',
            'paris_logement_aspeh',
            'paris_logement',
            'paris_logement_psol',
            'paris_forfait_famille',
            'paris_logement_familles',
        ],
    },
    'openfisca-rennesmetropole': {
        'individus': [ 'rennes_metropole_transport' ],
    },
}

def read(situationPath):
    with open(situationPath) as json_data:
        json_str = json_data.read()
        return json.loads(json_str)

def normalize(situation):
    if '_id' in situation:
        del situation['_id']
    for extension in extension_specifics:
        extension_specific = extension_specifics[extension]

        for entityKey in extension_specific:
            entities = situation[entityKey]
            props = extension_specific[entityKey]

            for instanceKey in entities:
                entity = entities[instanceKey]

                for prop in props:
                    if prop in entity:
                        del entity[prop]

    return situation


def main():
    n = normalize(read('/repos/tutorial/python/exemples/gt_non_recours/celibataire_aah_mes-aides_5a70bfe34b64656dc14d58a5'))
    pprint(n)


if __name__ == '__main__':
    sys.exit(main())
