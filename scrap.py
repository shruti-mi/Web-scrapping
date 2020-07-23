from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests

URL = 'https://www.linkedin.com/jobs/search?keywords=software%20engineer&redirect=false&position=1&pageNum=0'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('div', class_='result-card__contents')

# connection to the db
conn = MongoClient()
db = conn.job_info

for res in results:
    company_name = res.find('h4', class_='result-card__subtitle')
    post_name = res.find('h3', class_='job-result-card__title')
    location = res.find('span', class_='job-result-card__location')
    print(post_name.text)
    print(company_name.text)
    print(location.text)
    db.job_details.insert({"company_name": company_name.text,
                           "post_name": post_name.text,
                           "location": location.text
                           })
    print()
