'''
1. 1~20까지 숫자가 순서 없이 들어가있는 list 형태의 배열 A가 있습니다.
[a,b,c] 형태로 배열이 주어질 때 a번째~b번째 수까지 뽑아서 역순정렬하고 
그 역순정렬한 list에서 c번째에 해당하는 값을 뽑아내는 함수를 만드세요.
'''
# A = [17,12,8,3,18,11,15,13,1,6,7,4,20,14,19,2,5,10,9,16]

# def numbers(a,b,c):
#     x = A[a:b+1]
#     x.sort(reverse=True)
#     return x[c]

# print(numbers(3,8,2))


'''
2. 2021년 1월1일은 금요일입니다. [a,b] 형태로 값을 받아서 
2021년 a월 b일의 요일값을 반환하는 함수를 만드세요.(윤년아님)
'''
# day = [31,28,31,30,31,30,31,31,30,31,30,31]
# today = ["목","금","토","일","월","화","수"]

# def date(a,b):
#     p=0
#     for i in range(a):
#         p+=(day[i])
#     return today[(p-31+b)%7]

# print(date(5,18))


animal = [('cat', 11), ('dog', 16), ('monkey', 24), ('anaconda', 33), ('alligator', 39), ('bee', 43), ('bear', 47), ('jaguar', 55), ('crab', 62), ('fox', 73), ('buffalo', 88)]

animal2 = []
for i in range(len(animal)):
    if animal[i][0].count("a") != 0:
        animal2.append(animal[i])
    else:
        continue
animal2.sort()
print(animal2)


# mylist3 = ['Spam', 'egg', 'Ham']
# abc=[]
# for v in mylist3 :
#     abc.append(v.upper())
# print(abc)

# mylist3.sort(key=lambda x:x)

# print(mylist3)



# MAP - map(기능 보유 함수명, 함수에 들어갈 인자)
def cube(x):
    return x**2

a = list(map(cube, range(1, 11)))
print(a)


# 길이 구하는 함수
def func(a):
    return len(a)

x = map(func,("apple","banana","orange"))
print(x) # x만 찍으면 값 출력이 안된다.
print(list(x)) # list 등의 형태에 넣어줘야 출력이 된다. 사용 가능하게 가공

y = map(func,["apple","banana","orange"])
print(y)
print(tuple(y))

z = list(map(lambda n:len(n),["apple","banana","orange"]))
print(z)


print(list(map(lambda x:x**2,range(11))))

# REDUCE -> 파이썬 functools 내장 모듈의 함수.
# 기본적으로 초기값을 기준으로 데이터를 루프 돌면서 집계 함수를
# 계속해서 적용하면서 데이터를 누적하는 방식으로 작동합니다.

# 형태 -> reduce(집계 함수, 순회 가능한 데이터[, 초기값])





# FILTER

# filter함수는 특정 조건으로 걸러서 걸러진 요소들로 iterator객체를 만들어서 리턴해줍니다.
# map함수와 사용 방법은 동일하나, 함수의 결과가 참인지 거짓인지에 따라, 해당 요소를 포함할지를 결정합니다.
# 숫자를 가지고 있는 iterable객체에서 짝수들만 포함하는 새로운 객체를 만들때 다음과 같이 코드를 작성할 수 있습니다.

