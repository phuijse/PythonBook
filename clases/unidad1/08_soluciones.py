# -*- coding: utf-8 -*-
# Ejercicio read_csv

conv = dict.fromkeys(['open', 'close', 'high', 'low', 'next_weeks_open', 'next_weeks_close'], 
                     lambda x: float(x.strip("$")))

df = pd.read_csv("dow_jones_index.data", sep=',', header=0, index_col='date', 
                 converters=conv, parse_dates=[2])
display(df.head(), 
        df.dtypes)

AA_df = df[df["stock"] == "AA"].loc["2011-03-01":"2011-06-01"][["open", "high", "low", "close"]]

# Opcional: Graficando los valores de las acciones
import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(7, 4))
aa_dates_mpl = mdates.date2num(AA_df.index.values)
for date, stock_open, stock_close in zip(aa_dates_mpl, AA_df['open'].values, AA_df['close'].values):
    ax.arrow(x=date, 
             y=stock_open, 
             dx=0., 
             dy=stock_close - stock_open, 
             head_width=2, head_length=0.1, fc='k', ec='k')

ax.fill_between(AA_df.index.values, AA_df['low'].values, AA_df['high'].values, alpha=0.5);
ax.set_ylabel("Precio de las acciones de AA")
fig.autofmt_xdate()

# Ejercicio MultiIndex

df = pd.read_excel("Cantidad-de-Viviendas-por-Tipo.xlsx", 
                   sheet_name=1, # Importamos la segunda hoja (vivienda)
                   usecols=list(range(1, 20)), # Importamos las columnas 1 a 20
                   header=1, # El header está en la segunda fila
                   skiprows=[2], # Eliminamos la fila 2 ya que es invalida
                   index_col='ORDEN' # Usaremos el orden de las comunas como índice
                  ).dropna() # Eliminamos las filas con NaN

df.set_index(["NOMBRE REGIÓN", "NOMBRE PROVINCIA", "NOMBRE COMUNA"], inplace=True)
display(df.head())
idx = pd.IndexSlice
display(df.loc[("LOS RÍOS")],
        df.loc[idx[:, ["RANCO", "OSORNO"], :], :],
        df.loc[idx[:, :, ["VALDIVIA", "FRUTILLAR"]], :])


col_mask = df.columns[4:-1]
display(col_mask)
display(df.loc[idx[:, "VALDIVIA", :], col_mask].head(), 
        df.loc[idx[:, "VALDIVIA", :], col_mask].sum())

"""
Viviendas Particulares Ocupadas con Moradores Presentes                            94771.0
Viviendas Particulares Ocupadas con Moradores Ausentes                              5307.0
Viviendas Particulares Desocupadas (en Venta, para arriendo, Abandonada u otro)     6320.0
Viviendas Particulares Desocupadas\n(de Temporada)                                  6910.0
Viviendas Colectivas                                                                 386.0
"""

# Ejercicio groupby

df = pd.read_excel("Cantidad-de-Viviendas-por-Tipo.xlsx", 
                   sheet_name=1, # Importamos la segunda hoja (vivienda)
                   usecols=list(range(1, 20)), # Importamos las columnas 1 a 20
                   header=1, # El header está en la segunda fila
                   skiprows=[2], # Eliminamos la fila 2 ya que es invalida
                   index_col='ORDEN' # Usaremos el orden de las comunas como índice
                  ).dropna() # Eliminamos las filas con NaN

df.set_index(["NOMBRE REGIÓN", "NOMBRE PROVINCIA", "NOMBRE COMUNA"], inplace=True)

mask = ["Viviendas Particulares Ocupadas con Moradores Presentes",
       "Viviendas Particulares Ocupadas con Moradores Ausentes"]
display(df.groupby(by="NOMBRE REGIÓN", sort=False)[mask].aggregate([np.mean, np.std]).head(5))

def responsables(x):
    #Regiones donde en promedio las comunas tengan una proporcion de viviendas ocupadas(presentes)/total mayor a 85%
    return x[mask[0]]/(x[mask[0]] + x[mask[1]]) > 0.98


display(df.groupby("NOMBRE COMUNA", sort=False).filter(responsables)[mask])

def normalizar(x):
    if x.dtype == np.float:
        return (x - x.mean())/x.std()
    else:
        return x 

display(df.groupby(by="NOMBRE REGIÓN", sort=False)[mask].transform(normalizar).head(10))
