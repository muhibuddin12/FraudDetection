# Fraud Detection API

## 📚 Project Overview

This project aims to build a **Fraud Detection API** that uses machine learning to predict fraudulent transactions based on input data. The API is built using **FastAPI**, and the machine learning model is a **Random Forest Classifier** trained with transaction data. The goal is to provide a reliable way to identify potential fraud cases and assist in fraud prevention efforts.

Additionally, a **Streamlit** interface is provided for easy interaction with the model through a web-based UI.

### 🌟 Features
- **FastAPI**-based API for fraud detection.
- **Random Forest** machine learning model for fraud prediction.
- **Streamlit** interface for user-friendly interaction.
- Easy-to-use and scalable solution for identifying fraudulent transactions.

## 🛠️ Installation

Follow these steps to install the project and set it up in your local environment.

### 1. **Clone the repository**

First, clone this repository to your local machine:

```bash
git clone https://github.com/username/FraudDetection.git
```

Navigate to the project directory:

```bash
cd FraudDetection
```

### 2. **Set up Virtual Environment**

Create and activate a virtual environment (optional but recommended):

- **Linux/macOS**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

- **Windows**:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

### 3. **Install Required Dependencies**

Install the required Python packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. **Set up Environment Variables**

Create a `.env` file in the root directory to store any environment-specific configurations. For example:

```
API_KEY=your-api-key-here
MODEL_PATH=models/random_forest_model.pkl
```

Make sure to customize the file according to your project's needs.

## 🚀 Running the Application

### 1. **Running the FastAPI Server**

To run the FastAPI server, use **Uvicorn**. It will serve the Fraud Detection API:

```bash
uvicorn app.main:app --reload
```

By default, the API will be available at:

```
http://127.0.0.1:8000
```

You can visit the automatically generated API documentation provided by FastAPI at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 2. **Example API Request**

You can test the API by sending a POST request to the `/predict_fraud` endpoint with transaction data:

```json
{
  "amount": 1000.0,
  "oldbalanceOrg": 5000.0,
  "newbalanceOrig": 4000.0,
  "oldbalanceDest": 10000.0,
  "newbalanceDest": 11000.0
}
```

You will receive a response similar to this:

```json
{
  "is_fraud": false,
  "probability": 0.85
}
```

## 🌐 Running the Streamlit App

To make interaction with the API easier, we've built a **Streamlit** interface that allows you to input transaction data and receive fraud predictions visually.

### 1. **Run Streamlit**

To start the Streamlit app, use the following command:

```bash
streamlit run streamlit_app/main_ui.py
```

This will start a local web server, and you can access the UI in your browser at:

```
http://localhost:8501
```

### 2. **Streamlit Interface**

Once the Streamlit interface is running, you can input transaction details such as:

- `Amount`
- `Old Balance Original`
- `New Balance Original`
- `Old Balance Destination`
- `New Balance Destination`

After submitting the data, you will receive a prediction indicating whether the transaction is likely to be fraudulent, along with the fraud probability.

## 📂 Project Structure

```plaintext
FraudDetection/
│
├── app/
│   ├── main.py             # FastAPI entry point
│   ├── models/             # Trained machine learning models
│   └── services/           # Service logic for predictions
│
├── streamlit_app/
│   ├── main_ui.py          # Streamlit interface
│   ├── schemas/            # Request and response schemas
│   └── services/           # API interaction logic
│
├── .gitignore              # Ignore unnecessary files like .env and venv/
├── requirements.txt        # Project dependencies
├── README.md               # Project overview and setup instructions
└── .env                    # Environment configuration (not included in the repo)
```

## 💡 Contribution

Contributions are welcome! Please feel free to submit a pull request or create issues for any bugs or improvements.
