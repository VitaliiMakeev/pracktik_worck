import requests
respons = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
content = respons.text
rest_f = content.split('\n')

remote_list = [i.split(' - - ')[0] for i in rest_f]

request_type_list = []
requested_resource_list = []

for i in rest_f:
    n = i.split('"')
    for _ in n:
        if 'GET' in _:
            request_type = _.split()[0]
            request_type_list.append(request_type)
            requested_resource = _.split()[1]
            requested_resource_list.append(requested_resource)

logs_list = [(i, j, n) for i, j, n in zip(remote_list, request_type_list, requested_resource_list)]
result = str(logs_list)
# print(result)


with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    for i in logs_list:
        f.write(str(i) + '\n')

