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
    return len(divs)

c = extract(10)  

print(transform(c))
