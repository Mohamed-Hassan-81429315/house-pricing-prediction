import streamlit as st
import pickle
import pandas as pd



model = pickle.load(open('Housing_model.pkl', 'rb'))
scaler = pickle.load(open('Housing_scaler.pkl', 'rb'))

# try:
#     st.success("xgboost is successfully imported!")
# except ModuleNotFoundError:
#     st.error("xgboost is NOT installed!")

st.title("Housing Prices Prediction\n Tell Me about the details of your House")

area = st.number_input("Area Of The House", step=1.0 , min_value=1.0)
bedrooms = st.number_input("Number of Bedrooms", step=1.0 , min_value=1.0)
bathrooms = st.number_input("Number of Bathrooms", step=1.0 , min_value=1.0)
stories = st.number_input("Number of Stories", step=1.0 , min_value=1.0)
mainroad = st.selectbox("Has Mainroad ?",options=["Yes" , "No"])
mainroad = 1 if mainroad == "Yes" else 0
guestroom = st.selectbox("Contains Guestroom ? ", options=["Yes" , "No"])
guestroom = 1 if guestroom == "Yes" else 0
basement = st.selectbox("Has Basement ? ",options=["Yes" , "No"])
basement = 1 if basement == "Yes" else 0
airconditioning = st.selectbox("Contains Air Conditioning ?",options=["Yes" , "No"])
airconditioning = 1 if airconditioning == "Yes" else 0
parking = st.number_input("Number of Parking Spaces", step=1.0 , min_value=0.0)
prefarea = st.selectbox("Has Preferred Area ?",options=["Yes" , "No"])
prefarea = 1 if prefarea == "Yes" else 0
furnishingstatus = st.selectbox("Status of the Home",options= ["furnished", "semi-furnished", "unfurnished"])
furnishing_map = {"furnished": 0, "semi-furnished": 1, "unfurnished": 2}
furnishingstatus = furnishing_map[furnishingstatus]

if st.button("Predict The Housing Price"):
    input_data = pd.DataFrame([{
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "airconditioning": airconditioning,
        "parking": parking,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus
    }])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled) 

    st.success(f" The Predicted Home Price is ->  {prediction[0]:,.2f}$ ")