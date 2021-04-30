from flask import Flask, request
from peanuts import peanuts
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def welcome():
    return "Welcome to the Peanuts Translating API"

@app.route('/encode')
@cross_origin()
def encode():
    value = request.args.get('value')
    return peanuts(value)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)