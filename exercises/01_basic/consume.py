# https://docs.thecatapi.com/
import urllib2
import json

response = urllib2.urlopen("https://api.thecatapi.com/v1/images/search?breed_id=beng")

content = response.read()

content_dict = json.loads(content)
print (json.dumps(content_dict, indent=2))
