from gclass import Gclass

class Certificate(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    path = ''
    att = ['_certificate_id', '_certificate_name', '_certificate_type']

    def __init__(self, certificate_id, certificate_name, certificate_type):
        self._certificate_id = int(float(certificate_id))
        self._certificate_name = str(certificate_name)
        self._certificate_type = str(certificate_type)

        if self._certificate_id not in Certificate.obj:
            Certificate.obj[self._certificate_id] = self
            Certificate.lst.append(self._certificate_id)

    @property
    def certificate_id(self): 
        return self._certificate_id

    @property
    def certificate_name(self):
        return self._certificate_name

    @property
    def certificate_type(self): 
        return self._certificate_type

    def __str__(self):
        return f"ID: {self._certificate_id} | Name: {self._certificate_name} | Type: {self._certificate_type}"




