from flask import Flask, render_template
import os
from dotenv import load_dotenv
from flask import request

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route('/map')
def map():
    # Replace 'YOUR_ENV_VARIABLE' with the actual name of your environment variable
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    return render_template('map.html', api_key=api_key)


@app.route('/diagnosis')
def diagnosis_page():
    # Render a template or perform other logic for the diagnosis page
    return render_template('diagnosis.html')


@app.route('/', methods=['GET', 'POST'])
def conversation_input():
    if request.method == 'POST':
        message = request.form['message']
        print(message)
    return render_template('index.html')


@app.route('/diagnosis-result', methods=['POST'])
def diagnosis_result():
    patient_name = request.form['patient_name']
    symptoms = request.form['symptoms']
    diagnosis = request.form['diagnosis']
    # Process the data here, for example, save it to a database or perform some calculations.

    # For now, we'll just render a simple confirmation page:
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
