import numpy as np
import pickle
import pandas as pd
import streamlit as st

st.subheader('Imon International Bank Scoring')

model_selected = st.radio('What analysis do you want to use', ('LogisticRegression', 'DecisionTreeClassifier', 'RandomForestClassifier(without options)', 'RandomForestClassifier(with options)', 'Default'))

def load_model(model_name):
    try:
        if model_name == 'DecisionTreeClassifier':
            with open("ModelTree.pkl", "rb") as pickle_in:
                return pickle.load(pickle_in)
        elif model_name in ['LogisticRegression', 'Default']:
            with open("LogReg.pkl", "rb") as pickle_in:
                return pickle.load(pickle_in)
        elif model_name == 'RandomForestClassifier(with options)':
            with open("Forest(par).pkl", "rb") as pickle_in:
                return pickle.load(pickle_in)
        elif model_name == 'RandomForestClassifier(without options)':
            with open("Forest.pkl", "rb") as pickle_in:
                return pickle.load(pickle_in)
    except FileNotFoundError:
        st.error("Model file not found")
        return None

def predict_note_authentication(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business, classifier):
    try:
        prediction = classifier.predict(np.array([[gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business]]))
        return prediction
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None

def main():
    st.title("Imon International's Bank scoring system")
    classifier = load_model(model_selected)
    if classifier is None:
        return
    
    gender = st.radio('Ваш пол?(0 - male, 1 - female)', (0, 1))
    Issue_amount_nominal = st.number_input('Какова сумма выдочи номинала(используйте только цифры)?', step=1, value=0)
    Term = st.number_input('На какой срок вы хотите кредит?(используйте только цифры)?', step=1, value=0) 
    age = st.number_input('Сколько вам полных лет?(используйте только цифры)?', step=1, value=0)
    Family_status = st.radio('Каков ваш семеный статус?(0 - Widow/Widower, 1 - Single, 2 - Married, 3 - Divorced)', (0, 1, 2, 3))
    Type_of_client = st.radio('Какой вы клиент?(0 - Старый клиент, 1 - Новый клиент)', (0, 1))    
    education = st.radio('Какое у вас образование?(0 - Высшее образование, 1 - Сред.спец.образ-ние, 2 - Среднее образование, 3 - Непол Сред.образ, 4 - Начал образование, 5 - Аспирантура)', (0, 1, 2, 3, 4, 5))
    Tupe_of_business = st.radio('Какой у вас вид бизнеса?(0 - 1. Карзи истеъмоли/Потребительский кредит, 1 - 2. Истехсолот/Производство, 2 - 6. Хочагии кишлок / Сельское хозяйство, 3 - 3. Хизматрасони/Услуги, 4 - 4. Савдо / Торговля)', (0, 1, 2, 3, 4)) 
                     
   result = ""
    if st.button("Predict"):
        prediction = predict_note_authentication(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business, classifier)
        if prediction is not None:
            result = int(prediction[0])
    
    st.success(f'Scoring system result is {result}')

if __name__ == '__main__':
    main()

   
