import requests, re

#second task in week
# get file
#url = input('Enter file path: ')

# doing get request
def get_links(path):
    reg = requests.get(path)
    #print(reg.text)
    pattern = r'href=.*'
    link = re.findall(pattern, reg.text)
    #link = set(tuple(j for j in i if j)[0] for i in link)
    return link

a = get_links('http://pastebin.com/raw/hLx3HeZV')
for i in a:
    print(i)