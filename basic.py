from flask import Flask, jsonify, request
app = Flask(__name__)
from main import *
import datetime
import models


@app.route("/api/heart_rate", methods=["POST"])
def userCreation():
    r = request.get_json()

    user_email = r["user_email"]
    user_age = r["user_age"]
    heart_rate = r["heart_rate"]

    try:
        add_heart_rate(user_email, heart_rate, time=datetime.datetime.now())
    except:
        create_user(user_email, user_age, heart_rate, time=datetime.datetime.now())
        return 'User is created'
    return 'User overlap detected, data is appended'


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def getInfo(user_email):
    userJson = print_user(user_email)
    return jsonify(userJson)


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def averageHR(user_email):
    hrAvg = average_HR_Calc(user_email)
    averageHRJson = {
        "Average HR": hrAvg
    }
    return jsonify(averageHRJson)

@app.route("/api/heart_rate/interval_average", methods = ['POST'])
def interval_average():
    r = request.get_json()

    user_email = r["user_email"]
    time = r["heart_rate_average_since"]


    hrAvg = interval_HR_calc(user_email,time)
    averageHrJson = {
        "average hr since specified time": hrAvg
    }
    return jsonify(averageHRJson )
    # except:
    #     print("No user exists or no data points after that time!")

    # return 'ok'
