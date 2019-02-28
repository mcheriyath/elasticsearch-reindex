#!/usr/bin/env python
import boto3
from requests_aws4auth import AWS4Auth
import elasticsearch.helpers
from elasticsearch import Elasticsearch, RequestsHttpConnection

credentials = boto3.Session().get_credentials()

awsauth = AWS4Auth('<ACCESS ID>', '<ACCESS KEY>', 'us-east-1', 'es', session_token="<SESSION_TOKEN>")


elasticSource = Elasticsearch(
        hosts = [{'host': "engineering-metrics.kibana.com", 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

elasticDestination = Elasticsearch(
        hosts = [{'host': "engineering-metrics.kibana.com", 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

# Setup source and destinations connection to Elasticsearch. Could have been different clusters
# Delete index so we know it doesn't exist.
# elasticDestination.indices.delete(index="index-name", ignore=[400, 404])
# Create index with nothing in it.
# elasticDestination.indices.create(index="index-name", ignore=[400, 404])
elasticsearch.helpers.reindex(client=elasticSource, source_index="sourceIndexname", target_index="targetIndexname", target_client=elasticDestination)
