from flask import Flask, render_template
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Replace 'YOUR_ENV_VARIABLE' with the actual name of your environment variable
    api_key = os.environ.get('GOOGLE_MAPS_API_KEY')
    return render_template('index.html', api_key=api_key)




if __name__ == '__main__':
    app.run()
