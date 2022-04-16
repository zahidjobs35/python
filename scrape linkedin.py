# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:15:43 2022

@author: Zahid
"""



# import web driver
from selenium import webdriver

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('c:\windows\chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')


# send_keys() to simulate key strokes
username.send_keys('example@gmail.com')

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys('xxxxxx')

# locate submit button by_class_name
log_in_button = driver.find_element_by_class_name('login-submit')

# locate submit button by_class_id
log_in_button = driver.find_element_by_class_id('login submit-button')

# locate submit button by_xpath
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
log_in_button.click()

# Navigate to the directory where the file is
# cd Desktop 

# Command to execute the python file
# python script.py

# imports
from selenium import webdriver

# defining new variable passing two parameters
writer = csv.writer(open(parameters.file_name, 'wb'))

# writerow() method to the write to the file object
writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('c:\windows\chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()

