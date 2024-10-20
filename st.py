import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('model.sav','rb'))

def diabetes_prdiction(input_data):
    #channing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting dor one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)

    print(prediction)

    if (prediction[0] == 0):
        return 'the preson is not diabetic'
    else:
        return 'the person is diabetic'


def main():
    #giving a title
    st.title('Diabetees prediction ')

    #geting the input data from user						
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the person')

    #code for prediction
    diagnosis = ''

    #creating the button for prediction
    if st.button('Diabetes Test Result '):
        diagnosis = diabetes_prdiction([Pregnancies,Glucose	,BloodPressure,	SkinThickness,Insulin,BMI,DiabetesPedigreeFunction	,Age])
    

    st.success(diagnosis)

if __name__ == '__main__':
    main()

git remote add origin https://github.com/sanjithrana/diabetes-predictions.git
git branch -M main
git push -u origin main