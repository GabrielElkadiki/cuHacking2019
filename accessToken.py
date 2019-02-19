import requests
import base64


url = 'https://accounts.spotify.com/api/token'
client_id = ''
client_secret = ''

credentials = ('%s:%s' % (client_id, client_secret))

headers = {
    "Authorization": "Basic " + str(base64.b64encode(credentials.encode())).replace("b'", "").replace("'", ""),
}
data = {
  'grant_type': 'client_credentials'
}

response = requests.post(url, headers=headers, data=data)
access_token = (response.text.split(":")[1].split(",")[0].strip("\""))
