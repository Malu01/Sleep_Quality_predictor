from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# --- 1. LOAD ASSETS ---
try:
    model = joblib.load('sleep_predictor_model.pkl')
    scaler = joblib.load('scaler.pkl')
except Exception as e:
    print(f"Error: Missing model or scaler file! Run your Notebook first. Details: {e}")

# --- 2. NLP LOGIC ---
def analyze_sleep_diary(text):
    if not text or len(text.strip()) == 0:
        return "Neutral"
    
    positive_words = ['rested', 'deep', 'calm', 'good', 'refreshed', 'peaceful', 'great']
    negative_words = ['tired', 'awake', 'restless', 'anxious', 'noise', 'nightmare', 'bad']
    
    score = 0
    words = text.lower().split()
    for word in words:
        if word in positive_words: score += 1
        if word in negative_words: score -= 1
        
    if score > 0: return "Positive"
    elif score < 0: return "Negative"
    return "Neutral"

# --- 3. ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Order must match your Notebook: [Duration, Activity, Stress, Caffeine, Mood]
        raw_features = np.array([[
            float(data['duration']),
            float(data['exercise']),
            float(data['stress']),
            float(data['caffeine']),
            float(data['mood'])
        ]])

        # Apply Scaling
        scaled_features = scaler.transform(raw_features)

        # ML Prediction
        prediction = model.predict(scaled_features)[0]
        
        # NLP Analysis (Linked to your new UI text box)
        diary_sentiment = analyze_sleep_diary(data.get('diary', ''))

        # Tips Logic
        suggestion = ""
        if float(data['stress']) > 7:
            suggestion = "High stress detected. Try a 5-minute breathing exercise before bed."
        elif float(data['duration']) < 6:
            suggestion = "Short sleep duration. Aim for a consistent 7-8 hour window."
        else:
            suggestion = "Maintain your current lifestyle for stable sleep cycles."

        return jsonify({
            'result': prediction,
            'sentiment': diary_sentiment,
            'tip': suggestion
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)