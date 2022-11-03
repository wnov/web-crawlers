import requests

query = input('请输入搜索内容: ')
url = f"https://www.sogou.com/web?query={query}"

header_dict = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=header_dict)

print(resp.text)

resp.close()
