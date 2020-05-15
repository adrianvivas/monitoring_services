from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
import psutil

app = Flask(__name__)
CORS(app)
#cors = CORS(app, resources={r"/api/*":{"origins": "*"}})
api = Api(app)

#@app.route('/api/v1/users')
#def list_users():
 #   return "user example"

class Main(Resource):
    def get(self):
        return jsonify({"message": "This site shows you the main system info"})

class GetStorage(Resource):
    def get(self):
        storage = psutil.disk_usage('/')
        return jsonify({
            "message": "System storage",
            "value": {
                "total": storage[0],
                "used": storage[1],
                "free": storage[2],
                "percent": storage[3]
                }
            })
    
class GetMemory(Resource):
    def get(self):
        memory = psutil.virtual_memory()
        return jsonify({
            "message": "RAM memory",
            "value": {
                "total": memory[0],
                "avaliable": memory[1],
                "percent": memory[2],
                "used": memory[3],
                "free": memory[4]
                }
            })

api.add_resource(GetStorage, '/storage')
api.add_resource(GetMemory, '/memory')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run('192.168.0.23',4000,debug=True)
