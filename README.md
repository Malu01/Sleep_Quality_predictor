# 🌙 Sleep Quality Predictor (Flask + Machine Learning)

## 📌 Overview

The **Sleep Quality Predictor** is a Machine Learning-based web application that analyzes a user’s lifestyle and behavioral patterns to predict their sleep quality.

It classifies sleep into:

* ✅ Good
* ⚖️ Average
* ❌ Poor

The system also provides **personalized suggestions** to help users improve their sleep habits.

---

## 🎯 Problem Statement

Poor sleep quality is linked to several health issues such as stress, obesity, and reduced productivity. However, many people are unaware of how their daily habits affect their sleep.

This project aims to solve this problem by:

* Analyzing lifestyle factors
* Predicting sleep quality
* Providing actionable insights

---

## 🚀 Features

* 🧠 Predicts sleep quality using Machine Learning
* 📊 Considers multiple lifestyle factors:

  * Sleep duration
  * Physical activity
  * Stress level
  * Caffeine intake
  * Mood
* 💡 Provides personalized improvement tips
* 🌐 Built using Flask for real-time web interaction
* 📝 Optional NLP-based sleep diary analysis

---

## 🛠️ Technologies Used

### 💻 Programming Language

* Python

### 📚 Libraries

* pandas, NumPy – Data preprocessing
* scikit-learn – Model training
* joblib – Model saving/loading
* Flask – Web framework

### 🤖 Machine Learning Model

* Random Forest Classifier

---

## 📊 Dataset

* Sleep Health and Lifestyle Dataset (Kaggle)
* Additional simulated features:

  * Caffeine Level
  * Mood Score

---

## 🧠 How It Works

1. User enters daily lifestyle details
2. Data is processed and scaled
3. Machine Learning model predicts sleep quality
4. System displays result + suggestions

---

## 🖥️ Project Structure

```
Sleep-Quality-Predictor/
|
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Malu01/Sleep-Quality-predictor.git
cd Sleep-Quality-predictor
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Flask App

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📈 Output Example

**Predicted Sleep Quality:** Average

**Suggestions:**

* Reduce screen time before bed
* Improve physical activity
* Manage stress levels

---

## 🧪 Model Performance

* Accuracy: ~85–95% (depends on dataset)
* Evaluated using classification metrics

---

## ⚠️ Limitations

* Uses limited dataset
* Some features (caffeine, mood) are simulated
* Does not include real-time biometric data

---

## 🔮 Future Enhancements

* 📱 Mobile app integration
* ⌚ Smartwatch / wearable data support
* 🤖 AI chatbot for sleep advice
* 🧠 Deep Learning models (LSTM)
* 📊 Sleep trend tracking dashboard

---

## 🧑‍💻 Author

**Malathika P**

---

## 📜 License

This project is for educational and research purposes.
