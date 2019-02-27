```bash
'curl -X POST "https://domain.name.example.com.us-east-1.es.amazonaws.com/_reindex" -H 'Content-Type: application/json' -d'
{
  "source": {
    "index": "github-data-02.17"
  },
  "dest": {
    "index": "github-data-2019.02.17"
  }
}
'
```

```curl -X DELETE "https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.17"```

```curl -XGET https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.20/?pretty > index```


```curl -XPUT https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.20-fixed -H 'Content-Type: application/json' -d@index```

```curl -XPOST https://domain.name.example.com.us-east-1.es.amazonaws.com/_reindex -H 'Content-Type: application/json' -d '{ "source": { "index" : "github-data-2019.02.20" },"dest" : { "index" : "github-data-2019.02.19" } }'```

```curl -XDELETE https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.20'```
