class wizard :
    def __init__(self, name ):
        if not name:
            raise ValueError("Misssing name")
        self.name= name 


class Student(wizard):
    def __init__(self,name, house):
        super().__init__(name)
        self.house = house
    ...

class Professor(wizard):
    def __inti__(self, name, subject):
        super().__init__(name)
        self.subject = subject    
