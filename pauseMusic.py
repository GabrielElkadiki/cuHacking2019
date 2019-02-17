import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQDZCqa5Bvro-qTGYRxVwx1HMFY82nnHyJKBtnStybCQOP-DFSVfmRFfA1KQLiJ2mZh6Hd_Q8UOny-iTw_0RE-OPGNa9iR1aftoDFpL6SWSfF1spQ3fsGQz8uahXLQBG_YQ1vqk6vF8CVHp7yDy11P6SLAUd1WPPDpy1xQ7SPCP1ELY',
}

response = requests.put('https://api.spotify.com/v1/me/player/pause', headers=headers)
