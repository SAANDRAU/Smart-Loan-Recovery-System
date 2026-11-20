from flask import Flask, render_template, request
import numpy as np
# import joblib  # Uncomment if loading a saved ML model

app = Flask(__name__)

# Load your trained model (Uncomment and update path if applicable)
# model = joblib.load('model/loan_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 1. Extract data from HTML form
        borrower_name = request.form.get('borrower_name')
        loan_amount = float(request.form.get('loan_amount'))
        days_overdue = int(request.form.get('days_overdue'))
        credit_score = int(request.form.get('credit_score'))
        monthly_income = float(request.form.get('monthly_income'))

        # 2. Model Prediction / Smart Recovery Logic
        # If using an ML model, prepare features and call model.predict():
        # features = np.array([[loan_amount, days_overdue, credit_score, monthly_income]])
        # risk_prediction = model.predict(features)[0]

        # Example heuristic logic (Replace with your actual model output)
        debt_to_income = loan_amount / (monthly_income * 12)
        
        if days_overdue <= 30 and credit_score >= 650:
            risk_level = "Low Risk"
            strategy = "Send automated SMS/Email payment reminder with a 3-day grace period."
        elif days_overdue <= 90 and debt_to_income < 0.5:
            risk_level = "Moderate Risk"
            strategy = "Schedule a call with a recovery agent to offer a restructured EMI plan."
        else:
            risk_level = "High Risk"
            strategy = "Escalate to legal/field recovery team and offer a one-time settlement discount."

        return render_template(
            'index.html',
            prediction_done=True,
            name=borrower_name,
            risk_level=risk_level,
            strategy=strategy
        )

    except Exception as e:
        return render_template('index.html', error=f"Error processing input: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
