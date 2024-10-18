import streamlit as st
from schemas.ui_input import FraudInput
from services.api_service import get_api_service

# Inisialisasi ApiService dengan Dependency Injection
api_service = get_api_service()

# Judul aplikasi
st.title("Fraud Transaction Prediction")

# Form untuk input data transaksi
with st.form("fraud_prediction_form"):
    amount = st.number_input("Amount", min_value=0.0, value=1000.0, step=100.0)
    oldbalanceOrg = st.number_input("Old Balance Original", min_value=0.0, value=5000.0, step=100.0)
    newbalanceOrig = st.number_input("New Balance Original", min_value=0.0, value=4000.0, step=100.0)
    oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=10000.0, step=100.0)
    newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=11000.0, step=100.0)

    # Tombol submit untuk prediksi
    submitted = st.form_submit_button("Predict Fraud")

# Proses prediksi ketika tombol submit ditekan
if submitted:
    # Membuat objek FraudInput untuk validasi input
    input_data = FraudInput(
        amount=amount,
        oldbalanceOrg=oldbalanceOrg,
        newbalanceOrig=newbalanceOrig,
        oldbalanceDest=oldbalanceDest,
        newbalanceDest=newbalanceDest
    )
    
    # Mengirim data ke API dan menerima hasil prediksi
    result = api_service.predict_fraud(input_data)
    
    # Tampilkan hasil prediksi
    if "error" in result:
        st.error(result["error"])
    else:
        is_fraud = result["is_fraud"]
        probability = result["probability"]
        
        if is_fraud:
            st.error(f"Fraud detected with probability {probability:.2f}")
        else:
            st.success(f"No fraud detected with probability {probability:.2f}")
