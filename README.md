#### Step 1
- Check the conflict fileds in kibana index patterns under `management > index patterns`
#### Step 2
- Edit list-invalid-data-types.py with the fields shown in the above step
#### Step 3
- Run the list-invalid-data-types.py to see the correct mappings
#### Step 4
- Take a backup of the index
```bash
curl -XGET https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.27/?pretty > index-github-data-2019.02.27.backup.json
```
#### Step 5
Open the file index-github-data-2019.02.27.backup.json and fix the mappings, types etc. <br>
Edit fields like: index-name, created, version etc. and save

#### Step 6
Create a new index with the fixed file
```bash
curl -XPUT https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.27-fixed -H 'Content-Type: application/json' -d@index-github-data-2019.02.27.backup.json
```
#### Step 7

- Re-index 
```bash
curl -X POST "https://domain.name.example.com.us-east-1.es.amazonaws.com/_reindex" -H 'Content-Type: application/json' -d'
{
  "source": {
    "index": "github-data-2019.02.27"
  },
  "dest": {
    "index": "github-data-2019.02.27-fixed"
  }
}
'
```

#### Step 8
- Delete the old index

```bash
curl -X DELETE "https://domain.name.example.com.us-east-1.es.amazonaws.com/github-data-2019.02.27"
```


