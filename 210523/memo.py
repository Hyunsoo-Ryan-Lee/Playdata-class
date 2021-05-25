# def solution(record):
#     answer =[]
#     output = []
#     inuser = {}
#     # 1
#     for i in record:
#         command = i.split(" ")
#         # 2
#         if command[0] == 'Leave':
#             output.append([command[1],"님이 나갔습니다."])
#         # 3
#         elif command[0] == 'Enter':
#             inuser[command[1]] = command[2]
#             output.append([command[1],"님이 들어왔습니다."])
#         # 4
#         elif command[0] == 'Change':
#             inuser[command[1]] = command[2]
#     # 5
#     for log in output:
#         answer.append(inuser[log[0]]+log[1])
#     # 6
#     return answer

# a = [5, 10, 1, 1, 20, 1]


# for i in range(len(a)):
#     for j in range(len(a)):
#         if i!=j:
#             if i<=j:
#                 print(a.index(i), a.index(j))

a = ['김철수 010-1234-1234\n', '김미미 010-2222-2222\n', '박종민 010-2564-5555\n']
s = input('asdf : ')
for i in a:
    if i[:3] == s:
        print('{0}({1})에게 전화를 겁니다.'.format(i[:3],i[3:-1]))