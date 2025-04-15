
# 🔍 Customer Churn Prediction

This project is a **Machine Learning-based Streamlit web application** designed to predict whether a customer is likely to churn based on their personal and account-related attributes. It includes preprocessing steps, a trained neural network model, and an interactive frontend using Streamlit.

---

## 🚀 Project Overview

Customer churn is a key concern for businesses, especially those offering subscription-based services. This project uses deep learning to predict churn probability based on input features like age, balance, tenure, and more. The model is deployed using **Streamlit** to allow real-time predictions through a web interface.

---

## 🧠 Features

- End-to-end **churn prediction system**
- **Neural network model** built using TensorFlow/Keras
- **Preprocessing pipeline** using scikit-learn
- Encoders and scalers saved and reused with `pickle`
- Streamlit frontend with interactive user inputs
- Displays **churn probability** and interprets result

---

## 📂 Project Structure

```
Customer-Churn-Prediction/
│
├── model.h5                      # Trained Keras model
├── scalar.pkl                    # StandardScaler used for input normalization
├── onehot_encoder_geo.pkl        # OneHotEncoder for 'Geography'
├── label_encoder_gender.pkl      # LabelEncoder for 'Gender'
├── streamlit_app.py              # Streamlit web application script
├── requirements.txt              # Required Python packages
└── README.md                     # Project documentation
```

---

## 🛠️ Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- TensorFlow / Keras
- Streamlit
- Pickle (for saving encoders/scalers)

---

## ⚙️ How It Works

1. **Inputs** are collected via Streamlit UI:
   - Geography
   - Gender
   - Age
   - Credit Score
   - Balance
   - Tenure
   - Number of Products
   - Has Credit Card
   - Is Active Member
   - Estimated Salary

2. **Preprocessing** is applied:
   - Gender is label encoded.
   - Geography is one-hot encoded.
   - Features are scaled using a trained StandardScaler.

3. The input is passed into a **trained Keras model** (`model.h5`) to predict churn probability.

4. The result is displayed along with an interpretation (likely to churn / not likely to churn).

---

## 💻 Running the App

### 1. Clone the repository

```
git clone https://github.com/Jay-agrawal15/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

### 2. Install required packages

```
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```
streamlit run streamlit_app.py
```

---

## 📊 Example Output

```
Churn Probability: 0.78
The customer is likely to churn
```

---

## 📌 Future Enhancements

- Visualize feature importance or SHAP values
- Include customer feedback data
- Add database integration for customer records
- Deploy online (e.g., Streamlit Cloud, Hugging Face Spaces)

---

## 📬 Contact

**Jay Agrawal**  
📧 agrawaljay654@gmail.com 
🔗 [GitHub](https://github.com/Jay-agrawal15)

---

⭐ If you found this project helpful, feel free to star ⭐ this repository and share it!
