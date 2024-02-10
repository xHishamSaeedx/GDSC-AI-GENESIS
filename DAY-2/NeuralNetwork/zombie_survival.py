# -*- coding: utf-8 -*-
"""zombie_survival.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3-2F0gBwwrxLp2F324vtgZmrG0M6D9y
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder

df = pd.read_csv("/content/zombie_survival_data.csv")

ct = make_column_transformer((MinMaxScaler(), ['Age' , 'Bmi' , 'FamilyMembers' , 'CookingSkill']) ,
 (OneHotEncoder(handle_unknown = "ignore") , ['Gender', 'Location', 'MedicalConditions', 'CanDriveCar', 'CanDriveBike']))


x = df.drop('SurvivalTimeDays' ,axis = 1)
y = df['SurvivalTimeDays']





x = ct.fit_transform(x)

tf.random.set_seed(42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64 , activation = 'relu' , input_dim = x.shape[1]),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(32,activation = 'relu'),
    tf.keras.layers.Dense(1 , activation = 'linear')
])

model.compile(optimizer = 'adam' , loss = 'mean_squared_error')

model.fit(x , y , epochs = 100 , batch_size = 16 , validation_split =0.2)

columns = [
            "Age",
            "Gender",
            "Location",
            "FamilyMembers",
            "Bmi",
            "MedicalConditions",
            "CookingSkill",
            "CanDriveCar",
            "CanDriveBike",
        ]

#
# locations = ["Banjara Hills", "Jubilee Hills", "Mehdipatnam", "Lakdi-ka-pul", "Nampally", "Tolichowki",
#              "Malakpet", "Charminar", "Abids", "Secunderabad", "Begumpet", "Gachibowli", "Himayatnagar", "Dilsukhnagar"]

# medical_conditions = ["None", "Hypertension", "Diabetes", "Asthma", "Allergies", "Heart Disease"]

# genders = ["Male", "Female"]

input = [[20, "Male" , "Malakpet" , 2 , 23 , "None" , 7 ,"Yes" , "Yes"]]

input_df1 = pd.DataFrame(input, columns=columns)

input_df = ct.transform(input_df1)

prediction = model.predict(input_df)

import math


math.ceil(abs(prediction[0,0])*24)