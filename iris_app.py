import streamlit as st
import pickle
import time
import pandas as pd

st.set_page_config(page_title='Iris Species Prediction', page_icon='🌸', layout='wide')

st.title("🌸 Iris Species Prediction")
st.write("""
This app predicts the **Iris Species** based on flower measurements.

Data obtained from the [Iris Dataset](https://www.kaggle.com/uciml/iris) by UCIML.
""")

def iris():

    st.sidebar.header('User Input Features')

    uploaded_file = st.sidebar.file_uploader(
        "Upload your input CSV file", type=["csv"]
    )

    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
    else:
        st.sidebar.subheader("Manual Input")

        SepalLengthCm = st.sidebar.slider(
            'Sepal Length (cm)', min_value=4.3, value=6.5, max_value=10.0
        )
        SepalWidthCm = st.sidebar.slider(
            'Sepal Width (cm)', min_value=2.0, value=3.3, max_value=5.0
        )
        PetalLengthCm = st.sidebar.slider(
            'Petal Length (cm)', min_value=1.0, value=4.5, max_value=9.0
        )
        PetalWidthCm = st.sidebar.slider(
            'Petal Width (cm)', min_value=0.1, value=1.4, max_value=5.0
        )

        input_df = pd.DataFrame({
            'SepalLengthCm': [SepalLengthCm],
            'SepalWidthCm': [SepalWidthCm],
            'PetalLengthCm': [PetalLengthCm],
            'PetalWidthCm': [PetalWidthCm]
        })

        st.markdown(
            """
        *Iris Flower*  
        <small>Source: Dutch Grown</small>
        """,
            unsafe_allow_html=True
        )

    if st.sidebar.button("Predict"):

        st.subheader("Input Features")
        st.write(input_df)

        with open("generate_iris.pkl", "rb") as file:
            loaded_model = pickle.load(file)

        prediction = loaded_model.predict(input_df)

        species = {
            0: "Iris-setosa",
            1: "Iris-versicolor",
            2: "Iris-virginica"
        }

        result = species[int(prediction[0])]

        with st.spinner("Predicting..."):
            time.sleep(2)

        st.subheader("Prediction")
        st.success(f"🌸 Predicted Species: **{result}**")

# Langsung tampilkan aplikasi Iris
iris()
