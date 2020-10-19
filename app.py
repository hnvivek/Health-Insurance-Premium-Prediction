import numpy as np
import pandas as pd
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler



# load the model
model = pickle.load(open('model.pkl', 'rb'))
# load the scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))


#st.title('My first app')


def main():
   # st.title("Health Insurance Premium Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:5px">
    <h2 style="color:white;text-align:center;"> Health Insurance Premium Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True) #region
    age = st.text_input("Please enter your age")
    sex = st.selectbox('Select your gender',('Select','Male', 'Female'))
    bmi = st.text_input("Please enter your BMI")
    children = st.text_input(" How many children do you have? ")
    smoker = st.selectbox('Are you a smoker?',('Select','Yes', 'No'))
    region = st.selectbox('Where do you live ?',('Select','North West', 'South East', 'South West'))
    result=0

    if st.button("Predict"):
        NW = 0;
        SE = 0;
        SW = 0
        if sex == 'Male':
            sex_encoded = 1
        else:
            sex_encoded = 0
        if smoker == 'Yes':
            smoker_encoded = 1
        else:
            smoker_encoded = 0
        if region == 'North West':
            NW = 1
        elif region == 'South East':
            SE = 1
        else:
            SW = 1

        print(age + str(sex_encoded) + str(bmi) + str(children) + str(smoker_encoded) + str(NW) + str(SE) + str(SW))
        print(1)
        data = [[float(age),float(sex_encoded),float(bmi),float(children),float(smoker_encoded),float(NW),float(SE),float(SW)]]
        data=np.array(data)
        # transform the test dataset
       # x=scaler.fit([[float(age),float(sex_encoded),float(bmi),float(children),float(smoker_encoded),float(NW),float(SE),float(SW)]])
        X_test_scaled = scaler.fit_transform(data.reshape(8,-1))
        X_test_scaled = X_test_scaled.reshape(-1, 8)


        print(X_test_scaled)
        result=model.predict(X_test_scaled)
    if result != 0:
        st.success('Your Insurance Premium is {}'.format(result))


if __name__=='__main__':
    main()