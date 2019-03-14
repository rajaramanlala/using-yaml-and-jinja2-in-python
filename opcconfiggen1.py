# /usr/bin/python

import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import time

config_data = yaml.load(open('./opcbgp_data.yml'))
env = Environment(loader = FileSystemLoader('/Users/rajaraman'), trim_blocks=True, lstrip_blocks=True)
template = env.get_template('opcbgptemplates.txt')
sys.stdout=open("corebgpconfig.txt","w")
print(template.render(config_data))
sys.stdout.close()


