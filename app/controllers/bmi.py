from flask import Blueprint, render_template, request, jsonify
from datetime import datetime, timedelta, date
from flask_login import current_user
from models.bmidaily import BMIDAILY
from models.bmilog import BMILOG
from models.users import User

import csv
import io
import math

bmi = Blueprint('bmi', __name__)

# This controls controls the Ajax call to log a BMI 
@bmi.route('/process',methods= ['POST'])
def process():
    weight  = float(request.form['weight'])
    height = float(request.form['height'])

    # Since there is only one reading allowed in each day, the latest will be the log
    today = date.today()
    now = datetime.now()
    
    try:
        existing_user = User.objects(email=current_user.email).first()
    
        bmilogObject = BMILOG(user=existing_user, datetime=now, weight=weight, height=height)
        bmilogObject.bmi = bmilogObject.computeBMI(request.form['unit'])
        bmilogObject.save()
        
        bmidailyObjects = BMIDAILY.objects(user=existing_user, date=today) #GET INFO
        
        if len(bmidailyObjects) >= 1:

            # new_bmi_average = bmidailyObjects[0].updatedBMI(bmilogObject.bmi)
            # number = bmidailyObjects[0].numberOfMeasures
            # bmidailyObjects[0].update(__raw__={'$set': {'numberOfMeasures': number + 1, 'averageBMI': new_bmi_average}})

            the_bmidailyObject = bmidailyObjects.first()
            new_bmi_average = the_bmidailyObject.updatedBMI(bmilogObject.bmi)
            the_bmidailyObject.numberOfMeasures += 1
            the_bmidailyObject.averageBMI = new_bmi_average
            the_bmidailyObject.save()

        else:
            
            bmidailyObject = BMIDAILY(user=existing_user, date=today, numberOfMeasures=1, averageBMI = bmilogObject.bmi)
            bmidailyObject.save()
            
    except Exception as e:
        print(f"{e}")
        return jsonify({})
        
    return jsonify({'bmi' : bmilogObject.bmi})

@bmi.route('/process2',methods= ['POST'])
def process2():
    weight  = float(request.form['weight'])
    height = float(request.form['height'])

    # Since there is only one reading allowed in each day, the latest will be the log
    today = date.today()
    now = datetime.now()
    
    try:
        existing_user = User.objects(email=current_user.email).first()
    
        bmilogObject = BMILOG(user=existing_user, datetime=now, weight=weight, height=height)
        bmilogObject.bmi = bmilogObject.computeBMI(request.form['unit'])
        bmilogObject.save()
        
        bmidailyObjects = BMIDAILY.objects(user=existing_user, date=today) #GET INFO
        
        if len(bmidailyObjects) >= 1:

            # new_bmi_average = bmidailyObjects[0].updatedBMI(bmilogObject.bmi)
            # number = bmidailyObjects[0].numberOfMeasures
            # bmidailyObjects[0].update(__raw__={'$set': {'numberOfMeasures': number + 1, 'averageBMI': new_bmi_average}})

            the_bmidailyObject = bmidailyObjects.first()
            new_bmi_average = the_bmidailyObject.updatedBMI(bmilogObject.bmi)
            the_bmidailyObject.numberOfMeasures += 1
            the_bmidailyObject.averageBMI = new_bmi_average
            the_bmidailyObject.save()

        else:
            
            bmidailyObject = BMIDAILY(user=existing_user, date=today, numberOfMeasures=1, averageBMI = bmilogObject.bmi)
            bmidailyObject.save()
            
    except Exception as e:
        print(f"{e}")
        return jsonify({})
        
    return jsonify({'bmi' : bmilogObject.bmi})

