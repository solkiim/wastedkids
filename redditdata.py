import requests
import json

# url = "http://www.reddit.com/r/childrenfallingover/top/.json?count=1"
url = "http://www.reddit.com/r/childrenfallingover/top/.json?count=1"

json_resp = requests.get(url, headers = {'User-agent': 'wastedkids by /u/chickmcnug'})
resp = json.loads(json_resp.content)

print len(resp["data"]["children"])

for post in resp["data"]["children"]:
	print post["data"]["url"]
