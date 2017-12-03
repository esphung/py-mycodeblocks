# -*- coding: utf-8 -*-
# @Author: homeuser
# @Date:   2017-11-29 10:16:53
# @Last Modified 2017-12-02
# @Last Modified time: 2017-12-02 21:03:03

import urllib.request
from bs4 import BeautifulSoup


result = urllib.request.urlopen('https://www.google.com/').read()

soup = BeautifulSoup(result, 'html.parser')

print(soup.title)

