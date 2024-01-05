from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
from utilities.run_utilities import get_titles

app = Flask(__name__)

@app.route('/')
def index():
  websites = ['https://asuratoon.com/']
  titles_to_find = ['I Killed an Academy Player', 'Solo Max-Level Newbie']
  matches = {}
  for url in websites:
    response = requests.get(url)
    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')
      series_divs = soup.find_all('div', class_='luf')
      titles = get_titles(series_divs, titles_to_find)
      print(titles)
    else:
      print(f"Unable to retrieve data from {url}")
  return render_template('index.html', matches=matches)

if __name__ == '__main__':
  app.run(debug=True)