import pandas as pd
import matplotlib.pyplot as plt

dfhotel = pd.read_csv('http://harve.com.br/praticas/reservashotel.csv')
# print(dfhotel.head())
# print(dfhotel.info())

col1='tipo_de_quarto_reservado'
col2='bebês'

bebes_contingencia = pd.crosstab(dfhotel[col1], dfhotel[col2])

bebes_contingencia.T.plot.barh()


