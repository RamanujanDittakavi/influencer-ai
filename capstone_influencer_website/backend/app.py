
from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

users_data = [
    {"name":"User1","followers":1200,"score":0.91},
    {"name":"User2","followers":800,"score":0.65},
    {"name":"User3","followers":5000,"score":0.88},
    {"name":"User4","followers":2000,"score":0.72},
    {"name":"User5","followers":9500,"score":0.97},
    {"name":"User6","followers":3000,"score":0.83}
]

@app.route("/login", methods=["POST"])
def login():
    return jsonify({"status":"success","message":"Login successful"})

@app.route("/influencers")
def influencers():
    top = sorted(users_data, key=lambda x:x["score"], reverse=True)[:5]
    return jsonify(top)

@app.route("/campaign", methods=["POST"])
def campaign():
    product = request.json["product"]
    influencers = sorted(users_data, key=lambda x:x["score"], reverse=True)[:3]
    reach = random.randint(10000,50000)

    return jsonify({
        "product":product,
        "reach":reach,
        "influencers":influencers
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
