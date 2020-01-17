import requests
from lxml import html
import pandas as pd


search_url = 'https://stat.gov.pl/obszary-tematyczne/rynek-pracy/bezrobocie-rejestrowane/stopa-bezrobocia-rejestrowanego-w-latach-1990-2019,4,1.html'
page = requests.get(search_url)
html.fromstring(page.content)
print(xpath('/html/body/section[2]/div[1]/div/article/section/table/tbody[1]/tr/th[1]/p/text()'))
            