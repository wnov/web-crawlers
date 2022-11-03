import re
import requests
import csv

url = 'https://movie.douban.com/top250?start=25'
headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'

page_text = resp.text
with open('./douban_top_250.html', 'w') as f:
    f.write(page_text)

pattern = r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?导演: (?P<director>.*?)&nbsp.*?' \
          r'<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'

obj = re.compile(pattern, re.S)

result = obj.finditer(page_text)

f = open('./crawler_results.csv', 'w')
csv_writer = csv.writer(f)

for m in result:
    # print(m.group('name'))
    # print(m.group('director'))
    # print(m.group('year').strip())
    # print(m.group('score'))
    group_dict = m.groupdict()
    group_dict['year'] = group_dict['year'].strip()
    csv_writer.writerow(group_dict.values())

f.close()



