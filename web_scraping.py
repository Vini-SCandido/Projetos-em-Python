import requests
from bs4 import BeautifulSoup

#Aqui é passada uma url que direciona ao site que contem a previsão do tempo, nesse caso G1.
URL = 'https://g1.globo.com/previsao-do-tempo/go/anapolis.ghtml'
page = requests.get(URL)

#site armazena o html a ser analisado
site = BeautifulSoup(page.content, 'html.parser')

# dicionario da previsao. Agrupar o conteudo de cada seção analisada.
previsao = {
    'header': [],
    'forecast': [],
    'details': []
}

#header
header = site.find_all('div', class_='forecast-header') #header recebe todas as 'divs' forecast header
h_classes = ['forecast-header__date', 'forecast-header__place', 'forecast-header__summary'] #classes especificas dentro de forecast header
for h in h_classes:
    for e in header:
        previsao['header'].append(e.find('p', class_=h).text) #anexa o conteudo de h_classes à lista "header" dentro do dicionario previsão.
#Esse raciocínio se aplica ao resto do codigo

#forecast
forecast = site.find_all('div', class_='forecast-today')
f_classes = ['forecast-today__temperature forecast-today__temperature--max', 'forecast-today__temperature forecast-today__temperature--min']
for f in f_classes:
    for e in forecast:
        previsao['forecast'].append(e.find('div', class_=f).text.strip())

#details
details = site.find_all('div', class_='forecast-today-detail')
for t in details:
    table = t.find_all('div', class_='forecast-table__item')
    for i in table:
        previsao['details'].append(i.text.strip())

#Aqui são mostrados os resultados, porém dentro de listas
print(previsao['header'])
print(previsao['forecast'])
print(previsao['details'])
