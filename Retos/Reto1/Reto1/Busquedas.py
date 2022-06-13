import pandas as pd
import dateutil


def formato(df):
    df_format = df['FECHA_CORTE'] = df['FECHA_CORTE'].apply(dateutil.parse.parse)
    return df_format
