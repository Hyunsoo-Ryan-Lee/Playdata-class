class Iphone1:
    ''' Iphone have name, nuber, version(optional)
    three method : update_version, calling, contact
    '''
    def __init__(self, name, number, version=1.0):
        # define three methods : name, nuber, version(optional)
        self.name = name
        self.number = number
        self.version = version

    def update_version(self):
        # this method is about the version of the phone
        if self.version == 1.0:
            print('현재 폰의 버전은 [Version {}] 입니다.'.format(self.version))

    def calling(self):
        n = open('numbers.txt','r',encoding='utf-8')
        search = input('검색어 입력 : ')
        a = 0
        for i in n.readlines():
            if i[:3] == search:
                a += 1
                print('{0}({1})에게 전화를 겁니다.'.format(i[:3],i[3:-1]))
        if a == 0:
            print('매치되는 이름이 없습니다.')

    def contact(self):
        n = open('numbers.txt','r',encoding='utf-8')
        search = input('전화번호부 검색 : ')
        search_number = {}
        for i in n.readlines():
            if i.startswith(search):
                search_number[i[:4]] = i[-14:-1]
        print(search_number)
        if len(search_number) == 0:
            print("'{}'로 시작하는 사람이 없습니다.".format(search))


class Iphone2(Iphone1):
    # Inherit Iphone1 and the version is 2.0
    def __init__(self, name, number, version=2.0):
        Iphone1.__init__(self, name, number, version)

    def update_version(self):
        if self.version == 2.0:
            print('현재 폰의 버전은 [Version {}] 입니다.'.format(self.version))

    def message(self):
        # you can send messages using Iphone2
        n = open('numbers.txt','r',encoding='utf-8')
        search = input('메세지 보낼 사람 : ')
        search_number = {}
        for i in n.readlines():
            if i.startswith(search):
                search_number[i[:4]] = i[-14:-1]
        text = input('내용을 입력하세요 : ')
        print(search_number)
        print('[문자 전송 완료]\n{0}({1})에게 메시지를 보냅니다.\n내용 : {2}'.format(i[:3],i[3:-1],text))


class Iphone3(Iphone2):
    # Inherit Iphone1, Iphone2 and the version is 3.0
    def __init__(self, name, number, version=3.0):
        Iphone2.__init__(self, name, number, version)

    def update_version(self):
        if self.version == 3.0:
            print('현재 폰의 버전은 [Version {}] 입니다.'.format(self.version))

    def wifi(self):
        # you can connect to wifi with this method if the password matched
        wifi_pw = 1234
        input_pw=0
        while input_pw != wifi_pw:
            input_pw = int(input('wifi 비밀번호 입력 : '))
            if input_pw == wifi_pw :
                print('WIFI에 연결되었습니다.')
            else :
                print('비밀번호 불일치')

p1 = Iphone3('이현수','010-8484-8484')
