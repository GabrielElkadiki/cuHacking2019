import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQAtR0TZtD9XRyhaebE1kVkfs0PUn-YQjf0ERDW5t_OSoB95q08J75gouG3Rnm0cQrvcgp7RyIMWynFJd2iqen1s69FvrJU1ORUp1LdOVo9914blbqy3FXwJ61qKthrdkEWbor4N4XrXqRhp7x5_Pvdu4eFn8lh_B_ci8SlFcVZWzDA',
}

response = requests.put('https://api.spotify.com/v1/me/player/pause', headers=headers)
