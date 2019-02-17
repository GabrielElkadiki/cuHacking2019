import requests

url = "https://api.spotify.com/v1/me/player/devices"

payload = ""
headers = {
    'Authorization': "Bearer BQAtR0TZtD9XRyhaebE1kVkfs0PUn-YQjf0ERDW5t_OSoB95q08J75gouG3Rnm0cQrvcgp7RyIMWynFJd2iqen1s69FvrJU1ORUp1LdOVo9914blbqy3FXwJ61qKthrdkEWbor4N4XrXqRhp7x5_Pvdu4eFn8lh_B_ci8SlFcVZWzDA",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
