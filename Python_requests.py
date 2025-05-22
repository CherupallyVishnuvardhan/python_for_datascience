import requests
response=requests.get("https://en.wikipedia.org/wiki/Mahesh_Babu")
print(response)

#Headers
print(response.headers)

#Content Type
print(response.headers['Content-Type'])

#Body Content
print(response.content)