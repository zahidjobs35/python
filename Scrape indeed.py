# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:58:45 2022

@author: Zahid
"""

# Import packages
import pandas as pd
import numpy as np
import requests
from scrapy.selector import Selector
from IPython.display import clear_output
import time
import re


search_titles = ["data analyst","data analytics","business analyst", "business intelligence", "data scientist","data science","data engineer","database engineer"]
                 
# Initialise empty list related to search term
job_URL_list = []
search_title_list = []

# Start timer
start = time.time()

# Iterating over search titles, job types and salary ranges..
for stitle in search_titles:

    # Crawl to the first page of the search results
    path = f"https://au.indeed.com/jobs?as_ttl={stitle.replace(' ','+')}&sr=directhire&radius=0&l=Australia&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch"
    req = requests.get(path)

    # Extract the URLs for extra pages 
    extra_page_URL_list = Selector(text=req.text).xpath('//div[@class="pagination"]/a/@href').getall()
    extra_page_URL_list = extra_page_URL_list[:-1] # drop the last URL, due to next button URL
    extra_page_URL_list = ['http://au.indeed.com' + i for i in extra_page_URL_list]            

    print(f'Page 1 of {len(extra_page_URL_list)+1}:', end = '\n\n')

    print(f'Searching for all jobs titles that include: {stitle}',end = '\n')

    # Extract all URLs for all the job listings in page 1
    page_job_URL_list = Selector(text=req.text).xpath('//a[@data-tn-element="jobTitle"]/@href').getall()
    print(f"{len(page_job_URL_list)} job URLs extracted from Page 1", end = '\n\n')

    # Append all job URLs
    # Append search titles, job types and salary ranges to match number of job URLs
    job_URL_list += page_job_URL_list
    for i in range(len(page_job_URL_list)):
        search_title_list.append(stitle)

    # To make sure all list lengths are equal
    print('Job URL count:',len(job_URL_list))
    print('Search title count:',len(search_title_list))
    clear_output(wait=True)

    time.sleep(0.1)

    # Iterate through all the additional pages
    page_count = 1
    for extra_page in extra_page_URL_list:
        page_count += 1

        # Crawl to extra page
        req = requests.get(extra_page)
        print(f'Page {page_count} of {len(extra_page_URL_list)+1}:', end = '\n\n')

        print(f'Searching for all jobs titles that include: {stitle}',end = '\n')

        # Extract all URLs for all the job listings in extra pages
        page_job_URL_list = Selector(text=req.text).xpath('//a[@data-tn-element="jobTitle"]/@href').getall()
        print(f"{len(page_job_URL_list)} job URLs extracted from Page {page_count}", end = '\n\n')

        # Append all job URLs
        # Append search titles, job types and salary ranges to match number of job URLs
        job_URL_list += page_job_URL_list
        for i in range(len(page_job_URL_list)):
            search_title_list.append(stitle)

        # To make sure all list lengths are equal
        print('Job URL count:',len(job_URL_list))
        print('Search title count:',len(search_title_list))
        clear_output(wait=True) 

        time.sleep(0.1)
                             
job_URL_list = ['http://au.indeed.com' + i for i in job_URL_list]
print(f"Job URL scraping completed: {len(job_URL_list)}", end = '\n')

end = time.time()

# Writing to df
search = pd.DataFrame({"search_title": search_title_list,"job_url_search": job_URL_list})
search.head()

# Writing to csv
!mkdir Data
search.to_csv('Datasearch.csv',index=False)