import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle


df_procesado = pd.read_csv('../data/processed/df_procesado.csv', index_col=0)

def modelo_entreno(df):
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=42)
    train_df.to_csv('../data/train/df_train.csv', index=False)
    test_df.to_csv('../data/test/df_test.csv', index=False)

    df_train = pd.read_csv("../data/train/df_train.csv", sep=",") 
    
    x = df_train.drop(columns=['Target'])  
    y = df_train['Target']   
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    smote = SMOTE(random_state=42)
    x_resampled, y_resampled = smote.fit_resample(x_train, y_train)

    minmax_scaler = MinMaxScaler()
    minmax_scaler.fit(x_train)
    x_train_scaled = minmax_scaler.transform(x_train)
    x_test_scaled = minmax_scaler.transform(x_test)

    random_forest_model = RandomForestClassifier(
        n_estimators=150,       
        max_depth=40,           
        min_samples_split=4,  
        min_samples_leaf=4,   
        class_weight='balanced',
        random_state=42         
    )
    random_forest_model.fit(x_train, y_train)

    return random_forest_model

random_forest_model = modelo_entreno(df_procesado)

with open('../models/train_model_rf.pkl', 'wb') as archivo:
    pickle.dump(random_forest_model, archivo)