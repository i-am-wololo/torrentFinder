from flask import Flask, jsonify, request
import main

app = Flask(__name__)

@app.route("/")
def index():
    return "this is the index page of the server"








@app.route('/query', methods=['GET', 'POST'])
def search():
    if request.method == "GET":
        return "test"
    else:
        if "provider" in request.form.keys():
            return jsonify(main.search(request.form['query'], request.form['provider']))
        else:
            return jsonify(main.search(request.form['query']))

        return "OK"
