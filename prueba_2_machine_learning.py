# -*- coding: utf-8 -*-
"""Prueba 2 Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M4_JA44LEVMv2FKGDKjezYpYwuWj8n7i
"""

# importa las librerías a nuestro entorno de trabajo
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

#Upload DataFrame
df1 = pd.read_pickle('Anexo_A.pkl')
df = pd.DataFrame(df1)

#Cortar y Renombrar DataFrame "df"
newdataH= df1.iloc[:45,:]
newData = df1.iloc[46:,:]
newDataV2 = newData.T.reset_index()
newDataV2.columns = newDataV2.columns.to_flat_index().str.join('')
newDataV2['metadataSI'] = pd.to_numeric(newDataV2['metadataSI'])
newDataV2['metadataNO'] = pd.to_numeric(newDataV2['metadataNO'])

#//////////////////////////////////////////
#Medidas de Tendencia Central
#//////////////////////////////////////////
print(' ')
print('Medidas de Tendencia Central')
print(' ')
#----------------------
#metadataNO
#----------------------
print('Variable metadataNO')
#Media
MediaNO = newDataV2['metadataNO'].mean()
print('Media:', MediaNO)
#Mediana
MedianaNO = newDataV2['metadataNO'].median()
print('Mediana:', MedianaNO)
#Moda
ModaNO = newDataV2['metadataNO'].mode()
print('Moda:', ModaNO)
#----------------------
#metadataSI
#----------------------
print(' ')
print('Variable metadataSI')
#Media
MediaSI = newDataV2['metadataSI'].mean()
print('Media:', MediaSI)
#Mediana
MedianaSI = newDataV2['metadataSI'].median()
print('Mediana:', MedianaSI)
#Moda
ModaSI = newDataV2['metadataSI'].mode()
print('Moda:', ModaSI)
#//////////////////////////////////////////
#Medidas de dispersión
#//////////////////////////////////////////

#----------------------
#metadataSI
#----------------------

#Varianza
newDataV2['metadataSI'].var()

#Desviación estándar
newDataV2['metadataSI'].std()

#Cuartiles
newDataV2['metadataSI'].quantile([.25])

#Covarianza
newDataV2.cov()

newDataV2.plot.scatter(x = 'index', y= 'metadataNO')

#Coeficiente de correlación
newDataV2.corr()

#Resumen estadístico
newDataV2.describe()

#----------------------
#metadataNO
#----------------------

#Varianza
newDataV2['metadataNO'].var()

#Desviación estándar
newDataV2['metadataNO'].std()

#Cuartiles
newDataV2['metadataNO'].quantile([.25])

#//////////////////////////////////////////
#Graficos
#//////////////////////////////////////////


#Proyecto de ley, en tercer tramite constitucional, que modifica la ley N°20.551, 
#que regula el cierre de las faenas e instalaciones mineras. Enmiendas que propone 
#aprobar el informe de la Comisión de Minería y Energía.
newdataH[15].hist(bins=25)
newdataH[16].hist(bins=25)
plt.xlabel("Tipo de voto")
plt.ylabel("Cantidad de Votos")
plt.show()

disp=newDataV2.plot(kind='scatter',x='metadataSI', y='metadataNO')

#//////////////////////////////////////////
#Graficos
#//////////////////////////////////////////