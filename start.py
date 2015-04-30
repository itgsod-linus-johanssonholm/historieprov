 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml


#pprint(family['bernadotte']['name'])
#pprint(family['bernadotte']['consort']['name'])

#for index in family['bernadotte']['barn']:
#    print index

with open("bernadotte.yaml") as f:
        family = yaml.load(f)


def ett(family):

        for index in family['barn']:
            print ett(index)

print ett(family['bernadotte'])