#
#  EU-Road-Safety-Data
#  A Python 3 script to get European Union Road Safety
#  data from Wikipedia and put it into a .csv file
#
#  Article:
#  https://en.wikipedia.org/wiki/Road_safety_in_Europe.
#
#  Data Wrangling Challenge Solution by João Demenech.
#

import requests
import re
import csv
from bs4 import BeautifulSoup as bs


article_url = r'https://en.wikipedia.org/wiki/Road_safety_in_Europe'
caption_text = r'European Union Road Safety Facts and Figures'
filename = r'eu_road_safety_data.csv'
desided_columns_idx = [0, 1, 2, 3, 4, 5, 8] #   ... from the article's table

year = 2018 # The year column should always be 2018


#   Getting page's source code
#   else raise error
print('[*] Getting page\'s source code...')
try:
    res = requests.get(article_url)
    res.raise_for_status()
except requests.RequestException as e:
    raise e


#   Parse the source code with
#   BeautifulSoup
print('[*] Parsing the table')
page_html = bs(res.text, 'html.parser')


#   Finding the table by it's
#   excepted caption
print('[*] Looking for table with caption text "%s"' % caption_text)
table = None
for caption in page_html.find_all('caption'):
    if caption_text in caption.get_text():
        table = caption.find_parent('table', { 'class': 'wikitable' })
        break

if not table:
    raise Exception('Table with caption text "%s" NOT found' % caption_text)

#   Time to parse the table html
#   into a matrix
table_matrix = []
for row_idx, row in enumerate(table.find_all('tr')):
    tmp_row = []
    for col_idx, col in enumerate(row.find_all(['td', 'th'])):
        if col_idx in desided_columns_idx:
            tmp_row.append(col.text.strip())

    #   For each row, the second 
    #   element should be `year`
    tmp_row.insert(1, 'Year' if row_idx is 0 else year)

    table_matrix.append(tmp_row)


#   Let's format the column names
table_matrix[0] = [re.sub('\[.*\]|\\n|in \d+', ' ', header).strip() for header in table_matrix[0]]

#   Let's cast the strings to numbers
for row_idx, row in enumerate(table_matrix[1:]):    #   Ignoring header
    for col_idx, col in enumerate(row[2:]):         #   Ignoring country and year
        number_pieces = re.findall('[\d\.]+', col)
        
        if number_pieces is not None:
            number = ''.join(number_pieces)
        else:
            number = ''

        table_matrix[row_idx + 1][col_idx + 2] = number

#   Sort the data by the last column
data = table_matrix[1:] #   Isolating the data
data.sort(key = lambda row: row[-1])    #   Sorting it
table_matrix[1:] = data #   Putting it back in place

#   Saving the data
print('[*] Saving data in %s' % filename)
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(table_matrix)

print('[*] Done')