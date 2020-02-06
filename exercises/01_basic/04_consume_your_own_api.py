# https://docs.thecatapi.com/
import urllib
import json

api_url = "http://localhost:8080"
headers = {"Accept": "application/json"}
response = requests.get(api_url, headers=headers)

print "code:"+ str(response.status_code)
print "******************"
print "headers:"+ str(response.headers)
print "******************"
print "content:"+ str(response.text)