# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def getName(self):
#         return self.name
#     def setName(self,name):
#         self.name = name
        
# p1 = Person('Lee',31)
# p2 = Person('Yein', 28)
# p1.getName()



# a = ['100000012\n', '1000000\n', '1000000\n', '500000\n', '1500000\n']

# for i in a:
#     print(i)

# print(int(a[0]))

'''1. 이름과 나이를 입력해놓은 파일을 불러들여 읽은 후에
2. 나이 순으로 정렬하여(나이가 같다면 이름도 오름차순 정렬) 
3. 나이 정렬하였을 때, 홀수번째 사람들끼리 팀 / 짝수번째 사람들끼리 팀
4. 팀원의 이름과 나이 리스트 반환
'''

# class person:
#     def __init__(self,number,name,age):
#         self.number = number
#         self.name = name
#         self.age = age

#     # def team(self):
        

# p1 = person(1, '손흥민', 28)
# p2 = person(2, '박지성', 30)
# p3 = person(3, '루니', 35)
# p4 = person(4, '인자기', 43)
# p5 = person(5, '호날두', 22)
# p6 = person(6, '메시', 30)
# p7 = person(7, '비디치', 33)
# p8 = person(8, '드록바', 27)


# player = a.append(list(input("number name age : ").split(' ')))
p_list = []
p_map = {}
team_a = []
team_b = []
while len(p_list)<8:
    p_list.append(list(input("number name age : ").split(' ')))
for i in p_list:
    p_map[i[1]] = int(i[2])
map_sort = sorted(p_map.items(), key=lambda item:item[1])
for j in range(len(map_sort)):
    if j%2 == 0: team_a.append(map_sort[j])
    if j%2 == 1: team_b.append(map_sort[j])

print("A팀 멤버 : {0}\nB팀 멤버 : {1}".format(team_a, team_b))

# (1 손흥민 28)
# (2 박지성 30)
# (3 루니 35)
# (4 인자기 43)
# (5 호날두 22)
# (6 메시 30)
# (7, '비디치', 33)
# (8, '드록바', 27)






