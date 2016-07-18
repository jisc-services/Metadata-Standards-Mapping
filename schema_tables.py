from collections import defaultdict, OrderedDict
import json
from pprint import pprint

COL_ORDER = ['rioxx', 'openaire', 'casrai', 'hefce']

with open('schemas.json') as data_file:
    data = json.load(data_file)

# 1st pass - build field lookup
flookup = {}
for s in data:
    sid = s['id']
    flookup[sid] = {}
    for f in s['fields']:
        fid = f['id']
        # copy all field properties except mappings
        field = {}
        for k,v in f.items():
            if k == 'mappings':
                continue
            field[k] = v 
        flookup[sid][fid] = field

# 2nd pass - mappings: dereference fields and key on target schema
for s in data:
    for f in s['fields']:
        # target schemas - ordered
        mappings = OrderedDict()
        for c in COL_ORDER:
            if c == s['id']:
                continue
            mappings[c] = []
        if 'mappings' in f:
            for m in f['mappings']:
                sid = m['schema']
                fid = m['id']
                field = flookup[sid][fid]
                for k,v in field.items():
                    m[k] = v
                mappings[sid].append(m)
        f['mappings'] = mappings

import django
from django.conf import settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()
from django.template.loader import get_template
from django.template import Context
template = get_template('tables.html')
print template.render(Context({'schemas': data}))
