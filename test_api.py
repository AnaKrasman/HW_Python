import requests
import json

url = "https://petstore.swagger.io/v2/user"
#	Verify that allows creating a User
payload = json.dumps({
  "id": 10,
  "username": "test32",
  "firstName": "test21",
  "lastName": "test112",
  "email": "test11",
  "password": "test11",
  "phone": "test11",
  "userStatus": 0
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)

# Verify that allows login as a User


url = "https://petstore.swagger.io/v2/user/login?username=test1&password=test1"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)



# Verify that allows creating the list of Users

url = "https://petstore.swagger.io/v2/user/createWithList"

payload = json.dumps([
  {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)

#	Verify that allows Log out User

url = "https://petstore.swagger.io/v2/user/logout"

payload = ""
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)

#	Verify that allows adding a new Pet


url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "id": 10,
  "category": {
    "id": 10,
    "name": "string"
  },
  "name": "test",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)
resp_json = response.json()
assert resp_json['name'] == 'test', f'Expected the name to be "test", got {resp_json["name"]}'


#	Verify that allows updating Pet’s image

url = "https://petstore.swagger.io/v2/pet/10/uploadImage"

payload = {'file': ''}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)


#	Verify that allows updating Pet’s name and status

import requests
import json

url = "https://petstore.swagger.io/v2/pet"

payload = json.dumps({
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "test",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
assert response.status_code == 200

print(response.text)
resp_json = response.json()
assert resp_json['name'] == 'test', f'Expected the name to be "test", got {resp_json["name"]}'


#	Verify that allows deleting Pet 


url = "https://petstore.swagger.io/v2/pet/10?Id=10"

payload = {}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)
assert response.status_code == 200
print(response.text)
