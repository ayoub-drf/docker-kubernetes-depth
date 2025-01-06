from flask import Flask
import redis

app = Flask(__name__)

r = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    visits = r.get('visits')
    if visits is None:
        visits = 0
    else:
        visits = int(visits)
    
    r.set('visits', visits + 1)

    return f"Number of visits: {visits}"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
