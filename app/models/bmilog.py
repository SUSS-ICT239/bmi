from app import db
from models.users import User

import math

class BMILOG(db.Document):

    meta = {'collection': 'bmilog'}
    user = db.ReferenceField(User)
    datetime = db.DateTimeField()
    weight = db.FloatField()
    height = db.FloatField()
    unit = db.StringField()
    bmi = db.FloatField()
    
    def computeBMI(self):
        if self.unit == 'm':
            bmi = self.weight / math.pow(self.height, 2)
        else:
            bmi = self.weight / math.pow(self.height/100, 2)
        return bmi