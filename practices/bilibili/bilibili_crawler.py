import re
import requests
import csv

base_url = 'https://m.dytt8.net'

url = 'https://space.bilibili.com/517327498?spm_id_from=333.1007.tianma.2-3-6.click'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

data = {
    'spm_id_from': '333.1007.tianma.2-3-6.click'
}

resp = requests.get(url, headers=headers, data=data)
page_text = resp.text
print(page_text)

# with open('./dytt.html', 'w', encoding='utf-8') as f:
#     f.writelines(page_text)
#
# obj0 = re.compile(r'<div class="title_all"><p><strong>2022新片精品</strong>.*?</table>', re.S)
# obj1 = re.compile(r"最新电影下载</a>]<a href='(?P<href>.*?)'>(?P<movie>.*?)</a><br/>", re.S)
# obj2 = re.compile(r'<a target="_blank" href="(?P<download_url>.*?)"><strong><font style="BACKGROUND-COLOR: #ff9966">'
#                   r'<font color="#0000ff"><font size="4">磁力链', re.S)
#
# download_url_list = []
# href_list = []
# movie_name_list = []
#
# results = obj0.finditer(page_text)
# for m in results:
#     ul = m.group()
#
#     child_results = obj1.finditer(ul)
#     for n in child_results:
#         href = n.group('href')
#         movie_name = n.group('movie')
#         href_list.append(href)
#         movie_name_list.append(movie_name)
#         # print(href, movie_name)
#
#
#
# for movie_name, href in zip(movie_name_list, href_list):
#     child_url = base_url + href
#     child_resp = requests.get(child_url, headers=headers)
#     child_resp.encoding = 'gb2312'
#     child_page_text = child_resp.text
#
#     result = obj2.search(child_page_text)
#     download_url_list.append(result.group('download_url'))
#
#     print(movie_name, download_url_list[-1])
#
# f = open('movie_download_urls.csv', 'w')
# csv_writer = csv.writer(f)
#
# for movie_name, download_url in zip(movie_name_list, download_url_list):
#     csv_writer.writerow([movie_name, download_url])
#
# print('Done!!!')
#
# f.close()
#
