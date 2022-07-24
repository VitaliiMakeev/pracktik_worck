import requests
import re

res = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
respo = res.text
resporet = respo.split('\n')[0]
print(f'raw = {resporet}')

remote_addr_pr = re.compile(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}')
request_datetime_pr = re.compile(r'\d{1,2}[/]\w{1,4}[/]\d{4}[:]\d{2}[:]\d{2}[:]\d{2}\s*[+]\d{4}')
request_type_pr = re.compile(r'[A-Z]{3}')
request_resours_pr = re.compile(r'[/]\w+[/]\w+[_]\w')
response_code_pr = re.compile(r'\s\d{3}\s')
response_size_pr = re.compile(r'\s\d+\s["]')
size = re.search(response_size_pr, resporet).group(0).replace(' ', '', 2).replace('"', '')
code_ = re.search(response_code_pr, resporet).group(0).replace(' ', '', 2)
resours = re.search(request_resours_pr, resporet).group(0)
type_ = re.search(request_type_pr, resporet).group(0)
addr = re.match(remote_addr_pr, resporet).group(0)
date_ = re.search(request_datetime_pr, resporet).group(0)
print(f"parsed_raw = ('{addr}', '{date_}', '{type_}', '{resours}', '{code_}', '{size}')")
# print(size)
tmp = []
#Особенные строки tmp_2
tmp_2 = []
# for i in resporet:
#     if re.match(remote_addr_pr, i):
#         addr = re.match(remote_addr_pr, i).group(0)
#         tmp.append(addr)
#     else:
#         tmp_2.append(i)
# # print(tmp_2, len(tmp_2))