from flask import Flask
from flask import request,send_from_directory
from flask import render_template,url_for
from flask import Response
import json
from datetime import datetime
import time
import mysql.connector
from elasticsearch import Elasticsearch
INDEX_NAME = "movie_index"
app = Flask(__name__, static_url_path='/static', 
            static_folder='static')


try:
    es.transport.close()
except:
    pass
es = Elasticsearch()

HOST = "root"
USER = "admin"
PASSWORD = "123456789"
mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  password=PASSWORD,
  database="movie_db"
)


def get_data(keyword):
    #TODO

    res = []
    for result in myresult:
        page = {
            "link":result["link"],
            "image":result["image"],
            "title":result["title"],
            "story":result["story"],
        }
        res.append(page)
    return res


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search', methods=['POST'])
def search():
    keyword = request.values.get('data')
    res = get_data(keyword)
    
    return Response(json.dumps(res),  mimetype='application/json')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6007, debug=True)
