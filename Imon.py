import numpy as np
import pickle
import pandas as pd
import streamlit as st


st.subheader('Imon International Bank Scoring')

model_selected = st.radio('What analysis do you want to use', ('LogisticRegression', 'DecisionTreeClassifier', 'RandomForestClassifier(without options)',  'RandomForestClassifier(with options)', 'Default'))

if model_selected == 'DecisionTreeClassifier':
    pickle_in = open("ModelTree.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected in ['LogisticRegression', 'Default']:
    pickle_in = open("LogReg.pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(with options)':
    pickle_in = open("Forest(par).pkl","rb")
    classifier=pickle.load(pickle_in)
elif model_selected == 'RandomForestClassifier(without options)':
    pickle_in = open("Forest.pkl","rb")
    classifier=pickle.load(pickle_in)

                     
                     
def predict_note_authentication(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business):
    prediction=classifier.predict([[(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business)]])
    print(prediction)
    return prediction
                     
                     
def main():
    st.title("Imon International's Bank scoring system")
    gend = st.radio('Ваш пол?', ('Мужчина', 'Женщина'))
    if gend=='Мужчина':
        gender=1
    else:
        gender=0
    Issue_amount_nominal = st.number_input('Какова сумма выдочи номинала(используйте только цифры)?', step=1, value=0)
    Term = st.number_input('На какой срок вы хотите кредит?(используйте только цифры)?', step=1, value=0) 
    age = st.number_input('Сколько вам полных лет?(используйте только цифры)?', step=1, value=0)
    family_status = st.radio('Каков ваш семеный статус?', ('Не женат/замужем', 'Разведен(-а)', 'Женат/Замужем', 'Вдова/Вдовец'))
    if  family_status == 'Не женат/замужем':
        Family_status = 0
    elif  family_status == 'Разведен(-а)':
        Family_status = 1
    elif  family_status == 'Женат/Замужем':
        Family_status = 2
    else:
        Family_status = 3
    Type_of_client = st.radio('Какой вы клиент?(0 - Старый клиент, 1 - Новый клиент)', (0, 1))    
    ed = st.selectbox('Какое у вас образование?', ['Среднее образование', 'Высшее образование', 'Неполное Среднее образование',
    'Среднее спец. образование', 'Аспирантура', 'Начальное образование'])
    if ed=='Среднее образование':
        education = 0
    elif ed=='Высшее образование':
         education = 1
    elif ed=='Неполное Среднее образование':
         education = 2
    elif ed=='Среднее спец. образование':
         education = 3
    elif ed=='Аспирантура':
         education = 4
    else:
         education = 5
    Type = st.selectbox('Какой у вас вид бизнеса?', ['Хизматрасони/Услуги', 'Карзи истеъмоли/Потребительский кредит',
 'Савдо / Торговля', 'Истехсолот/Производство', 'Ипотека',
 'Чорводори / Животноводство', 'Хочагии кишлок / Сельское хозяйство']) 
    if Type == 'Хизматрасони/Услуги':
        Type_of_business = 0
    elif Type == 'Карзи истеъмоли/Потребительский кредит':
        Type_of_business = 1
    elif Type == 'Савдо / Торговля':
        Type_of_business = 2
    elif Type == 'Истехсолот/Производство':
        Type_of_business = 3
    elif Type == 'Ипотека':
        Type_of_business = 4 
    elif Type == 'Чорводори / Животноводство':
        Type_of_business = 5   
    else:
        Type_of_business = 0
    
    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Type_of_business)) 
        if result == 0:
            st.success('К сожалению мы не можем выдать вам кредит...(')
        else:
            st.success('Вы можете получить кредит!')
                                      
if __name__=='__main__':
    main()

   
