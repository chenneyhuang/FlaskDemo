import requests, json

###comment the codes with non json format
#user_info = {'name': ['letian', 'chenney', 'orange'], 'password': '123'}
#r = requests.post("http://127.0.0.1:5000/register", data=user_info)

#print r.text

user_info = {'name': 'letian'}
headers = {'content-type': 'application/json'}
r = requests.post("http://127.0.0.1:5000/json", data=json.dumps(user_info), headers=headers)
print r.headers
print r.json()