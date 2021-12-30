import requests
from bs4 import BeautifulSoup

endpoint_url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit" \
               "&txtKeywords=python&txtLocation= "
html_text = requests.get(endpoint_url).text
soup = BeautifulSoup(html_text,'lxml')