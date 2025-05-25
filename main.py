from joblib import load
import numpy as np
model=load('model/model.joblib')

def predict(s):
  lis=[float(a) for a in s.split(',')]
  input_data =tuple(lis)
  input_data_as_numpy_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
  prediction = model.predict(input_data_reshaped)
  if (prediction[0] == 0):
    return 'The Breast cancer is Malignant (Its cancerous please take the treatement) '
  return 'The Breast Cancer is Benign  (Its not cancerous but be careful)'
