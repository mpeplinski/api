import requests
from lxml import html
import pandas as pd
from tabulate import tabulate
import math
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
sns.set()
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# pobieranie ze strony xlsx
class Dane():
    ilosc_wierszow = 10
    ilosc_kolumn = 13
r = requests.get('https://stat.gov.pl/download/gfx/portalinformacyjny/pl/defaultaktualnosci/5475/22/5/1/praca_nierejestrowana_wykonywana_w_okesie_od_stycznia_do_wrzesnia_2017.xlsx')

with open('dane.xlsx', 'wb') as f:
    f.write(r.content)
#impot danych kolumn z excel
#surowedane = pd.read_excel('dane.xlsx', sheet_name='Tabl.2.1', skiprows=12, skip_footer=5, usecols='A:G')
ogolem = pd.read_excel('dane.xlsx', sheet_name='Tabl.2.1', skiprows=10, nrows=11, usecols='A:G')
miasto = pd.read_excel('dane.xlsx', sheet_name='Tabl.2.1', skiprows=23, nrows=8, usecols='A:G')
wies = pd.read_excel('dane.xlsx', sheet_name='Tabl.2.1', skiprows=33, nrows=8, usecols='A:G')
#ogolem1 = pd.read_excel('dane.xlsx', sheet_name='Tabl.2.1', skiprows=10, nrows=11, usecols='A:G')

#print('Ogólem \n: ',wies)
#print('Miasto: \n',miasto)
#print('Wies: \n',wies)

print(tabulate(ogolem, headers='keys', tablefmt='psql'))


#convert to csv
ogolem.to_csv(r'./ogolem.csv', sep=',', index = False, header=True)
wies.to_csv(r'./wies.csv', sep=',', index = False, header=True)
miasto.to_csv(r'./miasto.csv', sep=',', index = False, header=True)


# import csv
ogolem_csv = pd.read_csv('ogolem.csv',index_col=0)



#ogolem_dict = ogolem.to_dict('list')
#print(ogolem_dict)
###############################Filtrowanie za pomocą loc i iloc
ogolem_filtr = ogolem_csv.loc['Styczeń':'Wrzesień', :]
ogolem_filtr1 = ogolem_filtr.iloc[:, 1:3]
ogolem_filtr2 = ogolem_filtr.iloc[:, 4:6]
print(tabulate(ogolem_filtr, headers='keys', tablefmt='psql'))

