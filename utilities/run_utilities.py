from bs4 import BeautifulSoup
import requests
from datetime import datetime
import shelve

class Manhwa:
  def __init__(self, title, imglink, link, chapternum, chapterdate):
    self.title = title
    self.imglink = imglink
    self.link = link
    self.chapternum = chapternum
    self.chapterdate = chapterdate

def filter_titles(series_divs, titles_to_search_for):
  lib = []
  for div in series_divs:
    title_element = div.find('h4')
    if title_element:
      title = title_element.text.strip()
      for search_title in titles_to_search_for:
        if title == search_title:
          lib.append(div)
  return lib

# webistes == array, element_to_search == string, class_to_search == string
def site_parser(websites, element_to_search, class_to_search):
  desired_elements = []
  for url in websites:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      element_list = soup.find_all(element_to_search, class_=class_to_search)
      if element_list:
        for element in element_list:
          title_element = element.find('h4')
          if title_element:
            title = title_element.text.strip()
            desired_elements.append(Manhwa(title, url, element.find('a').get('href'), element.find('span', class_='chapternum').get_text(strip=True), element.find('span', class_='chapterdate').get_text(strip=True)))
  return desired_elements

def filter_by_date(chapters):
  today_chapter_spans = []
  today_datetime = datetime.now()
  today_date = today_datetime.strftime('%B %d, %Y')
  for chapter in chapters:
    chapter_date = chapter.select_one('.chapterdate').get_text(strip=True)
    if chapter_date == today_date:
      today_chapter_spans.append(chapter)
  return today_chapter_spans

def shelve_chapter(chapter):
  with shelve.open('last_chapter_log') as shelf:
    if chapter.title in shelf:
      del shelf[chapter.title]
    shelf[chapter.title] = chapter
  return 200