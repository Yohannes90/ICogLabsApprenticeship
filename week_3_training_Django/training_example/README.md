# Prediction Project

This repository contains the code and resources for a prediction project developed using Django. Below is a brief overview of the project structure, setup instructions, and proof of execution.

## Project Structure

```
.
|-- prediction
|   |-- db.sqlite3
|   |-- manage.py
|   |-- ml_model.joblib
|   |-- predict
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- ml_model.py
|   |   |-- models.py
|   |   |-- templates
|   |   |   `-- predict.html
|   |   |-- urls.py
|   |   `-- views.py
|   |-- prediction
|   |   |-- settings.py
|   |   |-- urls.py
|   |   `-- wsgi.py
|   `-- scaler.joblib
|-- requirements.txt
|-- screenshot\ of\ code\ running\ on\ localhost.png
|-- screenshot\ of\ code\ running\ on\ terminal.png
`-- venv
```

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Set up Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate   # For Windows
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:8000`.

## Proof of Execution

Below are screenshots demonstrating the project running successfully:

1. **Code running in terminal:**
   ![Terminal Output](screenshot%20of%20code%20running%20on%20terminal.png)

2. **Application running on localhost:**
   ![Localhost Output](screenshot%20of%20code%20running%20on%20localhost.png)

## Notes

- The `ml_model.joblib` and `scaler.joblib` files are pre-trained machine learning model assets used for prediction.
- The database file (`db.sqlite3`) and virtual environment (`venv`) are included for reference but may not need to be shared in production.
