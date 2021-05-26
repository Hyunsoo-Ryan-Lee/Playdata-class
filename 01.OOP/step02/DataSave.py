# 학생, 선생 정보를 file로 부터 read해서 ,(콤마)를 기준으로 데이터를 나눠 Student와 Teacher 객체 생성 및 제공
from Studentinfo import Student

class DataPublic:
    # student 객체 제공해주는 method
    def stu_public():
        with open('students.csv','r',encoding='utf-8') as f:
            data = f.readline()
            print(data) # 이현수,3학년,남,수학 -> 하나의 문자열
            print(data.split(','))
            # ['이현수', '3학년', '남', '수학\n'] 쉼표 기준 분해 후 list에 저장
            s_info = data.split(',')
            s = Student(s_info[0],s_info[1],s_info[2],s_info[3])
            print(s) # 객체를 참조하는 변수인 경우에 한해서만 str()이 호출되는 구조

    # file 내용 다 read해서 3명의 정보의 student객체 만들기
    def stu_public2():
        with open('students.csv','r',encoding='utf-8') as f:
            data = f.readlines()
            for i in data:
                sv = i.split(',')
                s = Student(sv[0],sv[1],sv[2],sv[3])
                print(s) # all_stu는 student 객체들의 주소 list
    
    
    def stu_public3():
        all_stu = []
        with open('students.csv','r',encoding='utf-8') as f:
            data = f.readlines()
            '''['이현수,3학년,남,수학\n', '이예인,4학년,여,경제\n', '김철수,2학년,남,국어\n',
            '손가락,1학년,여,영어\n', '발가락,6학년,남,미술']'''
            for i in data:
                sv = i.split(',')
                # s = Student(sv[0],sv[1],sv[2],sv[3])
                all_stu.append(Student(sv[0],sv[1],sv[2],sv[3]))
                #생성된 여러개의 student 객체들을 새로운 list에 저장해서 반환
        return all_stu # all_stu는 student 객체들의 주소 list
            
    # 학생 정보들을 반복문 통해서 출력하는 method 구현
    def stu_print(a_stu):
        for i in a_stu:
            print(i)


    #DataPublic 클래스의 method 정상 실행 확인만을 위한 특수 시작 코드
    if __name__ == '__main__':
        stu_public2()
        # stu_print(stu_public3()) # stu_print() 함수에 all_stu이 인자로 들어간다. 따라서 all의 각 항이 for문 돌며 출력된다.
