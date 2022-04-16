# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 22:19:32 2022

@author: Zahid
"""

import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from time import sleep
from random import randint

chromedriver_path = "C:\Windows\\chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
 
url = "http://www.usnews.com/best-colleges/rankings/national-universities"
driver.get(url)
sleep(randint(3, 5))

