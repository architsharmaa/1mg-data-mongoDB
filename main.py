import pandas as pd

from scraper import fetch_data
from mongodb import insert_data


#url = 'https://www.1mg.com/drugs/dolo-650-tablet-74467'
# url = 'https://www.1mg.com/drugs/xtpara-650mg-tablet-391757'

li = []
df = pd.read_csv('urls.csv')
for i in df['url']:
    li.append(fetch_data(i))
    print('one')
print('stage complete')
insert_data(li)

