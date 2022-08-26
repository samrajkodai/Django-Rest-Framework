import requests

endpoint="http://127.0.0.1:8000/api"
result=requests.get(endpoint, json={"title": "Abc123", "query": "Hello world"})

print(result.json())