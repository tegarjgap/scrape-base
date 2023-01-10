import requests
from bs4 import BeautifulSoup

url =  'https://homade.id/menu/'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# https://molekcatering.com/menu/
table_menu = soup.find('table', class_ = 'tablepress tablepress-id-1')
for foods in table_menu.find_all('tbody'):
    rows = foods.find_all('tr')
    for row in rows:
        food_stall =  row.find('td', class_ = 'column-2').text.strip()
        stall_khusus =  row.find('td', class_ = 'column-3').text.strip()
        dessert =  row.find('td', class_ = 'column-4').text.strip()
        dessert_khusus =  row.find('td', class_ = 'column-5').text.strip()
        print(food_stall, "-" , stall_khusus, "-", dessert, "-", dessert_khusus)

# https://homade.id/menu/
for foods in soup.find_all('h3', class_ = 'product-title'):
    menus = foods.find_all('a')
    for menu in menus:
        name = menu.text.strip()
        print(name)

# ref:https://www.youtube.com/watch?v=15f4JhJ8SiQ