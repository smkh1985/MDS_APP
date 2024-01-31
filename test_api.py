import requests


endpoint = 'http://127.0.0.1:8000/products/'



# res = requests.post(endpoint , data = {"water_type" : 'MDS',"bottle_size" : 5,"price" : 5})
res = requests.get(endpoint)
print(res.json())