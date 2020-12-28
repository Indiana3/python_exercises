from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'My first web app'

app.run(port=5000)

