from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

menu_items={
    "fish": 199,
    "soup": 149,
    "burger": {"cheese": True,
                "bacon": True,
                "fries": True}
}

class Menu(Resource):
    def get(self, item):
        return {"price": menu_items[item]}
    
    def put(self, item):
        return "put"

    def post(self):
        return request.args

class Fish(Resource):
    def get(self, item):
        return item

api.add_resource(Menu, '/menu/<string:item>')
api.add_resource(Fish, '/menu/fish/<string:item>')

if __name__ == "__main__":
    app.run(debug=True)

