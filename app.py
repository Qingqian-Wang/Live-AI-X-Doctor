from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from interact import interact_once

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

dataset = []
health_rating = [75]






@app.route('/update-number', methods=['GET'])
def update_number():
    # Your logic to generate a new health rating
    promt = "Now you are should follow the instruction strictly. Only Output a number, ranging from 30 to 100, to represent the patient's health condition based on the current conversation. Here are some references: A score of 100 indicates that the patient has fully recovered and is in excellent health. 90 means the patient is close to recovery. A score of 80 indicates that the patient has a minor illness (such as a cough), a score of 50 indicates that the patient is in the early stages of a serious illness, and a score of 40 indicates that the patient is seriously ill. If the patient's condition description is vague, give a relatively optimistic score. The score should reflect the state of health, where a higher score indicates better health."
    health_rating.append( interact_once(promt, dataset, False, True))

    # Return the new health rating as JSON
    return render_template('index.html', messages=dataset[1:], health_rating=health_rating[-1])


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
        content = interact_once(message, dataset)
        print(content)
        print(dataset)
    return render_template('index.html', messages=dataset[1:], health_rating=health_rating[-1])




@app.route('/diagnosis-result', methods=['POST'])
def diagnosis_result():
    patient_gender = request.form['patient_gender']
    symptoms = request.form['symptoms']
    diagnosis = request.form['diagnosis']
    new_data= "Hi, my gender is " + patient_gender + " and my current symptoms are descripted as following " + symptoms + " finally I got a diagnosis from hospital is following " + diagnosis + " please combine the diagnosis from the doctor, give me some suggestions. In the next reply, don't ask me question."
    content = interact_once(new_data, dataset, False)
    print(dataset)
    print("fdsjifjsifjiofeijfiwejoifjewiofewifoiejfoeiwj" + health_rating)
    # Process the data here, for example, save it to a database or perform some calculations.

    # For now, we'll just render a simple confirmation page:
    return render_template('index.html', messages=dataset[1:], health_rating=health_rating[-1])


if __name__ == '__main__':
    app.run()
