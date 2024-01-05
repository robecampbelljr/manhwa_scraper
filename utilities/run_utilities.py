def get_titles(series_anchors, titles_to_search_for):
  print("Title utility sucessfully called")
  lib = []
  for a in series_anchors:
    title_element = a.find('h4')
    if title_element:
      title = title_element.text.strip()
      for search_title in titles_to_search_for:
        if title == search_title:
          lib.append(a)
  return lib