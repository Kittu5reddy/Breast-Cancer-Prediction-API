import numpy as np
import pandas as pd
import sklearn.datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
breast_cancer_dataset = sklearn.datasets.load_breast_cancer()
data_frame = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)
data_frame['label'] = breast_cancer_dataset.target
X = data_frame.drop(columns='label', axis=1)
Y = data_frame['label']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
model = LogisticRegression()
model.fit(X_train, Y_train)

def predict(s):

  lis=[float(a) for a in s.split(',')]
  input_data =tuple(lis)
  input_data_as_numpy_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
  prediction = model.predict(input_data_reshaped)
  if (prediction[0] == 0):
    return 'The Breast cancer is Malignant (Its cancerous please take the treatement) '
  return 'The Breast Cancer is Benign  (Its not cancerous but be careful)'
