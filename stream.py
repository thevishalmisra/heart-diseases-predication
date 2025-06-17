import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

# creating a function for prediction
def heart_desiese_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person does not has heart disease'
    else:
        return 'The person has heart disease'

def main():
    # giving a title
    st.title('Heart Disiese Prediction Web App')
    
    # getting the input data from the user
    #age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall,output
    
    age =      st.text_input('Provide Age')
    sex =      st.text_input('Provide sex')
    cp =       st.text_input('provide cp')
    trtbps =   st.text_input('provide trtbps')
    chol =     st.text_input('provide chol')
    fbs =      st.text_input('provide fbs')
    restecg =  st.text_input('provide restecg')
    thalachh = st.text_input('provide thalachh')
    exng =     st.text_input('provide exng')
    oldpeak =  st.text_input('provide oldpeak')
    slp =      st.text_input('provide slp')
    caa =      st.text_input('provide caa')
    thall =    st.text_input('provide thall')

    data = [
    int(age) if age else 0,  # or a default value
    int(sex) if sex else 0,
    int(cp) if cp else 0,
    int(float(trtbps)) if trtbps else 0.0,
    int(chol) if chol else 0,
    int(fbs) if fbs else 0,
    int(restecg) if restecg else 0,
    int(thalachh) if thalachh else 0,
    int(exng) if exng else 0,
    float(oldpeak) if oldpeak else 0.0,
    int(slp) if slp else 0,
    int(caa) if caa else 0,
    int(thall) if thall else 0
]


    #data = [int(age),sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]
    print('----------------------')
    print(data)
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Hear Disease Test Result'):
        diagnosis = heart_desiese_prediction(data)
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    