# 한 학생 정보만 보유 가능한 class


class Student:
    def __init__(self,name,grade,gender,subject):
        self.stu_name = name
        self.stu_grade = grade
        self.stu_gender = gender
        self.stu_subject = subject

    def __str__(self):
        # 참조 변수명만 출력시 str이 자동 살행되어 return된 구조로 실행
        # 멤버 변수들을 다 결합해서 하나의 문자열로 반환
        # 인스턴스 자체를 출력 할 때의 형식을 지정해주는 함수
        return '학생정보 : ' + self.stu_name + ' ' + self.stu_grade + ' ' + \
            self.stu_gender + ' ' +  self.stu_subject


    # 각 멤버 변수별로 set/getXxx 함수가 있다 가정
'''
    def setStuGrade(self,new_grade):
    # 유효성 검증 코드 필수
        self.grade = new_grade

    def setStuGender(self,new_gender):
    # 유효성 검증 코드 필수
        self.gender = new_gender'''