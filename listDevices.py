import requests

url = "https://api.spotify.com/v1/me/player/devices"

payload = ""
headers = {
    'Authorization': "Bearer BQBv5qyjDDM1YTmPOZ7CDAX17ZVHDY6geBD7UeI4ee_FYJb_vkDwzyBOKlBug0PTabdeu1ypPT41MTmcDumNAbT8VrLb0lMg3sD1wwb4WMkvXaW6jHiaqyBR0cHfPmkI9etRz1CiKr3yckFbSN0RirIWodLanMZuyICS3I6N31zx6_M",
    'cache-control': "no-cache",
    }

response = requests.request("GET", url, data=payload, headers=headers)

print(response)
