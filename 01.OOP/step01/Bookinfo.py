class Book:
    
    # 생성자 - 객체생성(실 data로 생성 - 멤버 변수에 값 할당, 변수 초기화)
    def __init__(self, title, author):
        self.title = title
        self.author = author
        print('Book __init__')

    def getBookName(self):
        return self.title
    
    def getAuthorName(self):
        return self.author


