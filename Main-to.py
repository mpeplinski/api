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
