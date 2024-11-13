from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import pickle
from sklearn.metrics import recall_score


df_test = pd.read_csv("../data/test/df_test.csv", sep=",")

x_test = df_test.drop(columns=['Target'])
y_test = df_test['Target']


with open('../models/train_model_rf.pkl', 'rb') as archivo:
    modelo_importado = pickle.load(archivo)

    y_pred = modelo_importado.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("Recall: ", recall_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))