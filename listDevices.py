import requests

url = "https://api.spotify.com/v1/me/player/devices"

payload = ""
headers = {
    'Authorization': "Bearer BQCg-OxenkXgHHeVYv1Nd0ocRDo9qwjzzKEA38PpJhDp1FizzPwirf83qcbhZCxdjb4CptQSqYwJ3f00Z_knWTwefT5iIDTBZ6a4j7ZRqnbOc6-7fPJvJKxwhQoeXMYUOST4XrMg4YbSQ8x2T5I3RyTcyE5uQbcnMiiYSqyYI-Rc3QY",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
