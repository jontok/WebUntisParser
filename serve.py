from flask import Flask,jsonify
from flask_cors import CORS, cross_origin
import jsonDataclass
app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/")
def links():
    return "<a href='/period'>periods</a><br><a href='/classes'>classes</a>"

@app.route("/periods/<base_domain>/<school_id>/<class_id>/<date>", methods=['GET'])
def serveClassPeriods(base_domain,school_id,class_id,date):
    return jsonify(jsonDataclass.getPeriods(base_domain,school_id,class_id,date))

@app.route("/classes/<base_domain>/<school_id>")
@cross_origin(supports_credentials=True)
def serveClasses(base_domain,school_id):
    return jsonify(jsonDataclass.getSchoolClasses(school_id,base_domain))