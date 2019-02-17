import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQCdPwIPStZ7-DAsSPhlYSzxrHsZ89k9cUxVxuGXRnpKzaMOiWDOhaKWWtewKSSFGFHNSrQUtLzAnltpb2zhlIiH15AQvQKJWNCpgshPrmQCPGQewtS1M9Il3DKbDCAhCsAB1CayKxssHIkeaTploGjaU0_ueBReM5KFDj1hkUleBa0',
}

params = (
    ('device_id', '3aaf88397070392807b41c16deb1d75c1369e028'),
)

data = '{"context_uri":"spotify:playlist:37i9dQZF1DX7FY5ma9162x","offset":{"position":0},"position_ms":0}'

response = requests.put('https://api.spotify.com/v1/me/player/play', headers=headers, params=params, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.put('https://api.spotify.com/v1/me/player/play?device_id=3aaf88397070392807b41c16deb1d75c1369e028', headers=headers, data=data)
