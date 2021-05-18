'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}

# print(thisdict)
# print(thisdict.keys())
# print(thisdict.values())
print(thisdict.items())

thisdict["model"] = "bently"

print(thisdict.items())

for a in thisdict.keys():
    print(a, thisdict[a])
'''

'''
team1 = {"name":{1:"Lee", 2:"Kim", 3:"YOO"}, "age":{1:20, 2:30, 3:25}, \
    "job":{1:"singer", 2:"student", 3:"teacher"}}

print(team1["name"][3])

thisset = {True, "Lee" ,30, "camera"}

if False in thisset :
    print("True")
else:
    print("nono")

for i in thisset :
    print(i)
'''
# [문제]
# 파티에 참석한 사람들의 명단이 세트 A와 B에 각각 저장되어 있다.
# 2개 파티에 모두 참석한 사람들의 명단을 출력하려면 어떻게 해야 할까?

# [출력 결과]
# 2개의 파티에 모두 참석한 사람은 다음과 같습니다.
# {'Park'}


from os import lstat


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

# a = (set(data))
# b = {}
# for i in a:
#     num1 = data.count(i)
#     b.update({i:num1})
# print(b)

# c = set(data.split(" "))
# d = {}
# for j in c:
#     if j.count("\n")!=0:
#         continue
#     else:
#         num2 = data.count(j)
#         d.update({j:num2})
# print(d)

lst = []
for p in [1,2,3]:
    print(p)

[lst.append(p+10) for p in [1,2,3,4]]
print(lst)

new = [x for x in range(10) if x<5]
print(new)

this = [True, "Lee" ,30, "camera"]
[print(x) for x in this]

newthis = ["hello" for x in this]
print(newthis)

[print(x) if x!='Lee' else 30 for x in this]