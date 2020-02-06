# https://docs.thecatapi.com/
import requests
import json

api_url = "http://localhost:8080"
headers = {"Accept": "application/json"}
response = requests.get(api_url, headers=headers)

print("code:\n" + str(response.status_code))
print("\n==================\n")
print("headers:\n" + str(response.headers))
print("\n==================\n")
print("content:\n" + str(response.text))
print("\n==================\n")

print("pretty content:\n" + json.dumps(json.loads(response.text), indent=2))

# Assignment
# Get all ages and increment by 2 and POST to API
