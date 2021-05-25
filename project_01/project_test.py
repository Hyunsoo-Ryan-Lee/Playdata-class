# p_list = []
# p_map = {}
# team_a = []
# team_b = []
# while len(p_list)<8:
#     p_list.append(list(input("number name age : ").split(' ')))
# for i in p_list:
#     p_map[i[1]] = int(i[2])
# map_sort = sorted(p_map.items(), key=lambda item:item[1])
# for j in range(len(map_sort)):
#     if j%2 == 0:
#         team_a.append(map_sort[j])
#     if j%2 == 1:
#         team_b.append(map_sort[j])

# print("A팀 멤버 : {0}\nB팀 멤버 : {1}".format(team_a, team_b))

'''
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print('[지상 유닛 이동]')
        print('{0} : {1}시 방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name,damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp < 0:
            print('{} : 파괴되었습니다.'.format(self.name))
        
class attackunit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}'\
            .format(self.name, location, self.damage))
    
class Marine(attackunit):
    def __init__(self):
        attackunit.__init__(self, '마린', 40, 1, 5)

    def steampack(self):
        if self.hp > 10:
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다.\n체력 : {1}'\
                .format(self.name,self.hp))
        else:
            print('체력이 부족하여 스팀팩을 사용할 수 없습니다.')

class Tank(attackunit):

    def __init__(self):
        attackunit.__init__(self, '탱크', 150, 2, 35)
        self.seige_dev = False

    def seigemode(self):
        if self.seige_dev == True:
            print('{} : 시즈모드 해제!'.format(self.name))
            self.damage /= 2
            self.seige_dev == False
        else:
            self.damage *= 2
            print('{0} : 시즈모드 ON!\n공격력이 증가하였습니다.[{1}]'\
                .format(self.name,self.damage))
            


class Flyable:
    def __init__(self, flyspeed):
        self.flyspeed = flyspeed
    
    def fly(self, name, location):
        print('{0} : {1}시 방향으로 날아갑니다. [속도 {2}]'\
            .format(name, location, self.flyspeed))

class Flyableattack(attackunit, Flyable):
    def __init__(self, name, hp, damage, flyspeed):
        attackunit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flyspeed)
    
    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)


class Wraith(Flyableattack):
    def __init__(self):
        Flyableattack.__init__(self, '레이스', 80, 15, 10)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print('{} : 클로킹 해제'.format(self.name))
            self.clocked == False
        else:
            print('{} : 클로킹 ON'.format(self.name))
            self.clocked == True

m1 = Marine()
t1 = Tank()
w1 = Wraith()
m1.steampack()
t1.seigemode()
w1.move(5)
print(t1.damage)
print(m1.hp)
'''

# class Iphone:
#     ''' Iphone have name, nuber, version(optional)
#     three method : update_version, calling, search_contact
#     '''
#     def __init__(self, name, number, version=1.0, size = 5):
#         # we will add name, number, version(optional)
#         self.name = name
#         self.number = number
#         self.version = version
#         print("개통을 축하합니다. %s님" % name)

#     def update_version(self):
#         '''update_version will add 0.1 to previous version and print it'''
#         self.version += 0.1
#         print("os version is updated!")

#     def calling(self):
#         '''calling method will input a phone number and print the number + calling string'''
#         call_num = input("phone number : ")
#         print(call_num+'calling~')


class Iphone1:
    def __init__(self, name, number, version=1.0):
        self.name = name
        self.number = number
        self.version = version

    def update_version(self):
        if self.version == 1.0:
            print('현재 폰의 버전은 [Version {}] 입니다.'.format(self.version))

    def calling(self,person):
        self.person = person
        phone_number = input('번호를 입력하세요 : ')
        print('{0}({1})에게 전화를 겁니다.'.format(self.person,phone_number))
        
    def contact(self):
        with open('numbers.txt','r',encoding='utf-8') as n:
            search = input('전화번호부 검색 : ')
            search_number = {}
            for i in n.readlines():
                if i.startswith(search):
                    search_number[i[:4]] = i[-14:-1]
            print(search_number)