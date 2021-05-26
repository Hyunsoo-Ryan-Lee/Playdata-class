class Teach:
    def __init__(self,name,age,grade,subject):
        self.name = name
        self.age = age
        self.grade = grade
        self.subject = subject

    def __str__(self):
        return f'선생님 정보 : {self.name}({self.age}, {self.subject}) - {self.grade}'

    def getName(self):
        return self.name

    def setName(self,new_name):
        self.name = new_name
        return self.name 
