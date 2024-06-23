import json
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def get(self):
        return {"name": "narith", "gender": "M"}

api.add_resource(User, "/login")

# @app.route("/")
# def index():
#     return json.dumps({'name': 'alice', 'email': 'alice@outlook.com'})

if __name__ == '_main_':
    app.run(debug=True)
