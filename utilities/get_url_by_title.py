from run_utilities import site_parser, filter_titles
import shelve

titles_to_find = ['I Killed an Academy Player', 'Solo Max-Level Newbie', 'My School Life Pretending To Be a Worthless Person', 'The Greatest Estate Developer', 'Revenge of the Iron-Blooded Sword Hound', 'The Max Level Hero has Returned!', 'SSS-Class Suicide Hunter', 'The Reincarnated Assassin is a Genius Swordsman', 'Insanely-Talented Player', 'F-Class Destiny Hunter', 'Terminally-Ill Genius Dark Knight', 'Pick Me Up', 'Infinite Gacha', 'The Tutorial is Too Hard', 'Player Who Can’t Level Up', 'Academy’s Genius Swordmaster', 'The Dark Mage’s Return to Enlistment', 'I’ll Be Taking A Break For Personal Reasons', 'Villain To Kill', 'The Player Hides His Past', 'Standard of Reincarnation', 'Damn Reincarnation', 'Doctor’s Rebirth', 'I Regressed to My Ruined Family', 'Murim Login', 'Reformation of the Deadbeat Noble', 'Swordmaster’s Youngest Son', 'The Lord’s Coins Aren’t Decreasing?!', 'Dr. Player', 'World’s Strongest Troll', 'The Tutorial Tower of the Advanced Player', 'The Hero Returns', 'Legend of Asura – The Venom Dragon']
websites = ['https://asuratoon.com/', 'https://asuratoon.com/page/2', 'https://asuratoon.com/page/3', 'https://asuratoon.com/page/4', 'https://asuratoon.com/page/5']

series_anchors = site_parser(websites, 'a', 'series')
lib = []
# Next step will be if series anchors are truthy,
if series_anchors:
  # Filter all the anchors by the desired titles
  filtered_anchors = filter_titles(series_anchors, titles_to_find)
  # then we will iterate through the list
  for series in filtered_anchors:
    # and extract each link from the anchor and add it to our link shelve with the 'Title: link' format
    link = series.get('href')
    title = series.find('h4').text.strip()
    # Storing "title: link" key value pairs in shelf for persistance and access in other places
    with shelve.open('title_page') as shelf:
      shelf[title] = link
# Then run.py can use the shelve to retrieve titles and links to each individual titles main page
