import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav','rb'))

input_data = [41,0,1,130,204,0,0,172,0,1.4,2,0,2]

# changimg the input data to numpy arrays
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
print("->>>>",input_data_reshaped)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print('The person does not has heart disease')
else:
    print('The person has heart disease')