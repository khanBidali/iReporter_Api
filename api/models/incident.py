import datetime
incidents_list = []

class Incidents:
    '''This class stores incidents data'''
    increment = 0

    def __init__(self, id, createdOn, Type, location, Images, comment):
        Incidents.increment += 1
        self.id = id
        self.createdOn = createdOn 
        self.Type = Type
        self.location = location
        self.Images = Images
        self.comment = comment

    def serializable(self):
        return {
            'id': self.id,
            'createdOn': self.createdOn,
            'Type': self.Type,
            'location': self.location,
            'Images': self.Images,
            'comment': self.comment
        }


















