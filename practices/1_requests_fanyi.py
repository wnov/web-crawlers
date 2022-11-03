import requests

url = 'https://fanyi.baidu.com/sug'

kw = input('输入要翻译的文本: ')
# 输入参数字典
data_kw = {
    'kw': kw
}

resp = requests.post(url, data=data_kw)

print(resp.json())

resp.close()
