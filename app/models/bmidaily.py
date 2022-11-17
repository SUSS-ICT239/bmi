from app import db
from models.users import User

# class Bmi_Measurement(db_Document):
class BMIDAILY(db.Document):
    
    meta = {'collection': 'bmidaily'}
    user = db.ReferenceField(User)
    date = db.DateTimeField()
    numberOfMeasures = db.IntField()
    averageBMI = db.FloatField()
    
    def updatedBMI(self, newBMI):
        return (newBMI + (self.averageBMI * self.numberOfMeasures)) / (self.numberOfMeasures + 1) 
    
    # @property
    # def numberOfMeasures(self):
    #     return self.numberOfMeasures
    
    # @numberOfMeasures.setter
    # def numberOfMeasure(self, newNum):
    #     self.numberOfMeasures = newNum
    
    # @property
    # def averageBMI(self):
    #     return self.averageBMI
    
    # @averageBMI.setter
    # def averageBMI(self, newBMI):
    #     self.averageBMI = newBMI