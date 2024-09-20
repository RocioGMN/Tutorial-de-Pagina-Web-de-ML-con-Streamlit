import streamlit as st
import joblib
import pandas as pd

# Cargar el modelo desde la ruta especificada
MODEL_PATH = 'models\best_model.pkl'
best_model = joblib.load(MODEL_PATH)

# Título de la aplicación
st.title("Formulario de Datos del Estudiante")

# Crear formulario con Streamlit
with st.form(key='student_form'):
    marital_status = st.text_input('Estado Civil:')
    application_mode = st.text_input('Modo de Aplicación:')
    application_order = st.text_input('Orden de Aplicación:')
    course = st.text_input('Curso:')
    attendance = st.text_input('Horario (Diurno/Nocturno):')
    previous_qualification = st.text_input('Calificación Previa:')
    nationality = st.text_input('Nacionalidad:')
    mother_qualification = st.text_input('Calificación de la Madre:')
    father_qualification = st.text_input('Calificación del Padre:')
    mother_occupation = st.text_input('Ocupación de la Madre:')
    father_occupation = st.text_input('Ocupación del Padre:')
    displaced = st.text_input('Desplazado:')
    educational_needs = st.text_input('Necesidades Educativas Especiales:')
    debtor = st.text_input('Deudor:')
    tuition_up_to_date = st.text_input('Matriculación al Día:')
    gender = st.text_input('Género:')
    scholarship_holder = st.text_input('Becado:')
    age_at_enrollment = st.number_input('Edad al Inscribirse:', min_value=0)
    international = st.text_input('Internacional:')
    units1st_credited = st.number_input('Unidades Acreditadas 1er Semestre:', min_value=0)
    units1st_enrolled = st.number_input('Unidades Inscritas 1er Semestre:', min_value=0)
    units1st_evaluations = st.number_input('Unidades Evaluadas 1er Semestre:', min_value=0)
    units1st_approved = st.number_input('Unidades Aprobadas 1er Semestre:', min_value=0)
    units1st_grade = st.number_input('Nota del Semestre 1:', min_value=0.0)
    units1st_without_evaluations = st.number_input('Unidades sin Evaluación 1er Semestre:', min_value=0)
    units2nd_credited = st.number_input('Unidades Acreditadas 2do Semestre:', min_value=0)
    units2nd_enrolled = st.number_input('Unidades Inscritas 2do Semestre:', min_value=0)
    units2nd_evaluations = st.number_input('Unidades Evaluadas 2do Semestre:', min_value=0)
    units2nd_approved = st.number_input('Unidades Aprobadas 2do Semestre:', min_value=0)
    units2nd_grade = st.number_input('Nota del Semestre 2:', min_value=0.0)
    units2nd_without_evaluations = st.number_input('Unidades sin Evaluación 2do Semestre:', min_value=0)
    unemployment_rate = st.number_input('Tasa de Desempleo:', min_value=0.0)
    inflation_rate = st.number_input('Tasa de Inflación:', min_value=0.0)
    gdp = st.number_input('PIB:', min_value=0.0)

    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    # Recoge todos los datos del formulario y conviértelos al tipo adecuado
    input_dict = {
        'maritalStatus': int(marital_status),
        'applicationMode': int(application_mode),
        'applicationOrder': int(application_order),
        'course': int(course),
        'attendance': int(attendance),
        'previousQualification': int(previous_qualification),
        'nationality': int(nationality),
        'motherQualification': int(mother_qualification),
        'fatherQualification': int(father_qualification),
        'motherOccupation': int(mother_occupation),
        'fatherOccupation': int(father_occupation),
        'displaced': int(displaced),
        'educationalNeeds': int(educational_needs),
        'debtor': int(debtor),
        'tuitionUpToDate': int(tuition_up_to_date),
        'gender': int(gender),
        'scholarshipHolder': int(scholarship_holder),
        'ageAtEnrollment': int(age_at_enrollment),
        'international': int(international),
        'units1stCredited': int(units1st_credited),
        'units1stEnrolled': int(units1st_enrolled),
        'units1stEvaluations': int(units1st_evaluations),
        'units1stApproved': int(units1st_approved),
        'units1stGrade': float(units1st_grade),
        'units1stWithoutEvaluations': int(units1st_without_evaluations),
        'units2ndCredited': int(units2nd_credited),
        'units2ndEnrolled': int(units2nd_enrolled),
        'units2ndEvaluations': int(units2nd_evaluations),
        'units2ndApproved': int(units2nd_approved),
        'units2ndGrade': float(units2nd_grade),
        'units2ndWithoutEvaluations': int(units2nd_without_evaluations),
        'unemploymentRate': float(unemployment_rate),
        'inflationRate': float(inflation_rate),
        'gdp': float(gdp)
    }

    # Convierte el diccionario a DataFrame para facilitar el preprocesamiento
    input_df = pd.DataFrame([input_dict])

    # Realizar la predicción
    prediction = best_model.predict(input_df)

    # Determinar el resultado de la predicción
    result = "Graduado" if prediction[0] == "Graduate" else "Renunciado" if prediction[0] == "Dropout" else "Inscrito"

    # Mostrar el resultado en la interfaz de Streamlit
    st.write(f'Resultado de la Predicción: {result}')

