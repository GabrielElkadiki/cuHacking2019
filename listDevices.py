import requests

url = "https://api.spotify.com/v1/me/player/devices"

payload = ""
headers = {
    'Authorization': "Bearer BQCdPwIPStZ7-DAsSPhlYSzxrHsZ89k9cUxVxuGXRnpKzaMOiWDOhaKWWtewKSSFGFHNSrQUtLzAnltpb2zhlIiH15AQvQKJWNCpgshPrmQCPGQewtS1M9Il3DKbDCAhCsAB1CayKxssHIkeaTploGjaU0_ueBReM5KFDj1hkUleBa0",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
