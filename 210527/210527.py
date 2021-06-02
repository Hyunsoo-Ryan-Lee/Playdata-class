'''
f = open('coffee.csv','r',encoding='utf-8')
head = f.readlines()
# headlist = head.split(',')

a = []
b = []
c = []
d = []

for i in head:
    a.append(i.split(',')[0])
    b.append(i.split(',')[1])
    c.append(i.split(',')[2])
    d.append(i.split(',')[3])

print(a)

f.close()
'''

# import datetime

# a = datetime.date(2018,4,10)
# b = datetime.date.today()
# print(b-a)

# print(datetime.datetime.now())

import calendar

# print(calendar.calendar(2021,m=6))

'''
print(calendar.monthrange(2021,5)) # 0~6 = 월~일
print(calendar.firstweekday()) # 한 주의 시작일이 보통 월요일이기 때문에 0이 출력된다.
calendar.setfirstweekday(calendar.SUNDAY) # 한 주의 시작 요일을 바꿀 수 있다.
print(calendar.month(2021,5))
'''

# print(calendar.weekday(2016,1,1))
# print(calendar.monthrange(2016,2))

def solution(a, b) :
    day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    p = calendar.weekday(2016,a,b)
    return day[p]

print(solution(1,1))