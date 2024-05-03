from flask import Flask, request
import redis
import json

app = Flask(__name__)
redis_client = redis.Redis(host='valkey', port=6379, db=0)

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