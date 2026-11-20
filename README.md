# Smart Loan Recovery System

A web application built with **Python** and **Flask** that assesses borrower repayment risk and recommends tailored loan recovery strategies.

---

## Screenshots

### Home / Input Form
![Home Screen](screenshots/Screenshot_1.png)

### Recovery Assessment Result 1
![Prediction Result 1](screenshots/Screenshot_2.png)

### Recovery Assessment Result 2
![Prediction Result 2](screenshots/Screenshot_3.png)

---

## Tech Stack
* **Backend:** Python, Flask, NumPy, Pandas, Scikit-Learn, Joblib
* **Frontend:** HTML5, CSS3 (Jinja2 Templates)
* **Data Analysis & Model Training:** Jupyter Notebook
* **Tools:** VS Code, Git & GitHub

---

## Project Structure

```text
smart_loan_recovery/
│
├── model/                              # Saved ML model
├── screenshots/                        # App UI screenshots
│   ├── Screenshot_1.png
│   ├── Screenshot_2.png
│   └── Screenshot_3.png
├── templates/                          # HTML templates
│   └── index.html
├── .gitignore                          # Git ignore rules
├── app.py                              # Main Flask application
├── loan-recovery.csv                   # Loan recovery dataset
├── README.md                           # Project documentation
├── requirements.txt                    # Project dependencies
└── Smart Loan Recovery System.ipynb    # Model development & EDA notebook
```

---

## Getting Started

### Prerequisites
* Python 3.9 or higher

### 1. Clone the Repository
```bash
git clone https://github.com
cd smart-loan-recovery
```

### 2. Create & Activate Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open your browser and go to `http://127.0.0.1:5000` to use the app.

---

## Features
* **Data Exploration & Modeling:** Built and evaluated in `Smart Loan Recovery System.ipynb` using `loan-recovery.csv`.
* **Risk Classification:** Categorizes borrowers into **Low Risk**, **Moderate Risk**, or **High Risk**.
* **Actionable Recommendations:** Outputs a tailored recovery strategy based on predicted risk level.
