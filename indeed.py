import requests
from bs4 import BeautifulSoup

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.2.0.1713 Safari/537.36'}
    url = f'https://www.indeed.com/jobs?q=java%20developer&l=American%20Canyon%2C%20CA&start={page}'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for item in divs:
        title = item.find('a').text.strip()
        company= item.find('span', class_ ='company').text.strip()
        try:
            salary = item.find('sapn', class_ = 'salaryText').text.strip()
        except:
            salary = ''
        summary = item.find('div', {'class' : 'summary'}).text.strip()    
        job = {
          'title': title,
          'company': company,
          'salary': salary,
          'summary': summary,  
        }
        joblist.append(job)
    return

joblist = []
c = extract(10)  

transform(c)
print(joblist)
