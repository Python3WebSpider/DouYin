class User(object):
    
    def __init__(self, **kwargs):
        
        self.id = kwargs.get('id')
        self.gender = kwargs.get('gender')
        self.name = kwargs.get('nickname')
        