import datetime as dt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st
import json as js
import csv

def segmento1(name):
    #Se lee el archivo csv
    frame = pd.read_csv(name,',')
    #Se purga la base para obtener explusivamente los usuarios de sonora y se almacena en otra variable
    frame = frame[frame['ENTIDAD_RES'] == 26].copy()
    #Se mantienen unicamente las columnas necesarias
    frame = frame[['FECHA_SINTOMAS', 'ID_REGISTRO', 'FECHA_DEF']].copy()
    #Se mantienen unicamente las columnas necesarias
    frame["FECHA_DEF"].replace({"9999-99-99": ''}, inplace=True)
    #Se les da formato a los años para poder trabajar con ellos
    frame['FECHA_SINTOMAS'] = pd.to_datetime(frame['FECHA_SINTOMAS'].astype(str), format='%Y/%m/%d')
    frame['FECHA_DEF'] = pd.to_datetime(frame['FECHA_DEF'].astype(str), format='%Y/%m/%d')
    #Se Agrupan por fecha y se obtiene el conteo
    final = frame.groupby(['FECHA_SINTOMAS'], as_index=False).count()
    #Se crea el csv
    final.to_csv('tabla1.csv', index=False)















if __name__ == '__main__':
    segmento1('examen-prog/covid-data/200511COVID19MEXICO.csv')


