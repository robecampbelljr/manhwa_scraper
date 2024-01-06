from bs4 import BeautifulSoup
import os
import requests
from dotenv import load_dotenv
import shelve

load_dotenv()

titles = os.getenv('TITLES_TO_FIND')
websites = os.getenv('WEBSITES')

for url in websites:
  response = requests.get(url)
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
