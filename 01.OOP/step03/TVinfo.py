class TV:
    def __init__(self,name,company):
        self.name = name
        self.company = company

    def __str__(self):
        return f'이 TV의 이름은 {self.name}이며 제작 회사는 {self.company}입니다.'

    def getName(self): # self는 멤버 변수 호출을 위한 필수 키워드
        return self.name # 생성된 객체가 보유한 멤버변수값 반환



if __name__ == '__main__':
    tv = TV('슬림','LG')
    print(tv)