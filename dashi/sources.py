from elasticsearch import Elasticsearch

class Source(object):
    def __init__( self, conf, *args, **kwargs ):
        pass

class Elasticsearch_Source( Source ):
    def __init__( self, conf, *args, **kwargs ):
        super( Elasticsearch_Source, self ).__init__(conf, *args, **kwargs)
        self.client = Elasticsearch()
    def query(self):
        res = self.client.search(
            index = self.conf['data']['index'],
            body = self.conf['data']['query']
        )
        return [ r.values() for r in res['aggregations'][self.conf['data']['use']]['buckets'] ]
