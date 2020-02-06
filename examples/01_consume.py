# https://docs.thecatapi.com/
import requests
import json

api_url = "https://api.thecatapi.com/v1/images/search?breed_id=beng"
headers = {"Accept": "application/json"}
response = requests.get(api_url, headers=headers)

print("code:\n" + str(response.status_code))
print("\n==================\n")
print("headers:\n" + str(response.headers))
print("\n==================\n")
print("content:\n" + str(response.text))
print("\n==================\n")

print("pretty content:\n" + json.dumps(json.loads(response.text), indent=2))

# Assignment:
# Please print only the name, description, and temperament of the Bengal cat


# Extra credit:
# Please print the names of all the cats in the database
