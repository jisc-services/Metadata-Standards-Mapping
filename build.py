from collections import OrderedDict
import csv
import django
from django.conf import settings
from django.template.loader import get_template
from django.template import Context
import os.path

# read schemas
schemas = OrderedDict()
with open('data/schemas.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        schemas[row['id']] = row

# read fields
fields = {}
with open('data/fields.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = row['schema']
        if sid not in fields:
            fields[sid] = OrderedDict()
        row['schema'] = schemas[sid].copy() # dereference schema
        fields[sid][row['id']] = row

# read mappings
mappings = {}
with open('data/mappings.csv', 'rb') as f:
    reader = csv.DictReader(f)
    for row in reader:
        fsid = row['from_schema']
        if fsid not in mappings:
            mappings[fsid] = {}
        ffid = row['from_field']
        if ffid not in mappings[fsid]:
            mappings[fsid][ffid] = OrderedDict()
        tsid = row['to_schema']
        if tsid not in mappings[fsid][ffid]:
            mappings[fsid][ffid][tsid] = []
        mappings[fsid][ffid][tsid].append(row['to_field'])

# build context for template
data = []
for sid in schemas:
    schema = schemas[sid].copy()
    data.append(schema)
    schema['fields'] = []
    for fid in fields[sid]:
        field = fields[sid][fid].copy()
        schema['fields'].append(field)
        field['mappings'] = OrderedDict()
        if fid in mappings[sid]:
            for tsid in mappings[sid][fid]: # ordered
                for tfid in mappings[sid][fid][tsid]:
                    tfield = fields[tsid][tfid].copy()
                    if tsid not in field['mappings']:
                        field['mappings'][tsid] = []
                    field['mappings'][tsid].append(tfield)
                    notefile = 'data/mappings/%s-%s-%s-%s.html' % (sid, fid, tsid, tfid)
                    if os.path.isfile(notefile):
                        with open(notefile, 'r') as f:
                            tfield['note'] = f.read()

# populate and print template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
    }
]
settings.configure(TEMPLATES=TEMPLATES)
django.setup()
template = get_template('tables.html')
print template.render(Context({'schemas': data}))