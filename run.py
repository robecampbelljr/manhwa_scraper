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

@app.route('/sasura')
def scrape_asura():
  titles = []
  # This will change after link shelve has been implemented
  # The new version will parse the link shelve created by get_url_by_title
  with shelve.open('title_page') as shelf:
    # It will look for the chapter elements in the manhwa's main page
    for title, link in shelf.items():
      # It will log the most recent chapter
      if title == 'Terminally-Ill Genius Dark Knight':
        chapters = site_parser([link], 'div', 'eph-num')
        todays_chapters = filter_by_date(chapters)
        for chapter in todays_chapters:
          print(f"=============\n{chapter}\n================")
      # If the most recent chapter is the same as the last one I read as compared to the last read shelve
        # Then ignore it and alert me somehome
      # elif the chapter is the next chapter (e.g. chapter# == last chapter + 1)
        # Save and display the chapter on the front end linked to the asuratoon chapter
        # Update the last read shelve with the new chapter for that title
  ### Some times AT chapters are numbered with decimals (e.g. 1.1, 1.2, 1.3, etc.)
  ### I will have to work on logic to compensate for that eventually
  ### As of now, that doesn't happen too often so I will not worry about it for v1.0
  return "Asura Scraped Smee!", 200

if __name__ == '__main__':
  app.run(debug=True)