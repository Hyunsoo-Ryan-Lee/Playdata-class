from Teachers import Teach
from Books import Bookshelf

class SchoolAdmin():

    def teacher_public():
        with open('teachers.csv','r',encoding='utf-8') as f:
            print(f.read())

    def teacher_info():
        # 담당 선생님들의 상세 정보를 보여줍니다.
        with open('teachers.csv','r',encoding='utf-8') as f:
            data = f.readlines()
            for i in data:
                sp = i.split(',')
                t1 = Teach(sp[0],sp[1],sp[2],sp[3])
                print(t1)
    
    def book_info():
        # 교재들의 상세 정보를 보여줍니다.
        with open('Books.csv','r',encoding='utf-8') as p:
            info = p.readlines()
            for i in info:
                sp = i.split(',')
                b1 = Bookshelf(sp[0],sp[1],sp[2],sp[3])
                print(b1)

    def teacher_book():
        # 선생님의 담당 과목에 따른 책을 매치해서 보여줍니다.
        with open('teachers.csv','r',encoding='utf-8') as f:
            teacher_data = f.readlines()
            t_data = [] # 선생님들 data를 list로 넣어줍니다.
            for x in teacher_data:
                t_data.append(x.split(','))

        with open('Books.csv','r',encoding='utf-8') as p:
            book_info = p.readlines()
            b_info = [] # 책들의 information을 list로 넣어줍니다.
            for y in book_info:
                b_info.append(y.split(','))

        # 과목이 같으면 선생님과 책을 매치해줍니다.
        total = []
        for a in t_data:
            for b in b_info:
                if a[3] == b[3]:
                    total.append("{0}선생님의 교재는 '{1}'입니다.".format(a[0],b[0]))
                    
        [print(c) for c in total]


    
    if __name__ == '__main__':
        # teacher_public()
        # print('*'*50)
        # book_info()
        teacher_book()



