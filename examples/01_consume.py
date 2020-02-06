# https://docs.thecatapi.com/
import requests
import json

api_url = "https://api.thecatapi.com/v1/images/search?breed_id=beng"
headers = {"Accept": "application/json"}
response = requests.get(api_url, headers=headers)

print ("code:"+ str(response.status_code))
print ("******************")
print ("headers:"+ str(response.headers))
print ("******************")
print ("content:"+ str(response.text))
print ("******************")


print ("pretty content:"+ json.dumps(json.loads(response.text), indent=2))
