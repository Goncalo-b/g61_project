from gclass import Gclass

class Platform(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    path = ''
    att = ['_platform_id']

    def __init__(self, platform_id):
        self._platform_id = int(float(platform_id))
        if self._platform_id not in Platform.obj:
            Platform.obj[self._platform_id] = self
            Platform.lst.append(self._platform_id)

    @property
    def platform_id(self): 
        return self._platform_id
    
    def __str__(self): 
        return f"Platform | ID: {self._platform_id}"
    
    
