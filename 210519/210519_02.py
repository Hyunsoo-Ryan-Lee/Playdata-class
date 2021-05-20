users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},\
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},\
        {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},\
            {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},\
                {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]

# ans = []
# for i in users:
#     if i['sex'] == 'M':
#         ans.append(i['name'])
#     else:
#         continue
# print(ans)

'''
def is_men(a): #is_men 이라는 함수 정의
    return a['sex'] == 'M' 
    # 주어진 dict type의 a값의 'sex'라는 key와 매치되는 value가 "M"이면 return.

for man in filter(is_men,users): #man은 is_men함수가 True일때 나오는 값
# 딕셔너리들의 list인 users의 값이 하나하나씩 is_men에 들어간다.
# is_men 함수가 돌면서 sex가 M인 항목들만 추려낸다. 그게 man이다.
    print(man) #추려진 값들을 print 한다.

for women in filter(lambda x:x['sex'] !='M',users):
    # users list의 각 항들이 하나씩 들어가 lambda x:x['sex'] !='M'가 True가 되는 녀석들이 women이 된다.
    # users의 각 항인 딕셔너리가 x로 들어가게 되는데 거기서 sex가 M이 아닌 리스트 항들이 women으로 들어감.
    print(women)

#.endswith(), startswith() 함수로 값 뽑기

for mail in filter(lambda x:x['name'].endswith('ez'),users):
    print(mail)
for papa in filter(lambda x:x['name'].startswith('M'),users):
    print(papa)
print()
print()
    
    
[print(a) for a in users if a["sex"]=='M']
print()
[print(b) for b in users if b['mail'].endswith(".com")]

'''

def intro(**kwargs):
    for a,b in kwargs.items():
        print("{} and {}".format(a,b))

ti = intro(name='kim')


def speak(**kwargs):
    for a,b in kwargs.items():
        if '김' in kwargs.keys():
            print("어서옵쇼!")
        else:
            print("{}이 {}왔구나!".format(a,b))
fi = speak(김 = '빨리')


from functools import reduce
a = [1,2,3,4]
b = [-3,-1,0,2]
def solution(a,b):
    # ans = 0
    # for i in range(len(a)):
    #     p = a[i]*b[i]
    #     ans += p
    # return ans
    
    return sum([x*y for x,y in zip(a,b)])
print(solution(a,b))


x = ["leo", "kiki", "eden"]	
y = ["eden", "kiki"]

for i in range(len(y)):
    x.remove(y[i])
print(x)

# for i in range(len(y)):
#     if x.count(y[i]) != 0:
#         x.remove(y[i])
# print(x)

#PROGRAMMERS - 폰켓몬

def poke(num):
    ans = list(set(num))
    if len(ans)<=len(num)/2 :
        return len(ans)
    else:
        return len(num)/2
