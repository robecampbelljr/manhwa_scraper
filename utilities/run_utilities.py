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