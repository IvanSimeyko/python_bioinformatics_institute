import requests, re
import sys
from bs4 import BeautifulSoup

sys.stdin = open('input.txt', 'r')

# r = requests.get('http://ivansimeyko.com')   # простой get запрос
# print(r.text)   # вывод ответа сервера

#Задание
#  программе на вход подаются две строки, содержащие url двух документов A и B.
#Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

# get urls
n, k = 2, 0
urls = []
while k < n:
    urls.append(input('Enter url: ').strip())
    k += 1

# make get request
r = requests.get(urls[0])
#print(r.text)

# find links in page
def find_urls(reg):
    pattern = r'"((http|ftp)s?://.*?)"'
    link = re.findall(pattern, reg.text)
    link = set(tuple(j for j in i if j)[0] for i in link)
    return link

link = find_urls(r)
print(link)

# go to all link in page and find  particular url
def go_and_find(link, find_url):
    for i in link:
        r = requests.get(i)
        all_links = find_urls(r)
        if find_url in all_links:
            return 'Yes'
    return 'No'

print(go_and_find(link, urls[1]))

