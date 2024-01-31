import requests


get_detail = 'http://127.0.0.1:8000/products/2'

get_list  = 'http://127.0.0.1:8000/products/'

# res = requests.put(get_detail , data = {"price" : 500})
# print(res.json())
res = requests.get(get_list)
print(res.json())