import requests
from cuHacking2019 import accessToken

url = "https://api.spotify.com/v1/me/player/devices"

payload = ""
headers = {
    'Authorization': "Bearer " + accessToken.access_token,
    'cache-control': "no-cache",
    }
print("BQCLDEbhiFi-Eodmd73zNI4tsC15_BaXqXVsq3aNevaFXEdJopzbQ_4mqVHwd8m2Y3s3L1k8kBPH_eroK1UC1RE4wbSMsJF18sEpTqQqfKsnZGq9DW5VcsIEUXAFvsx82uEnIrH-WgdsT-1hsbQ2CLxwLk75bpZmKn22cdBeGE3NWA4")
print(accessToken.access_token)
response = requests.request("GET", url, data=payload, headers=headers)

print(response.text)
