from flask import Flask, request, jsonify
from service import ToDoService
from models import Schema
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/name")
def name():
    return 'My name is Nay'
@app.route("/todo" ,methods=["POST"])
def create_todo():
    return ToDoService().create(request.get_json())

if __name__=='__main__':
    Schema()
    app.run(debug=True)