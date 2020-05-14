from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import psutil

app = Flask(__name__)
api = Api(app)

class GetStorage(Resource):
    def get(self):
        storage = psutil.disk_usage('/')
        return jsonify({
            "message": "System storage",
            "value": storage
            })
    
class GetMemory(Resource):
    def get(self):
        memory = psutil.virtual_memory()
        return jsonify({
            "message": "RAM memory",
            "value": memory
            })

api.add_resource(GetStorage, '/storage')
api.add_resource(GetMemory, '/memory')

if __name__ == '__main__':
    app.run(debug=True)
