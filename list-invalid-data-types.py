#!/usr/bin/python

import elasticsearch
import certifi

es = elasticsearch.Elasticsearch('https://search-kibana-7dn4x3q63sbgzkvxyq2fvoqjby.us-east-1.es.amazonaws.com',use_ssl=True, ca_certs=certifi.where())
index_list = es.indices.get('*')

#the fields in kibana that show as a conflict
fields = ['repository.pushed_at', 'repository.created_at']

#get a list of mappings, filtered by the fields we are inspecting
mappings = es.indices.get_field_mapping(",".join(fields), "*")

for m in mappings:
    if mappings[m]['mappings']:
        print(m)
        print(mappings[m]['mappings'])
