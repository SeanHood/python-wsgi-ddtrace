from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import redis
import json

app = Flask(__name__)
redis_client = redis.Redis(host='valkey', port=6379, db=0)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# db.create_all()



@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"



## Redis
@app.get("/redis/<key>")
def redis_read(key):
    return json.dumps(str(redis_client.get(key)))


@app.put("/redis/<key>/<value>")
def redis_put(key, value):
    return json.dumps(redis_client.set(key, value))


## DB
@app.get("/user/<username>")
def db_read(username):

    user = User.query.filter_by(username=username).first()

    return json.dumps(user.email)

@app.put("/user/<username>/<email>")
def db_put(username, email='nobody@example.com'):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return json.dumps(user.email)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username