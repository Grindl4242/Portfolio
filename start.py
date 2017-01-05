from flask import Flask, render_template
from pymongo import MongoClient
app = Flask(__name__)
coll = MongoClient('localhost', 27017)["Portfolio_db"]["Projects"]


@app.route('/')
def index():
    res = ""
    for item in coll.find():
        res += item.__str__() + "<br>"
    return render_template('index.html', data=coll.find())


@app.route('/projects/<string:project_name>')
def project_datail(project_name):
    query = coll.find_one({"name": project_name})
    return render_template('details.html', item=query)
