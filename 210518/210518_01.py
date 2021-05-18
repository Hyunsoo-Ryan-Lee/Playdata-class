#REVERSE
'''
lst = ['a', 'b', 'e', 'c']
lst.sort(reverse=True)
print(lst)

print(sorted(lst,reverse=True))

v = 1,2,'v'
print(v,type(v)) # (1, 2, 'v') <class 'tuple'>
a,b,c = v
print(a,b,c) # 1 2 v
'''

# ZIP
'''
numbers = [1,2,3]
alphas = ["A","B","C"]
x = {}
for i in range(len(numbers)):
    x.update(zip(numbers,alphas))
    
print(x)

data = 내 속엔 내가 너무도 많아 당신의 쉴 곳 없네
내 속엔 헛된바램들로 당신의 편할 곳 없네
내 속엔 내가 어쩔 수 없는 어둠 당신의 쉴 자리를 뺏고
내 속엔 내가 이길 수 없는 슬픔 무성한 가시나무숲같네

word = set(data) # set을 이용하여 각 단어들을 중복없이 넣어준다.
dic = {}
for i in word :
    if i != " ":
        num1 = str(data.count(i))
        dic.update(zip(i,num1)) # update({a:b}) 형태를 이용하여 dict에 추가 가능
    else:
        continue
print(dic)
'''

#미션- 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해 보기

from random import *
alp = "abcdefghijklmnopqrstuvwxyz0123456789"

def password():
    pw = []
    for i in range(5):
        x = randint(1,len(alp))
        pw.append(alp[x])    
    return "".join(pw)

print(password())


# import random

# def genPass():
#     alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
#     password = ""
    
#     for i in range(6):
#         index = random.randrange(36)
#         password += alphabet[index]
#     return password
    
# print(genPass())
# print(genPass())
# print(genPass())


# *(0~무한대) 가 표시된 변수
'''
def my_function(*kids):
    # 몇 개의 값이 들어갈지 모를 때, *을 붙이면 에러 안나고 값이 들어간다. 
    print("The youngest child is " + kids[1])

my_function("Emil", "Tobias",)
my_function("Emil", "Tobias", "Linus")
my_function("Emil", "Tobias", "Linus","Lee")
my_function("Emil", "Tobias", "Linus","Lee", "Kim")
'''

# 반환값이 여러개도 가능. 반환시 tuple 타입으로 자동 변환.
# 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어준다.
'''
def f1():
    return 1,2,3
print(f1())


def f2():
    return 'a', 2
v1, v2 = f2()
print(v1, v2)
print(v1)
'''

# def fun4(**a):
#     for k,v in fun4.items():
#         print(k,v)
    
# fun4(x=10, y=20, z=30)

# kwargs parameter
#**kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
def print_kwargs(**kwargs): # kwargs = keyword arguments의 약자
    print(kwargs)


print_kwargs(name='foo', age=3)



import random
print(random.randint(0,30))