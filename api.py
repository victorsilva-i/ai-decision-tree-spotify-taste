from flask import Flask, escape, request
from flask import jsonify
import main
import json
# get this object
from flask import Response

app = Flask(__name__)


@app.route('/api-test')
def hello():
    datastore = json.loads(main.main()['songs'])
    return  jsonify(songs=datastore, score=main.main()['score'])
