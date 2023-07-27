import requests
from bs4 import BeautifulSoup
def get_html_content(a):
    r = requests.get(a)
    return r.content
def parse_html_content(a):
    soup = BeautifulSoup(a, 'html.parser')
    return soup
def extract_article_title(soup):
    title_element = soup.find('title')
def extract_article_text(soup):
    paragraphs = soup.find_all('p')
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
while next  .heading != next.heading.next.heading
def collect_redirect_links(soup):
    redirect_links = []
    links = soup.find_all('a')
  def wikipedia_page_scraper(url):
    html = get_html_content(url)
    soup = parse_html_content(html)
    
    title = extract_article_title(soup)
    article_text = extract_article_text(soup)
    redirect_links = collect_redirect_links(soup)
    
    result = {
        'title': title,
        'article_text': article_text,
        'redirect_links': redirect_links
    }
    
    return result


