from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app=app)
ns = api.namespace('image', description='all image in stie download')

@ns.route("/test")
class test(Resource):
    def get(self):
        return "test get"
    
    def post(self):
        return "test post"






if __name__ == "__main__":
    app.run(debug = False)