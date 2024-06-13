# Get Data From Wiki and Save it in CSV

import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

import WikiHeader


def GetLanguages():
    url = 'https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes'
    response = requests.get(url, headers=WikiHeader.WikiHeaderReturn())
    soup = BeautifulSoup(response.content, 'html.parser')
    pattern = ['', '', '', '']
    pattern[0] = re.compile(r'^[a-z]{2}$')
    pattern[1] = re.compile(r'[A-Z]{1}')
    pattern[2] = re.compile(r'^ISO.*?')
    pattern[3] = re.compile(r'^[A-Za-zü]+(\s[A-Za-zü]+)?$')
    codes = []
    for link in soup.find_all('a', rel='nofollow'):
        codes.append(link.text.strip())
    codes = [code for code in codes if pattern[0].search(code)]
    # print(codes)
    names = []
    links = soup.find_all('a', href=lambda href: href and href.startswith('/wiki/') or 'mw-redirect' in (
        link_class := link.get('class', [])))
    for link in links:
        href = link.get('href')
        names.append(link.text.strip())
    names = [name for name in names if pattern[1].search(name)]
    names = [name for name in names if not pattern[2].search(name)]
    names = [name for name in names if pattern[3].search(name)]
    names = names[19:-5]
    to_remove = ['Vanuatuan languages', 'West Flemish', 'Ancient Greek',
                 'Standard Malay', 'Nynorsk', 'Yi languages', 'Filipino',
                 'French Polynesia', 'Twi', 'Fanti', 'Standard Arabic', 'Eastern Armenian',
                 'Western Armenian', 'Classical Armenian', 'Flemish']
    names[names.index('Church\xa0Slavonic')] = 'Church Slavonic'
    for element in to_remove:
        names.pop(names.index(element))
    # print(len(codes), len(names))
    # names.append('')
    data = {'Language Name': names,
            'Langauge Codes': codes}
    df = pd.DataFrame(data)
    df.to_csv('LanguageSelector.csv', index=False)
