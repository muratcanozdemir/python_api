import requests

r = requests.get("https://xkcd.com")
print(r.links)