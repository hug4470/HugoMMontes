# app.py

import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo entrenado
with open('../models/train_model_rf.pkl', 'rb') as f:  
    modelo = pickle.load(f)

# Título de la aplicación
st.title('Predicción de Cronificación de la Depresión')

# Descripción de la app
st.write('Ingrese los datos del usuario para hacer predicciones sobre la posibilidad de cronificación de la depresión.')

# Crear formularios de entrada para cada variable
edad = st.number_input('Edad', min_value=0, max_value=120, step=1)
estado_civil = st.selectbox('Estado Civil', ['Single', 'Married', 'Divorced', 'Widowed'])
nivel_educacion = st.selectbox('Nivel de Educación', ['High School', "Bachelor's Degree", "Master's Degree", 'PhD'])
num_hijos = st.number_input('Número de Hijos', min_value=0, max_value=20, step=1)
estado_fumador = st.selectbox('Estado de Fumador', ['Smoker', 'Non-smoker'])
nivel_actividad_fisica = st.selectbox('Nivel de Actividad Física', ['Sedentary', 'Moderate', 'Active'])
estado_empleo = st.selectbox('Estado de Empleo', ['Employed', 'Unemployed'])
ingreso = st.number_input('Ingreso', min_value=0.0, step=500.0)
consumo_alcohol = st.selectbox('Consumo de Alcohol', ['Low', 'Moderate', 'High'])
habitos_dieteticos = st.selectbox('Hábitos Alimenticios', ['Unhealthy', 'Moderate', 'Healthy'])
patrones_suenio = st.selectbox('Patrones de Sueño', ['Poor', 'Fair', 'Good'])
historial_enfermedad_mental = st.selectbox('Historial de Enfermedad Mental', ['Yes', 'No'])
historial_abuso_sustancias = st.selectbox('Historial de Abuso de Sustancias', ['Yes', 'No'])
historial_familiar_depresion = st.selectbox('Historial Familiar de Depresión', ['Yes', 'No'])

# Mapeo de los valores de entrada a numéricos
estado_civil = {'Single': 3, 'Married': 2, 'Divorced': 1, 'Widowed': 0}[estado_civil]
nivel_educacion = {'High School': 0, "Bachelor's Degree": 2, "Master's Degree": 3, 'PhD': 1}[nivel_educacion]
estado_fumador = {'Smoker': 0, 'Non-smoker': 2}[estado_fumador]
nivel_actividad_fisica = {'Sedentary': 0, 'Moderate': 1, 'Active': 2}[nivel_actividad_fisica]
estado_empleo = {'Employed': 1, 'Unemployed': 0}[estado_empleo]
consumo_alcohol = {'Low': 0, 'Moderate': 1, 'High': 2}[consumo_alcohol]
habitos_dieteticos = {'Unhealthy': 0, 'Moderate': 1, 'Healthy': 2}[habitos_dieteticos]
patrones_suenio = {'Poor': 0, 'Fair': 1, 'Good': 2}[patrones_suenio]
historial_enfermedad_mental = 1 if historial_enfermedad_mental == 'Yes' else 0
historial_abuso_sustancias = 1 if historial_abuso_sustancias == 'Yes' else 0
historial_familiar_depresion = 1 if historial_familiar_depresion == 'Yes' else 0

# Botón para hacer la predicción
if st.button('Predecir'):
    # Crear un DataFrame con los datos ingresados
    datos_usuario = pd.DataFrame({
        'Age': [edad],
        'Marital Status': [estado_civil],
        'Education Level': [nivel_educacion],
        'Number of Children': [num_hijos],
        'Smoking Status': [estado_fumador],
        'Physical Activity Level': [nivel_actividad_fisica],
        'Employment Status': [estado_empleo],
        'Income': [ingreso],
        'Alcohol Consumption': [consumo_alcohol],
        'Dietary Habits': [habitos_dieteticos],
        'Sleep Patterns': [patrones_suenio],
        'History of Mental Illness': [historial_enfermedad_mental],
        'History of Substance Abuse': [historial_abuso_sustancias],
        'Family History of Depression': [historial_familiar_depresion]
    })

prediccion = modelo.predict(datos_usuario)
probabilidad = modelo.predict_proba(datos_usuario)[0][1]  # Obtener la probabilidad de cronificación

# Convertir la probabilidad a porcentaje
probabilidad_porcentaje = probabilidad * 100

# Mostrar resultado simplificado
resultado = "Sí" if probabilidad > 0.5 else "No"
st.write(f'Probabilidad de cronificación: {resultado} ({probabilidad_porcentaje:.2f}%)')
