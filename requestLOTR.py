import requests, json
"""
Makes an API call to a LOTR book site.  This API endpoint retrieves all of the books 
in the LOTR series as well as an internal database ID number for reference when
making other API calls.
Headers is currently empty, but this is where you might send data as part of your request,
including authorization information or further information needed to fulfill the
request.
"""

url = "https://the-one-api.dev/v2/book/"


headers = {}

response = requests.request("GET", url, headers=headers)

x = json.loads(response.text)
for i in x:
    print(i,x[i])
