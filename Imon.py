import streamlit as st
import pickle

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

def predict_score(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business, model):
    prediction = model.predict([[gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business]])[0]
    return prediction

def main():
    st.title("Imon International's Bank Scoring System")
    gender = st.radio('Ваш пол?(0 - мужской, 1 - женский)', (0, 1))
    Issue_amount_nominal = st.number_input('Сумма выдачи номинал (только числа)', step=1, value=0)
    Term = st.number_input('Срок кредита (только числа)', step=1, value=0) 
    age = st.number_input('Возраст (только числа)', step=1, value=0)
    Family_status = st.radio('Семейное положение (0 - вдовец/вдова, 1 - холост/не замужем, 2 - женат/замужем, 3 - разведен(а))', (0, 1, 2, 3))
    Type_of_client = st.radio('Тип клиента (0 - старый клиент, 1 - новый клиент)', (0, 1))    
    education = st.radio('Образование (0 - высшее, 1 - среднее специальное, 2 - среднее, 3 - неполное среднее, 4 - начальное, 5 - аспирантура)', (0, 1, 2, 3, 4, 5))
    Tupe_of_business = st.radio('Вид бизнеса (0 - 1. Потребительский кредит, 1 - 2. Производство, 2 - 6. Сельское хозяйство, 3 - 3. Услуги, 4 - 4. Торговля)', (0, 1, 2, 3, 4)) 
    
    if loaded_model:
        prediction = predict_score(gender, Issue_amount_nominal, Term, age, Family_status, Type_of_client, education, Tupe_of_business, loaded_model)
        if st.button("Предсказать"):
            st.success(f'Результат скоринговой системы: {prediction}')
    else:
        st.warning("Выберите модель для загрузки.")

if __name__ == '__main__':
    main()
