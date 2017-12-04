# Extracción de una página web de información

import urllib3
from bs4 import BeautifulSoup
import pandas as pd

# Obtención de la página web
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
response = http.request('GET', wiki)

# Procesamos para obtener la tabla
soup = BeautifulSoup(response.data.decode('utf-8'), "lxml")
right_table=soup.find('table', class_='wikitable sortable plainrowheaders')

# Definimos en una única linea 7 listas vacías
A, B, C, D, E, F, G = [[] for _ in range(7)]

# Poblamos con el contenido de la tabla
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells)==6:
        B.append(states[0].find(text=True))
        for v, w in zip([A, C, D, E, F, G], range(6)):
            v.append(cells[w].find(text=True))

# Construimos un Data Frame
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']= F
df['Former_Capital']=G

# Resolvemos el problema de las columna `Year_Capital`
df[['Year_Capital']] = df[['Year_Capital']].apply(pd.to_numeric, errors='raise')

# Seleccionamos un subset
result = df.query('Year_Capital > 1930 and  Year_Capital < 1960')

# Y lo exportamos en CSV (estilo Excel)

result.to_csv('data.csv', sep=';', encoding='utf-8')
