from flask import Flask, render_template
from utilities.run_utilities import filter_titles, site_parser, filter_by_date
import shelve
import os

app = Flask(__name__)

#
#
# 'titles_to_find' and 'websites' will eventually access a shelve created by the get_url_by_title script. For now will leave as blank arrays
titles_to_find = []
websites = []
#
#
#

@app.route('/')
def index():
  return render_template('index.html')

# **** CURRENT IN DEV **** v1.0 is going through the list of desired titles and pulling all the chapters that were published today.

# v2.0 will keep track of the last chapter that I read and the date it was published in a shelf. It will then pull all chapters that have
# been published for that title since the last time I read

class Manhwa:
  def __init__(title, link, chapternum, chapterdate):
    self.title = title
    self.link = link
    self.chapternum = chapternum
    self.chapterdate = chapterdate


from flask import Flask, render_template
from utilities.run_utilities import filter_titles, site_parser, filter_by_date
import shelve
import os

app = Flask(__name__)

#
#
# 'titles_to_find' and 'websites' will eventually access a shelve created by the get_url_by_title script. For now will leave as blank arrays
titles_to_find = []
websites = []
#
#
#

@app.route('/')
def index():
  return render_template('index.html')

# **** CURRENT IN DEV **** v1.0 is going through the list of desired titles and pulling all the chapters that were published today.

# v2.0 will keep track of the last chapter that I read and the date it was published in a shelf. It will then pull all chapters that have
# been published for that title since the last time I read

class Manhwa:
  def __init__(self, title, imglink, link, chapternum, chapterdate):
    self.title = title
    self.imglink = imglink
    self.link = link
    self.chapternum = chapternum
    self.chapterdate = chapterdate


@app.route('/sasura')
def scrape_asura():
  todays_chapters = []
  titles = []
  with shelve.open('title_page') as shelf:
    for title, link in shelf.items():
      chapter_info={}
      # Get all the chapters from the manhwa's main page
      chapters = site_parser([link], 'div', 'eph-num')
      # Pull chapters that were published today
      chapters = filter_by_date(chapters)
      for chapter in chapters:
        chapter_info = Manhwa(title, link, chapter.find('a').get('href'), chapter.find('span', class_='chapternum').get_text(strip=True), chapter.find('span', class_='chapterdate').get_text(strip=True))
        todays_chapters.append(chapter_info)
        # I need to think about storing the Manhwa objects. I might need to refactor, this app takes too long already.
  return render_template('index.html', todays_chapters=todays_chapters)

if __name__ == '__main__':
  app.run(debug=True)

if __name__ == '__main__':
  app.run(debug=True)