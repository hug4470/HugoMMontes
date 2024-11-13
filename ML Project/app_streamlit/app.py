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
st.write('Según estos datos, trataremos de predecir si está usted en riesgo de que pueda cronificarse su depresión, en caso de desarrollarla.')

# Crear formularios de entrada para cada variable
st.write('Introduzca su edad')
edad = st.number_input('Edad', min_value=0, max_value=120, step=1)
st.write('Seleccione su estado civil')
estado_civil = st.selectbox('Estado Civil', ['Soltero', 'Casado', 'Divorciado', 'Enviudado'])
st.write('Seleccione su nivel de educación')
nivel_educacion = st.selectbox('Nivel de Educación', ['Secundaria/Elemental', "Graduado", "Post-universitario", 'Doctorado'])
st.write('Introduzca el número de hijos que tenga')
num_hijos = st.number_input('Número de Hijos', min_value=0, max_value=20, step=1)
st.write('Introduzca sus ingresos ANUALES')
ingreso = st.number_input('Ingreso', min_value=0.0, step=500.0)  # Agregada entrada de ingreso
st.write('Marque la casilla si es fumador')
estado_fumador = st.checkbox('Fumador')
st.write('Marque la casilla si está trabajando actualmente')
estado_empleo = st.checkbox('Empleado')

# Opciones de actividad física, alcohol, dieta y sueño con checkbox y claves únicas
st.write('Seleccione su nivel de Actividad Física:')
actividad_fisica = {
    'Sedentary': st.checkbox('Sedentario', key='act_sedentary'),
    'Moderate': st.checkbox('Moderado', key='act_moderate'),
    'Active': st.checkbox('Activo', key='act_active')
}
nivel_actividad_fisica = max(actividad_fisica, key=actividad_fisica.get)

st.write('Seleccione su consumo de Alcohol:')
consumo_alcohol = {
    'Low': st.checkbox('Ninguno', key='alc_low'),
    'Moderate': st.checkbox('Ocasional', key='alc_moderate'),
    'High': st.checkbox('Habitual', key='alc_high')
}
nivel_consumo_alcohol = max(consumo_alcohol, key=consumo_alcohol.get)

st.write('Indique sus hábitos alimentarios:')
habitos_dieta = {
    'Unhealthy': st.checkbox('Insanos', key='diet_unhealthy'),
    'Moderate': st.checkbox('Regulares', key='diet_moderate'),
    'Healthy': st.checkbox('Adecuados', key='diet_healthy')
}
nivel_dieta = max(habitos_dieta, key=habitos_dieta.get)

st.write('Indique sus hábitos del sueño:')
patrones_sueno = {
    'Poor': st.checkbox('Pobre', key='sleep_poor'),
    'Fair': st.checkbox('Regular', key='sleep_fair'),
    'Good': st.checkbox('Bueno', key='sleep_good')
}
nivel_sueno = max(patrones_sueno, key=patrones_sueno.get)

st.write('Marque las casillas correspondientes a sus antecedentes, en caso de tenerlos.')

# Historiales como checkbox con claves únicas
historial_enfermedad_mental = st.checkbox('Antecedentes de Enfermedad Mental', key='hist_mental')
historial_abuso_sustancias = st.checkbox('Antecedentes de Abuso de Sustancias', key='hist_abuse')
historial_familiar_depresion = st.checkbox('Antecedentes Familiares de Depresión', key='hist_family_depression')

# Mapeo de los valores de entrada a numéricos
estado_civil = {'Single': 3, 'Married': 2, 'Divorced': 1, 'Widowed': 0}[estado_civil]
nivel_educacion = {'High School': 0, "Bachelor's Degree": 2, "Master's Degree": 3, 'PhD': 1}[nivel_educacion]
estado_fumador = 1 if estado_fumador else 0
estado_empleo = 1 if estado_empleo else 0
nivel_actividad_fisica = {'Sedentary': 0, 'Moderate': 1, 'Active': 2}[nivel_actividad_fisica]
nivel_consumo_alcohol = {'Low': 0, 'Moderate': 1, 'High': 2}[nivel_consumo_alcohol]
nivel_dieta = {'Unhealthy': 0, 'Moderate': 1, 'Healthy': 2}[nivel_dieta]
nivel_sueno = {'Poor': 0, 'Fair': 1, 'Good': 2}[nivel_sueno]
historial_enfermedad_mental = 1 if historial_enfermedad_mental else 0
historial_abuso_sustancias = 1 if historial_abuso_sustancias else 0
historial_familiar_depresion = 1 if historial_familiar_depresion else 0

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
        'Alcohol Consumption': [nivel_consumo_alcohol],
        'Dietary Habits': [nivel_dieta],
        'Sleep Patterns': [nivel_sueno],
        'History of Mental Illness': [historial_enfermedad_mental],
        'History of Substance Abuse': [historial_abuso_sustancias],
        'Family History of Depression': [historial_familiar_depresion]
    })

    # Realizar la predicción
    prediccion = modelo.predict(datos_usuario)
    probabilidad = modelo.predict_proba(datos_usuario)[0][1]  # Obtener la probabilidad de cronificación

    # Convertir la probabilidad a porcentaje
    probabilidad_porcentaje = probabilidad * 100

    # Mostrar resultado simplificado
    resultado = "Sí" if probabilidad > 0.5 else "No"
    st.write(f'Probabilidad de cronificación: {resultado} ({probabilidad_porcentaje:.2f}%)')
