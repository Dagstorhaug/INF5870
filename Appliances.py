dsadasffd


class Appliances(self, name, consumption, intervall, duration, starttime, shiftable=False):
    def __init__(self):        
        self.shiftable = shiftable
        self.consunmption = consumption
        self.interveall = intervall
        self.duration = duration
        self.starttime = starttime
        
        properties = {'shiftable': self.shiftable, 
                      'consumption': self.consumption,
                      'intervall': self.intervall,
                      'duration': self.duration,
                      'starttime': self.starttime
        }
        
        self.appliance = {name: properties}
        
        
    def construct(self):
        return self.appliances
        
        
        
        



