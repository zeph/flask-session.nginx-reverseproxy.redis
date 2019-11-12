from flask import Flask, session
from flask_session import Session
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# Check Configuration section for more details
SESSION_TYPE = 'redis'
SESSION_REDIS = redis
app.config.from_object(__name__)
Session(app)

@app.route('/', methods=["PUT"])
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/')
def get():
    count = redis.incr('hits')
    value = session.get('key', 'not set')
    return '({}) Hello World! I have been seen {} times.\n'.format(value, count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)