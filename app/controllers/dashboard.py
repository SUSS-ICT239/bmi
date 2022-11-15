from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime, timedelta, date
from app import db

import csv
import io
from statistics import mean

from models.bmidaily import BMIDAILY
from models.chart import CHART

dashboard = Blueprint('dashboard', __name__)

def getChartDim(user_email=None):

    # meta = {'collection': 'bmidaily'}
    # user = db.ReferenceField(User)
    # date = db.DateTimeField()
    # numberOfMeasures = db.IntField()
    # averageBMI = db.FloatField()
    
    chartDim = {} 
    labels = []
    
    # New Output 
    # var chartDim = data.chartDim; 
    # {'usr_1': [[datetime1, 23], [datetime2, 21.5], ...], 'usr_2': [[],[], ... ],  ...}
    # var xLabels = data.labels;
    # [] 

    try:
        bmidailys = BMIDAILY.objects()
        chartDim = {}

        for bmidaily in bmidailys:
            if not user_email or (bmidaily.user.user_email == user_email): 
                bmis = chartDim.get(bmidaily.user.name)
                if not bmis:
                    chartDim[bmidaily.user.name]=[[bmidaily.date, bmidaily.averageBMI]]
                else:
                    bmis.append([bmidaily.date, bmidaily.averageBMI])
        return chartDim, labels
    except:
        return None

def getAveDict():
    
    # meta = {'collection': 'bmidaily'}
    # user = db.ReferenceField(User)
    # date = db.DateTimeField()
    # numberOfMeasures = db.IntField()
    # averageBMI = db.FloatField()
    
    aveDict = {} 
    
    # New Output - dictionary with user name as key and average BMI as value
    # aveDict
    # {'usr_1': 12.23, 'usr_2': 12.23,  ...}

    try:
        bmidailys = BMIDAILY.objects()
        for bmidaily in bmidailys:
            user_name, aveBMI = bmidaily.user.name, bmidaily.averageBMI
            aves = aveDict.get(user_name)
            if not aves:
                aveDict[user_name]=[aveBMI]
            else:
                aves.append(aveBMI)
        
        for key, values in aveDict.items():
            aveDict[key]=mean(values)
        
        return aveDict
    except:
        return None

@dashboard.route('/chart2', methods=['GET', 'POST'])
def chart2():
    if request.method == 'GET':
        #I want to get some data from the service
        return render_template('bmi_chart2.html', name=current_user.name, panel="BMI Chart")    #do nothing but to show index.html
    elif request.method == 'POST':
        
        chartDim, labels = getChartDim()
        
        return jsonify({'chartDim': chartDim, 'labels': labels})

@dashboard.route('/chart3', methods=['GET', 'POST'])
def chart3():
    if request.method == 'GET':
        #I want to get some data from the service
        return render_template('bmi_chart3.html', name=current_user.name, panel="BMI Chart")    #do nothing but to show index.html
    
    elif request.method == 'POST':
    
        aveDict = getAveDict()
        return jsonify({'averages': aveDict})
   
@dashboard.route('/dashboard')
@login_required
def render_dashboard():
    return render_template('dashboard.html', name=current_user.name, panel="Dashboard")

@dashboard.route('/chart')
@login_required
def chart():
    return render_template('bmi_chart.html', name=current_user.name, panel="BMI Chart")
