#LAMBDA
def inc(n):
    return lambda x : x*n
 #1
'''
mylist2 = [('kim', 23, 100), ('lee', 27, 99), ('park', 43, 102)]
mylist2.sort(key=lambda x:x[0],reverse=True)
print(mylist2) '''
 #2
'''mylist3 = ["Egg","Ham","Tomato","Lettus"]

for a in mylist3:
    print(a.upper())
ans = []

for b in mylist3:
    x = lambda j:j.upper()
    ans.append(x(b))
print(ans)'''

# DICTIONARY SORTED
'''mydict4 = {'c':11, 'b':2, 'a':3}
print(sorted(mydict4))
print(sorted(mydict4.keys()))
print(sorted(mydict4.values()))
print(sorted(mydict4.items()))'''

# f = inc(4)
# print(f(4))

# a = [2,4,6,8]
# b = [10,12,14,16]
# yek = map(lambda x,y : x*y,a,b)

# print(list(yek))


#FILTER -> filter(function, iterable) / filter(조건 함수, 순회 가능한 데이터) 이러한 형태로 쓰임
# filter에 인자로 사용되는 function은 처리되는 각각의 요소에 대해 Boolean 값을 반환합니다.
# True를 반환하면 그 요소는 남게 되고, False 를 반환하면 그 요소는 제거 됩니다.


foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
p = filter(lambda x:x%4==0,foo)
print(list(p))

q = tuple(filter(lambda y:y>15,foo))
print(q)

# MAP -> map(함수, 리스트) 형태

def cube(a):
    return a**3
q = list(map(cube,range(1,11)))
print(q)

def gil(n):
    return len(n)
xi = ['apple', 'banana', 'cherry','watermelon']
print(list(map(gil,xi)))

pi = list(map(lambda x:len(x),xi))
print(pi)

# REDUCE

# 파이썬의 functools 내장 모듈의 reduce() 함수는 여러 개의 데이터를 대상으로 주로 누적 집계를 내기 위해서 사용합니다.
# 기본 문법은 다음과 같은데요. 기본적으로 초기값을 기준으로 데이터를 루프 돌면서 집계 함수를 계속해서 적용하면서 데이터를 누적하는 방식으로 작동합니다.

# from functools import reduce
# aa = [1,2,3,4,5]
# data = reduce(lambda x,y:x*y,aa)
# print(data)

users = [{'mail': 'gregorythomas@gmail.com', 'name': 'Brett Holland', 'sex': 'M', 'age': 73},\
    {'mail': 'hintoncynthia@hotmail.com', 'name': 'Madison Martinez', 'sex': 'F', 'age': 29},\
        {'mail': 'wwagner@gmail.com', 'name': 'Michael Jenkins', 'sex': 'M', 'age': 51},\
            {'mail': 'daniel79@gmail.com', 'name': 'Karen Rodriguez', 'sex': 'F', 'age': 32},\
                {'mail': 'ujackson@gmail.com', 'name': 'Amber Rhodes', 'sex': 'F', 'age': 42}]


# numb = [1,2,3,4,5,6]
# add = reduce(lambda acc, cur: acc + [cur["mail"]], users, [])
# add2 = reduce(lambda acc,b : acc + b['age'], users,0)
# print(add,add2)

# 유저 이름을 성별에 따라서 분류 

def mw(a):
    men = []
    women = []
    for i in users:
        if i['sex'] == 'M':
            men.append(i['name'])
        else:
            women.append(i['name'])
    return dict()

print(mw(users))

