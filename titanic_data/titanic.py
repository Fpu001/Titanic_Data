import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.text("Titanic passenger data")

df = pd.read_excel('Titanic Data.xlsx') #DataFrame

st.write(df) #magic

##################################################

st.write("Summed fares by sex:")
Fares_by_sex = df.groupby(["Sex"])["Fare"].sum()
Fares_by_sex = round(Fares_by_sex)
st.write(Fares_by_sex)

numbers = [
    22, 38, 26, 35, 35, 54, 2, 27, 14, 4, 58, 20, 39, 14, 55, 2, 31, 35, 34,
    15, 28, 8, 38, 19, 40, 66, 28, 42, 21, 18, 14, 40, 27, 3, 19, 18, 7, 21,
    49, 29, 65, 21, 28, 5, 11, 22, 38, 45, 4, 29, 19, 17, 26, 32, 16, 21,
    26, 32, 25, 1, 30, 22, 29, 28, 17, 33, 16, 23, 24, 29, 20, 46, 26, 59,
    71, 23, 34, 34, 28, 21, 33, 37, 28, 21, 38, 47, 14, 22, 20, 17, 21,
    70, 29, 24, 2, 21, 32, 32, 54, 12, 24, 45, 33, 20, 47, 29, 25, 23,
    19, 37, 16, 24, 22, 24, 19, 18, 19, 27, 9, 37, 42, 51, 22, 55, 40,
    51, 16, 30, 44, 40, 26, 17, 1, 9, 45, 28, 61, 4, 1, 21, 56, 18, 50, 30,
    36, 9, 1, 4, 45, 40, 36, 32, 19, 19, 3, 44, 58, 42, 24, 28, 34, 45, 18,
    2, 32, 26, 16, 40, 24, 35, 22, 30, 31, 27, 42, 32, 30, 16, 27, 51, 38, 22,
    19, 20, 18, 35, 29, 59, 5, 24, 44, 8, 19, 33, 29, 22, 30, 44, 25, 24,
    37, 54, 29, 62, 30, 41, 29, 30, 35, 50, 3, 52, 40, 36, 16, 25, 58, 35, 25,
    41, 37, 63, 45, 7, 35, 65, 28, 16, 19, 33, 30, 22, 42, 22, 26, 19, 36, 24,
    24, 23.5, 2, 50, 19, 1, 17, 30, 30, 24, 18, 26, 28, 43, 26, 24, 54, 31,
    40, 22, 27, 30, 22, 36, 61, 36, 31, 16, 45, 38, 16, 29, 41, 45, 45, 2,
    24, 28, 25, 36, 24, 40, 3, 42, 23, 15, 25, 28, 22, 38, 40, 29, 45, 35, 30,
    60, 24, 25, 18, 19, 22, 3, 22, 27, 20, 19, 42, 1, 32, 35, 18, 1, 36, 17,
    36, 21, 28, 23, 24, 22, 31, 46, 23, 28, 39, 26, 21, 28, 20, 34, 51, 3, 21,
    33, 44, 34, 18, 30, 10, 21, 29, 28, 18, 28, 19, 32, 28, 42, 17, 50, 14, 21,
    24, 64, 31, 45, 20, 25, 28, 4, 13, 34, 5, 52, 36, 30, 49, 29, 65, 50, 48,
    34, 47, 48, 38, 56, 2, 38, 33, 23, 22, 34, 29, 22, 2, 9, 50, 63, 25, 35,
    58, 30, 9, 21, 55, 71, 21, 54, 25, 24, 17, 21, 37, 16, 18, 33, 28, 26, 29,
    36, 54, 24, 47, 34, 36, 32, 30, 22, 44, 41, 50, 39, 23, 2, 17, 30, 7, 45,
    30, 22, 36, 9, 11, 32, 50, 64, 19, 33, 8, 17, 27, 22, 22, 62, 48, 39, 36,
    40, 28, 24, 19, 29, 32, 62, 53, 36, 16, 19, 34, 39, 32, 25, 39, 54, 36, 18,
    47, 60, 22, 35, 52, 47, 37, 36, 49, 49, 24, 44, 35, 36, 30, 27, 22, 40, 39,
    35, 24, 34, 26, 4, 26, 27, 42, 20, 21, 21, 61, 57, 21, 26, 80, 51, 32, 9,
    28, 32, 31, 41, 20, 24, 2, 1, 48, 19, 56, 23, 18, 21, 18, 24, 32, 23,
    58, 50, 40, 47, 36, 20, 32, 25, 43, 40, 31, 70, 31, 18, 24.5, 18, 43, 36,
    27, 20, 14, 60, 25, 14, 19, 18, 15, 31, 4, 25, 60, 52, 44, 49, 42, 18, 35,
    18, 25, 26, 39, 45, 42, 22, 24, 48, 29, 52, 19, 38, 27, 33, 6, 17, 34, 50,
    27, 20, 30, 25, 25, 29, 11, 23, 23, 29, 48, 35, 36, 21, 24, 31, 70, 16,
    30, 19, 31, 4, 6, 33, 23, 48, 1, 28, 18, 34, 33, 41, 20, 36, 16, 51,
    31, 32, 24, 48, 57, 54, 18, 5, 43, 13, 17, 29, 25, 25, 18, 8, 1, 46, 16,
    25, 39, 49, 31, 30, 30, 34, 31, 11, 1, 27, 31, 39, 18, 39, 33, 26, 39
    ]

Cherbourg = [
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",

    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female",
     ]

Queenstown = [ 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male",

    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female",
    ]

Southampton = [
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",  
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male",
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", "male", 
    "male", "male", "male", "male", "male", "male", "male",
    
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female",
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female", "female", "female", "female", "female", "female", "female", "female", 
    "female", "female", "female",
    ]

number = st.number_input(
    "Insert age", numbers.count(""), value=None,  placeholder="Type a number..."
)
st.write("Number of people in selected age: ", numbers.count(number))

Fares_by_Pclass = df.groupby(["Pclass"])["Fare"].sum()
Fares_by_Pclass = round(Fares_by_Pclass)

st.write("Summed Fare by Passenger Class ", Fares_by_Pclass)

result_CM = Cherbourg.count('male')
result_CF = Cherbourg.count('female')

result_QM = Queenstown.count('male')
result_QF = Queenstown.count('female')

result_SM = Southampton.count('male')
result_SF = Southampton.count('female')


embarked = st.radio(
    "City of embarkment",
    ["Cherbourg", "Queenstown", "Southampton"],
)

if embarked == "Cherbourg":
    st.write("Males from Cherbourg: ", result_CM)
    st.write("Females from Cherbourg: ", result_CF)
    
elif embarked == "Queenstown":
    st.write("Males from Queenstown: ", result_QM)
    st.write("Females from Queenstown: ", result_QF)
    
elif embarked == "Southampton":
    st.write("Males from Southampton: ", result_SM)
    st.write("Females from Southampton: ", result_SF)
    



