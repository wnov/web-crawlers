import requests

url = 'https://movie.douban.com/j/chart/top_list'
header_dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

param = {
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20,
}

resp = requests.get(url, params=param, headers=header_dict)

print(resp.json())

resp.close()
