 # -*- coding: utf-8 -*-
from pprint import pprint
import yaml


#pprint(family['bernadotte']['name'])
#pprint(family['bernadotte']['consort']['name'])

#for index in family['bernadotte']['barn']:
#    print index

with open("bernadotte.yaml") as f:
        family = yaml.load(f)


def ett(p, death=True):

    print p['name']#, p['birth'], p['death']


    if "consort" in p:
        ett(p['consort'], death=death)
    if "mistress" in p:
        ett(p['mistress'], death=death)
    if "barn" in p:
        for b in p['barn']:
            ett(b, death=death)

print ett(p=family['bernadotte'], death=False)