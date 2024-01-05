from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from utilities.run_utilities import get_titles

app = Flask(__name__)

titles_to_find = ['I Killed an Academy Player', 'Solo Max-Level Newbie', 'My School Life Pretending To Be a Worthless Person']

@app.route('/')
def index():
  return render_template('index.html')

@app.rout('/sasura')
def scrape_asura():
  websites = ['https://asuratoon.com/', 'https://asuratoon.com/page/2', 'https://asuratoon.com/page/3']
  matches = {}
  for url in websites:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      series_divs = soup.find_all('div', class_='luf')
      titles = get_titles(series_divs, titles_to_find)
    else:
      print(f"Unable to retrieve data from {url}")

if __name__ == '__main__':
  app.run(debug=True)