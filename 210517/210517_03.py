#Dictionary -> {KEY:VALUE} 형태로 이루어진 집합
'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #중간에 year 값 변경
}
print(thisdict.keys()) #키만 출력
print(thisdict.values()) #값만 출력
print(thisdict.items()) #키와 값 쌍으로 출력

thisdict["year"] = 2010 #year 값 수정
thisdict["color"] = "black" #새로운 키:값 쌍 추가
print(thisdict)
'''

# Dictionary 속에 Dictionary
'''
team = {"name":{1:"RYAN",2:"YEIN",3:"ALICE"}, "age":{1:30, 2:25, 3:27},\
     "job":{"a":"student","b":"writer","c":"traveler"}}

name_group = team["name"] # {1: 'RYAN', 2: 'YEIN', 3: 'ALICE'}
age_group = team["age"]
job_group = team["job"]

print(name_group[1])
print(team["name"][1])
'''

# 문장내 글자수 세기(공백은 제외)

data = '''내 속엔 내가 너무도 많아 당신의 쉴 곳 없네
내 속엔 헛된바램들로 당신의 편할 곳 없네
내 속엔 내가 어쩔 수 없는 어둠 당신의 쉴 자리를 뺏고
내 속엔 내가 이길 수 없는 슬픔 무성한 가시나무숲같네
바람만 불면 그 메마른가지 서로 부대끼며 울어대고
쉴곳을 찾아 지쳐 날아온 어린새들도 가시에 찔려 날아가고
바람만 불면 외롭고 또 괴로워 슬픈 노래를 부르던 날이 많았는데
내 속엔 내가 너무도 많아서 당신의 쉴 곳 없네
바람만 불면 그 메마른가지 서로 부대끼며 울어대고
쉴곳을 찾아 지쳐 날아온 어린새들도 가시에 찔려 날아가고
바람만 불면 외롭고 또 괴로워 슬픈 노래를 부르던 날이 많았는데
내 속엔 내가 너무도 많아서 당신의 쉴 곳 없네'''
word = set(data) # set을 이용하여 각 단어들을 중복없이 넣어준다.
dic = {}
for i in word :
    if i != " ":
        num1 = data.count(i)
        dic.update({i:num1}) # update({a:b}) 형태를 이용하여 dict에 추가 가능
    else:
        continue
print(dic)

'''
# LOOP LIST (대괄호 []를 이용하여 줄여서 쓰기)

# 1. 원래 format
lst = []
for p in list(range(11)):
    if p>5:
        lst.append(p)
print(lst)

# 2. 줄인 form_01
a = [x for x in range(11) if x>5]
print(a)

# 3. 줄인 form_02
b = []
[b.append(x) for x in range(11) if x>5]
print(b)

# 다른 예시
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = [x if x != "kiwi" else "orange" for x in fruits]
# fruits 내 값들에 대해 'kiwi'가 아닌것들은 if문에서 True이기 때문에 그대로 pass,
#하지만 'kiwi'라면 if문에서 False이기 때문에 Else문으로 가서 'Orange'가 출력.
print(new)

# 또 다른 예시_원래 format
v = []
values = ['v1 test', 'v2 test', 'v3 test', 'v4', 'v5']
for x in values:
    if len(x) > 2:
        v.append(x.upper())
print(v)

# 또 다른 예시_줄인 format
short = [x.upper() for x in values if len(x)>2]
print(short)
'''

# REVERSE
str1 = "엔코아 플레이데이터 openpose"
re = list(str1.split(" "))
print(" ".join(reversed(re))) # 1번

print(" ".join(reversed(list(str1.split(" "))))) # 2번

print(" ".join(re[::-1])) # 3번

re.reverse() 
print(" ".join(re)) # 4번