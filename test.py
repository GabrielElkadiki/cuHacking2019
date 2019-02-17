import requests

params = (
    ('client_id', '5fe01282e94241328a84e7c5cc169164'),
    ('redirect_uri', 'http://example.com/callback'),
    ('scope', 'user-read-private user-read-email'),
    ('response_type', 'token'),
)

response = requests.get('https://accounts.spotify.com/authorize', params=params)
print(response.text)