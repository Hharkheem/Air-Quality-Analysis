# import streamlit as st
# import pickle

# # loading the model
# @st.cache_data
# def load_model():
#     with open('AQModel.pkl', 'rb') as f:
#         model = pickle.load(f)
#     return model

# def main():
#     st.title("AIR QUALITY PREDICTION")

#     # Input fields for features
#     input_fields = {
#         'CO(GT)': 'Concentration of Carbon Monoxide (CO) measured in mg/m^3',
#         'PT08.S1(CO)': 'Sensor measurement for CO',
#         'NMHC(GT)': 'Non-Methane Hydrocarbons concentration in µg/m^3',
#         'PT08.S2(NMHC)': 'Sensor measurement for Non-Methane Hydrocarbons',
#         'NOx(GT)': 'Concentration of Nitrogen Oxides (NOx) measured in ppb',
#         'PT08.S3(NOx)': 'Sensor measurement for NOx',
#         'NO2(GT)': 'Concentration of Nitrogen Dioxide (NO2) measured in ppb',
#         'PT08.S5(O3)': 'Sensor measurement for Ozone (O3)',
#         'T': 'Temperature in degrees Celsius (°C)',
#         'RH': 'Relative Humidity in percentage (%)',
#         'AH': 'Absolute Humidity in gm/m^3'
#     }

#     for feature, _ in input_fields.items():
#         input_fields[feature] = st.number_input(feature + ': ')

#     # Load model
#     model = load_model()

#     # Predict button
#     if st.button("PREDICT"):
#         # Prepare input for prediction
#         input_data = [input_fields[feature] for feature in input_fields.keys()]
#         # Make prediction
#         result = model.predict([input_data])
#         st.write(f"C6H6(GT): {result}")

# if __name__ == '__main__':
#     main()





import streamlit as st
import pickle

# loading the model
@st.cache_data
def load_model():
    with open('AQModel.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def main():
    st.title("AIR QUALITY PREDICTION")

    # Input fields for features
    co_gt = st.number_input('Concentration of Carbon Monoxide (CO) measured in mg/m^3', format="%.5f")
    pt08_s1_co = st.number_input('Sensor measurement for CO', format="%.5f")
    nmhc_gt = st.number_input('Non-Methane Hydrocarbons concentration in µg/m^3', format="%.5f")
    pt08_s2_nmhc = st.number_input('Sensor measurement for Non-Methane Hydrocarbons', format="%.5f")
    nox_gt = st.number_input('Concentration of Nitrogen Oxides (NOx) measured in ppb', format="%.5f")
    pt08_s3_nox = st.number_input('Sensor measurement for NOx', format="%.5f")
    no2_gt = st.number_input('Concentration of Nitrogen Dioxide (NO2) measured in ppb', format="%.5f")
    pt08_s5_o3 = st.number_input('Sensor measurement for Ozone (O3)', format="%.5f")
    t = st.number_input('Temperature in degrees Celsius (°C)', format="%.5f")
    rh = st.number_input('Relative Humidity in percentage (%)', format="%.5f")
    ah = st.number_input('Absolute Humidity in gm/m^3', format="%.5f")

    # Load model
    model = load_model()

    # Predict button
    if st.button("PREDICT"):
        # Prepare input for prediction
        input_data = [
            co_gt,
            pt08_s1_co,
            nmhc_gt,
            pt08_s2_nmhc,
            nox_gt,
            pt08_s3_nox,
            no2_gt,
            pt08_s5_o3,
            t,
            rh,
            ah
        ]
        # Make prediction
        result = model.predict([input_data])
        st.write(f"The Benzene component of the atmosphere C6H6(GT) is: {result[0]:.3f}(µg/m^3)")

if __name__ == '__main__':
    main()
