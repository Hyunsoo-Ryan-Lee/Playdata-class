# Method : 이름 제공 - getCust_name or getCustName / 등급 제공 - getXxx

class Customer:
    
    # 생성자 - 객체생성(실 data로 생성 - 멤버 변수에 값 할당, 변수 초기화)
    def __init__(self, name, grade):
        self.cust_name = name
        self.cust_grade = grade
        print('Customer __init__')

    def getCustName(self):
        return self.cust_name


