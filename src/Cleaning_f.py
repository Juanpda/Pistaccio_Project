import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt


def Index_date(df,keys):
    df_index = df.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
    return (df_index)

def drop_colums(df,lista):
    DA_dropcol = df.drop(columns=lista)
    return (DA_dropcol)

def get_nans(df,key):
    df_nan = df[key]
    nan_rows = df_nan[df_nan.isnull()]
    return (nan_rows)

def saca_medias(column,dia1,dia2):
    col = column.loc[dia1 : dia2]
    sin_nan = col.dropna(axis=0, how='any', inplace=False)
    puntos = pd.to_numeric([x for x in sin_nan])
    return (puntos.mean())

def to_num(column):
    comas_por_puntos = [str(x).replace(',','.') for x in column];
    A = pd.to_numeric(comas_por_puntos)
    return(A)

def fill_nans(df):
    df1 = df.fillna(method="ffill")
    return(df1)

def get_med(columns,dia1,dia2):
    a = []
    for column in columns:
        a.append(saca_medias(column,dia1,dia2))
    return(a)