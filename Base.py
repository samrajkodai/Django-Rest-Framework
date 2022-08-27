import requests

# endpoint="http://127.0.0.1:8000/api/"
# result=requests.post(endpoint, json={'title': 'new',
#             'content': 'testing',
#             'price': 12,
#             'sale_price':45})

# print(result.json())

endpoint="http://127.0.0.1:8000/api/1/"
result=requests.get(endpoint, json={'title': 'new',
            'content': 'testing',
            'price': 12,
            'sale_price':45})

print(result.json())
