from collections import defaultdict, OrderedDict
import json
from pprint import pprint

with open('../schemas.json') as data_file:
    data = json.load(data_file)

import csv
with open('schemas.csv', 'wb') as f:
    writer = csv.writer(f);
    writer.writerow(['id','title','shorttitle','version','url'])
    for s in data:
        if('version' not in s):
            s['version'] = ''
        writer.writerow([s['id'], s['title'], s['shorttitle'], s['version'], s['url']])

with open('fields.csv', 'wb') as f:
    writer = csv.writer(f);
    writer.writerow(['schema','id','field','label','shortlabel','url'])
    for s in data:
        for f in s['fields']:
            if('url' not in f):
                f['url'] = ''
            if('field' not in f):
                f['field'] = ''
            if('shortlabel' not in f):
                f['shortlabel'] = ''
            writer.writerow([s['id'], f['id'], f['field'], f['label'], f['shortlabel'], f['url']])

with open('mappings.csv', 'wb') as f:
    writer = csv.writer(f);
    writer.writerow(['from_schema','from_field','to_schema','to_field'])
    for s in data:
        for f in s['fields']:
            if 'mappings' in f:
                for m in f['mappings']:
                    writer.writerow([s['id'], f['id'], m['schema'], m['id']])
                    if 'note' in m:
                        with open('mappings/%s-%s-%s-%s.html' % (s['id'], f['id'], m['schema'], m['id']), 'w') as g:
                            g.write(m['note'])
