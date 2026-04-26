
from gclass import Gclass

class Course(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    path = ''
    att = ['_course_id', '_course_name', '_course_info', '_platform_id', '_online_date']

    def __init__(self, course_id , course_name, course_info, platform_id, online_date):
        if str(course_id) == "None":
            self._course_id= Course.get_id(0)
        else:
            self._course_id = int(float(course_id))
        self._course_name = str(course_name)
        self._course_info = str(course_info)
        self._platform_id = int(float(platform_id))
        self._online_date = str(online_date)
        if self._course_id not in self.__class__.obj:
            self.__class__.obj[self._course_id] = self
            self.__class__.lst.append(self._course_id)


    @property
    def course_id(self): return self._course_id

    @property
    def course_name(self): return self._course_name

    @property
    def course_info(self): return self._course_info

    def __str__(self):
        return f'Course | ID: {self._course_id} | Name: {self._course_name}'
    
    
