import requests

URL = "http://www.google.com/"

queryParams = {"one": 1, "param_two": 2}

res = requests.get(url=URL, params=queryParams)


# Case of an error or bad request
res.raise_for_status()

# All is right in the world
data = res.json()  # As a dict


# POST
res = requests.post(url=URL, json={"data": "to post"}, headers={"head-key": "val"})
print(res.text)
