# app.py

import streamlit as st
import pandas as pd
import numpy as np
import pickle  # o joblib si prefieres

# Cargar el modelo entrenado
with open('..\models\train_model_rf.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Título de la aplicación
st.title('Aplicación de Predicción de Machine Learning')

# Descripción de la app
st.write('Ingrese los datos del usuario para hacer predicciones basadas en el modelo.')

# Crear formularios de entrada para cada variable
edad = st.number_input('Edad', min_value=0, max_value=120, step=1)
estado_civil = st.selectbox('Estado Civil', ['Single', 'Married', 'Divorced', 'Widowed'])
nivel_educacion = st.selectbox('Nivel de Educación', ['High School', 'Bachelor\'s Degree', 'Master\'s Degree', 'PhD'])
num_hijos = st.number_input('Número de Hijos', min_value=0, max_value=20, step=1)
estado_fumador = st.selectbox('Estado de Fumador', ['Smoker', 'Non-smoker'])
nivel_actividad_fisica = st.selectbox('Nivel de Actividad Física', ['Sedentary', 'Moderate', 'Active'])
estado_empleo = st.selectbox('Estado de Empleo', ['Employed', 'Unemployed'])
ingreso = st.number_input('Ingreso', min_value=0.0, step=500.0)
consumo_alcohol = st.selectbox('Consumo de Alcohol', ['Low', 'Moderate', 'High'])
habitos_dieteticos = st.selectbox('Hábitos Dietéticos', ['Unhealthy', 'Moderate', 'Healthy'])
patrones_suenio = st.selectbox('Patrones de Sueño', ['Poor', 'Fair', 'Good'])
historial_enfermedad_mental = st.selectbox('Historial de Enfermedad Mental', ['Yes', 'No'])
historial_abuso_sustancias = st.selectbox('Historial de Abuso de Sustancias', ['Yes', 'No'])
historial_familiar_depresion = st.selectbox('Historial Familiar de Depresión', ['Yes', 'No'])

# Mapeo de los valores de entrada a numéricos
mapeo_estado_civil = {'Single': 3, 'Married': 2, 'Divorced': 1, 'Widowed': 0}
mapeo_nivel_educacion = {'High School': 0, 'Bachelor\'s Degree': 2, 'Master\'s Degree': 3, 'PhD': 1}
mapeo_estado_fumador = {'Smoker': 0, 'Non-smoker': 2}
mapeo_nivel_actividad_fisica = {'Sedentary': 0, 'Moderate': 1, 'Active': 2}
mapeo_estado_empleo = {'Employed': 1, 'Unemployed': 0}
mapeo_consumo_alcohol = {'Low': 0, 'Moderate': 1, 'High': 2}
mapeo_habitos_dieteticos = {'Unhealthy': 0, 'Moderate': 1, 'Healthy': 2}
mapeo_patrones_suenio = {'Poor': 0, 'Fair': 1, 'Good': 2}
mapeo_booleano = {'Yes': 1, 'No': 0}

# Botón para hacer la predicción
if st.button('Predecir'):
    # Crear un DataFrame con los datos ingresados y transformados
    datos_usuario = pd.DataFrame({
        'Age': [edad],
        'Marital Status': [mapeo_estado_civil[estado_civil]],
        'Education Level': [mapeo_nivel_educacion[nivel_educacion]],
        'Number of Children': [num_hijos],
        'Smoking Status': [mapeo_estado_fumador[estado_fumador]],
        'Physical Activity Level': [mapeo_nivel_actividad_fisica[nivel_actividad_fisica]],
        'Employment Status': [mapeo_estado_empleo[estado_empleo]],
        'Income': [np.log(ingreso + 1)],  # Transformación logarítmica para el ingreso
        'Alcohol Consumption': [mapeo_consumo_alcohol[consumo_alcohol]],
        'Dietary Habits': [mapeo_habitos_dieteticos[habitos_dieteticos]],
        'Sleep Patterns': [mapeo_patrones_suenio[patrones_suenio]],
        'History of Mental Illness': [mapeo_booleano[historial_enfermedad_mental]],
        'History of Substance Abuse': [mapeo_booleano[historial_abuso_sustancias]],
        'Family History of Depression': [mapeo_booleano[historial_familiar_depresion]]
    })

    # Realizar la predicción
    prediccion = modelo.predict(datos_usuario)
    st.write(f'La predicción del modelo es: {prediccion[0]}')

# Ejecución
if __name__ == '__main__':
    st.write('¡Listo para predecir!')
