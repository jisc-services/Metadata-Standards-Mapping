from collections import defaultdict
import json
from pprint import pprint

schemas = {}
fields = {}
mappings = {}

with open('schemas.json') as data_file:
    data = json.load(data_file)

# load data
for schema in data['schemas']:
    schemas[schema['id']] = schema
    fields[schema['id']] = {}
    mappings[schema['id']] = {}
    for field in schema['fields']:
        fields[schema['id']][field['id']] = field
        if 'mappings' in field:
            field_mappings = defaultdict(list)
            for mapping in field['mappings']:
                field_mappings[mapping['schema']].append(mapping)
            mappings[schema['id']][field['id']] = field_mappings

# check mappings
for src_schema in mappings:
    for src_field in mappings[src_schema]:
        for tgt_schema  in mappings[src_schema][src_field]:
            for mapping in mappings[src_schema][src_field][tgt_schema]:
                tgt_field = mapping['id']
                if tgt_field not in fields[tgt_schema]:
                    print 'invalid identifier in mapping %s.%s -> %s.%s' % (src_schema, src_field, tgt_schema, tgt_field)
