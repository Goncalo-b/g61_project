import datetime
from gclass import Gclass

class Trans(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    path = ''
    att = [ '_platform_id', '_certificate_id', '_issue_date', '_certificate_fee', 'trans_id']

    def __init__(self ,platform_id, certificate_id, issue_date, certificate_fee):
        self._trans_id = Trans.get_id(0)
        self.__class__.obj[self._trans_id] = self
        self.__class__.lst.append(self._trans_id)
        self._platform_id = int(float(platform_id))
        self._certificate_id = int(float(certificate_id))
        
        if isinstance(issue_date, str):
            self._issue_date = datetime.date.fromisoformat(issue_date[:10])
        else:
            self._issue_date = issue_date
            
        self._certificate_fee = float(certificate_fee)

        
    @property
    def trans_id(self): 
        return self._trans_id

    @property
    def platform_id(self): 
        return self._platform_id

    @property
    def certificate_id(self): 
        return self._certificate_id

    @property
    def issue_date(self): 
        return self._issue_date

    @property
    def certificate_fee(self): 
        return self._certificate_fee


    def __str__(self):
        return f"Transaction {self._trans_id} | Date: {self._issue_date} | Fee: {self._certificate_fee:.2f}€"
    
    






