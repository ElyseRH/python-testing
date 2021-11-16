from datetime import date, timedelta
import requests


class Student:
    """
    A Student class as a base for method testing
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365) #student enrolled for 1 year
        self.naughty_list = False
    

    def apply_extension(self, days):
        self.end_date = self.end_date + timedelta(days=days)


    @property #decorator is for read only methods
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"


    def alert_santa(self):
        self.naughty_list = True

    
    def course_schedule(self): #mocking an api for a schedule
        response = requests.get(f"http://fakecompany.com/course-schedule/{self._last_name}/{self._first_name}")

        if response.ok:
            return response.text
        else:
            return "Something went wrong with the request"