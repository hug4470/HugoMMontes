import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/raw/dataset.csv/depression_data.csv')

def procesado(df):
    df['History of Mental Illness'] = df['History of Mental Illness'].replace({'Yes': 1, 'No': 0})
    df['Family History of Depression'] = df['Family History of Depression'].replace({'Yes': 1, 'No': 0})
    df['History of Substance Abuse'] = df['History of Substance Abuse'].replace({'Yes': 1, 'No': 0})
    df['Physical Activity Level'] = df['Physical Activity Level'].replace({'Active': 2, 'Sedentary' : 0, 'Moderate': 1})
    df['Smoking Status'] = df['Smoking Status'].replace({'Non-smoker': 2, 'Current' : 0, 'Former': 1})
    df['Alcohol Consumption'] = df['Alcohol Consumption'] .replace({'Low': 0, 'Moderate' : 1, 'High': 2})
    df['Dietary Habits'] = df['Dietary Habits'].replace({'Unhealthy': 0, 'Moderate' : 1, 'Healthy': 2})
    df['Sleep Patterns'] = df['Sleep Patterns'].replace({'Poor': 0, 'Fair' : 1, 'Good': 2})
    df['Income'] = np.log(df['Income'])
    df['Marital Status'] = df['Marital Status'].replace({'Widowed': 0, 'Divorced' : 1, 'Married': 2, 'Single' : 3})
    df['Education Level'] = df['Education Level'].replace({'High School': 0,'Associate Degree': 1,'Bachelor\'s Degree': 2,'Master\'s Degree': 3,'PhD': 4})
    df['Employment Status'] = df['Employment Status'].replace({'Unemployed': 0, 'Employed' : 1})
    df.drop(columns = 'Name', inplace = True)
    df['Target'] = df['Chronic Medical Conditions'].replace({'Yes': True, 'No': False})
    df.drop(columns='Chronic Medical Conditions', inplace = True)

    return df

df_procesado = procesado(df)

df_procesado.to_csv('../data/processed/df_procesado.csv')