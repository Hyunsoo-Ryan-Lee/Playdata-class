class Bookshelf:
    def __init__(self,title,page,author,category):
        self.title = title
        self.page = page
        self.author = author
        self.category = category

    def __str__(self):
        return f'책 정보 : {self.title}({self.page}pg) - {self.author} / {self.category}'

    def getName(self):
        return self.title

    def setName(self,new_title):
        self.title = new_title
        return self.title 
    
    if __name__ == '__main__':
        print('if __name__ == __main__')

b1 = Bookshelf('음악과함께',200,'가나다','음악')
print(b1)