# import requests

# url="https://api.github.com/users/aryanjain17"
# r=requests.get(url)
# print(r.content)

#Add Package
import requests

#Prepare URL
url="https://api.github.com/users/aryanjain17"

#Web REST API Calls (GET- HTTP VERB) Request
#response=requests.get(url,params={k:v},args)
r=requests.get(url)

#Fetch Reponse Content
print(r.content)