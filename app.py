from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import psutil

app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        return jsonify({"message": "This site shows you the main system info"})

class GetStorage(Resource):
    def get(self):
        storage = psutil.disk_usage('/')
        return jsonify({
            "message": "System storage",
            "value": {
                "Total": storage[0],
                "Used": storage[1],
                "Free": storage[2],
                "Percent": storage[3]
                }
            })
    
class GetMemory(Resource):
    def get(self):
        memory = psutil.virtual_memory()
        return jsonify({
            "message": "RAM memory",
            "value": {
                "Total": memory[0],
                "Avaliable": memory[1],
                "Percent": memory[2],
                "Used": memory[3],
                "Free": memory[4]
                }
            })

api.add_resource(GetStorage, '/storage')
api.add_resource(GetMemory, '/memory')
api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
