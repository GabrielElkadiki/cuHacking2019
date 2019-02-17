import requests
import base64


url = 'https://accounts.spotify.com/api/token'
client_id = '78581569df8f435e82dcc96dfc400070'
client_secret = 'ed22f981f0f64258bad72f62aa1f1923'

credentials = ('%s:%s' % (client_id, client_secret))

headers = {
    "Authorization": "Basic " + str(base64.b64encode(credentials.encode())).replace("b'", "").replace("'", ""),
}
print(headers['Authorization'])
data = {
  'grant_type': 'client_credentials'
}

response = requests.post(url, headers=headers, data=data)

print(response.text)
