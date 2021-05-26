
# 모듈 적용
from step01.Customerinfo import Customer
from step01.Bookinfo import Book
class BookShopAdmin:


    # self 키워드는 class내에 멤버 변수 선언 및 호출시 사용
    # 멤버 변수를 사용하는 method들도 parameter or argument or 인수 or 인자에 self 적용 필수
    # BookShopAdmin에는 멤버 변수가 없기 때문에 self 불필요
    # 객체 생성없이 method만 호출시에는 self parameter 선언하지 않음

    def cust_create():
        c1 = Customer('Lee','A')
        return c1

    def book_create():
        b1 = Book('Python','Kim')
        return b1

    if __name__ == '__main__':
        # python BookShopAdmin.py 명령어로 실행시 최초로 자동 실행되는 로직의 코드
        # intro 설정 코드, 이 부분이 먼저 실행이 된다.



        print(cust_create()) # c1 = <Customerinfo.Customer object at 0x018D1FA0>
        #생성된 객체가 저장된 시스템 메모리의 이름을 c1 변수에 대입
        
        print(cust_create().getCustName()) # Lee
        #c1 class내에 선언된 method를 호출하여 print

        print(book_create()) # b1 = <Bookinfo.Book object at 0x00BC1FA0>
        print(book_create().getBookName())

