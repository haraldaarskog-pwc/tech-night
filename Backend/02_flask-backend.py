from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

menu_items={
    "fish": 199,
    "soup": 149,
    "burger": 99
}

class HelloWorld(Resource):
    def get(self, item):
        return {"price": menu_items[item]}
    
    def put(self, item):
        return "put"

    def post(self):
        return request.args

api.add_resource(HelloWorld, '/menu/<string:item>')

if __name__ == "__main__":
    app.run(debug=True)