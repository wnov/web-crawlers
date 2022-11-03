import re

# # 匹配所有，返回列表
# lst = re.findall(r"\d+", "中国移动: 10086, 中国电信: 10010")
# print(lst)
#
# # 匹配所有，返回迭代器
# it = re.finditer(r'\d+', "中国移动: 10086, 中国电信: 10010")
# for i in it:
#     print(i.group())
#
# # 匹配第一个
# ser = re.search(r'\d+', "中国移动: 10086, 中国电信: 10010")
# print(ser.group())
#
# # 从开头匹配
# mat = re.match(r'\d+', "中国移动: 10086, 中国电信: 10010")
# print(mat)
#
# # 预编译正则表达式
# obj = re.compile(r'\d+')
# it = obj.finditer("中国移动: 10086, 中国电信: 10010")
# for i in it:
#     print(i.group())

str = """
<div class='mouse'><span id=1>杰瑞</span></div>
<div class='cat'><span id=2>汤姆</span></div>
<div class='dog'><span id=3>旺财</span></div>
<div class='snake'><span id=4>小青</span></div>
"""

obj = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span></div>", re.S)  # re.S让.可以匹配换行符
# (?P<分组名称>正则) 可以从正则表达式中单独抽取部分内容
obj = re.compile(r"<div class='.*?'><span id=(?P<id>\d)>(?P<name>.*?)</span></div>", re.S)

it = obj.finditer(str)
for i in it:
    print(i.group("name"))
    print(i.group("id"))

