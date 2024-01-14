from flask import Flask, render_template
from utilities.run_utilities import filter_titles, site_parser, shelve_chapter, filter_by_date
import shelve
import os
from utilities.run_utilities import Manhwa

app = Flask(__name__)

# **** CURRENT IN DEV **** v1.0 is going through the list of desired titles and pulling all the chapters that were published today.

# v2.0 will keep track of the last chapter that I read and the date it was published in a shelf. It will then pull all chapters that have
# been published for that title since the last time I read

@app.route('/')
def index():
  todays_chapters = []
  titles = []
  with shelve.open('title_page') as shelf:
    for title, link in shelf.items():
      # Get all the chapters from the manhwa's main page
      chapters = site_parser([link], 'div', 'eph-num')
      # Pull chapters that were published today
      chapters = filter_by_date(chapters)
      for chapter in chapters:
        # Switched to class to eventually save in a shelve
        shelve_chapter(chapter)
  return render_template('index.html', todays_chapters=todays_chapters)

if __name__ == '__main__':
  app.run(debug=True)