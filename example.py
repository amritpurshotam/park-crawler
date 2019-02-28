import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.Request(
    "https://www.parkrun.co.za/events/", 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, 'lxml')
links = soup.find_all('a')
print(links)