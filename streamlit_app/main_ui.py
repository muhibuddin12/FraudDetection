from io import BytesIO
import streamlit as st
from models.fraud_input import FraudInput
from services.api_service import get_api_service
import pandas as pd
from services.api_service import ApiService
from services.prediction_service import PredictionService
from utils.file_handler import download_csv
from services.openai_service import PandasAIChatBot
from PIL import Image


def main():

    # Inisialisasi ApiService dengan Dependency Injection
    api_service = get_api_service()
    prediction_service = PredictionService(api_service)
    llm = PandasAIChatBot()


    # Placeholder for the file and prediction
    if 'predictions' not in st.session_state:
        st.session_state['predictions'] = None


    # Judul aplikasi
    st.title("Fraud Transaction Prediction")
    algorithm = st.selectbox("Pilih Fraud Detection Model", ("Random Forest","Logistic Regresion","DecisionTreeClassifier"))
    # Upload file CSV
    uploaded_file = st.file_uploader("Upload a CSV file for prediction", type=["csv"])
    if uploaded_file is not None:
        # Baca file CSV yang diunggah
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data:", data.head())

        # Tombol untuk melakukan prediksi
        if st.button("Predict"):
            # Lakukan prediksi berdasarkan algoritma yang dipilih
            predictions = prediction_service.predict(algorithm, uploaded_file)
            if predictions:
                 # Store predictions in session state
                st.session_state['predictions'] = predictions
                # Tampilkan hasil CSV yang dikembalikan dari API
                st.success("Prediction complete! Download the result below.")

        # Show the download button only if predictions are available
        if st.session_state['predictions'] is not None:
            # Tombol untuk mengunduh file CSV hasil prediksi dengan key unik
            st.download_button(
                label="Download CSV", 
                data=st.session_state['predictions'], 
                file_name="predictions.csv", 
                mime="text/csv",
                key="download_csv_button"  # Adding a unique key to avoid duplicate ID errors
            )
            data =  pd.read_csv(BytesIO(st.session_state['predictions']))

            st.dataframe(data)

            # Show a spinner while waiting for the API response
            with st.spinner('Analyzing data with LLM, please wait...'):
                response = llm.chat_with_dataframe_to_analyse(data, "Analisa data tersebut dan berikan insight dari data tersebut.")
            
            st.write(response)

            prompt_input = st.text_input(label="Prompt")
            button_chat = st.button("Kirim")
            if button_chat:

                with st.spinner('Please wait...'):
                    response = llm.chat_with_dataframe(data,prompt_input)

                # Check if `response` is a DataFrame
                if isinstance(response, pd.DataFrame):
                    # If response is a DataFrame, display it in Streamlit
                    st.write(response)
                elif isinstance(response, str) and response == "/home/muhibuddin/FraudDetection/streamlit_app/exports/charts/temp_chart.png":
                    # If the response is an image file path, open and display the image
                    try:
                        img = Image.open(response)
                        st.image(img, caption="Fraud Detection Chart", use_column_width=True)
                    except Exception as e:
                        st.error(f"Error opening image: {e}")
                else:
                    # Handle unexpected cases
                    st.write(response)


    


if __name__ == "__main__":
    main()
