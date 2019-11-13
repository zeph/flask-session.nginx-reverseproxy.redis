from flask import Flask, session, jsonify
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)
print('secret_key', app.secret_key)

#SESSION_COOKIE_PATH = 'not the one'
app.config.from_object(__name__)

@app.route('/', methods=["PUT"])
def set():
    session['key'] = 'value'
    return jsonify("ok"), 201

@app.route('/')
def get():
    value = session.get('key', 'not set')
    http_code = 401 if value == 'not set' else 200
    return jsonify({'value':value, 'count': 'Hello World! Forgive me...'}), http_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)