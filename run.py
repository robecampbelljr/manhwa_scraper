from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from utilities.run_utilities import filter_titles
import shelve
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
titles_to_find = os.getenv('TITLES_TO_FIND')
websites = os.getenv('WEBSITES')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sasura')
def scrape_asura():
  titles = []
  for url in websites:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      series_divs = soup.find_all('div', class_='luf')
      titles = filter_titles(series_divs, titles_to_find)
      for title in titles:
        print(f"{title}")
        print("====================================================")
    else:
      print(f"Unable to retrieve data from {url}")
  return "Asura Scraped Smee!", 200

if __name__ == '__main__':
  app.run(debug=True)