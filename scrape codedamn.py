# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 12:09:15 2022

@author: Zahid
"""

# import requests

# res = requests.get('https://codedamn.com')

# print(res.text)
# print(res.status_code)

# import requests

# # Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
# # Store the result in 'res' variable
# res = requests.get(
#     'https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
# txt = res.text
# status = res.status_code

# print(txt, status)


import requests
from bs4 import BeautifulSoup

page = requests.get("https://codedamn.com")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>
print(title)




# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_title, page_head)
