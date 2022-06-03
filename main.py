import requests
from bs4 import BeautifulSoup
import re

data = []
zel = 0; put = 0; por = 0; baid = 0; jon = 0
art_z =[]; art_p = []; art_por=[]; art_baid=[]; art_jon =[]

print('input number of pages you want to purs:')

pages = input()
pages = int(pages)


for p in range(0, pages):
    url = f'https://www.pravda.com.ua/articles/page_{p}/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    news = soup.findAll('div', class_="article article_list")


    polit = ['Зел', 'Пут', 'Порош', 'Байд', 'Джонс',]

    x = 0

    for each in news:
        for y in polit:
            link = each.find('div', class_="article_header").find('h3').find('a').get('href')
            text = each.find('div', class_="article_header").find('h3').find('a').text

            if re.search(y, text):
                data.append([link, text])


    for y in data:
        for each in polit:
            if re.search(each, y[1]):
                if each == 'Зел':
                    zel += 1
                    art_z.append(y[0])
                if each == 'Пут':
                    put += 1
                    art_p.append(y[0])
                if each == 'Порош':
                    por += 1
                    art_por.append(y[0])
                if each == 'Байд':
                    baid += 1
                    art_baid.append(y[0])
                if each == 'Джонс':
                    jon += 1
                    art_jon.append(y[0])


pres = {'Згадування політика Зеленського' : zel,'Згадування політика Путіна' :  put,'Згадування політика Порошенка' :  por,'Згадування політика Байдена' :  baid,'Згадування політика Джонсона' :  jon}
arts = {'Посилання де згадували Зеленського': art_z,'Посилання де згадували Чорта':  art_p,'Посилання де згадували Порошенка': art_por,'Посилання де згадували Байдена': art_baid,'Посилання де згадували Джонсона': art_jon}


print(pres)
print(arts)

#print(data)

# print(soup.find('div', class_="article article_list").find('div', class_="article_header").find('h3'))

# print(soup.find('div', class_="article article_list").find('div', class_="article_header").find('h3').find('a').get('href'))

# print(soup.find('div', class_="article article_list").find('div', class_="article_header").find('h3').find('a').text)
