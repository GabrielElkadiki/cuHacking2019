import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQDZyIcTa3ndgT0CwvEDU5Z1uayf0dqeXRGu0OTJ0DGq-0V0TTfVq8gAP2Yyw2FlZ2dfsb7a0S2lCaABdtk6doc0CQqKDnhL2M1W3CrCJM4rGL4zecCjMi74vCH5nWkaWo9Oj4QbzmHR-YUAbC-DyK01zRXL1qaGhHaUl-7OSScn7LQ',
}

data = '{"device_ids":["ac44d0e8c891d14ad1396b2f10786c148d1d5c5b"]}'

response = requests.put('https://api.spotify.com/v1/me/player', headers=headers, data=data)
