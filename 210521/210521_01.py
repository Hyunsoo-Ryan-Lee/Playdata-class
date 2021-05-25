# Q1-1
# 반복문을 사용하여 임의의 값을 받아(2~9단) 구구단을 출력하는 프로그램을 작성하시오




# Q1-2
# 임의의 숫자의 범위를 정하고 (예: 0~100) 반복문을 사용하여 범위 내의 소수(素数)를 출력하는 프로그램을 작성하시오
# ※ 소수(素数): 1과 자기 자신만으로 나누어 떨어지는 정수

num = input('start : end => ') #5 10
rge = list(map(int,num.split(' ')))
total = []
for i in range(rge[0],rge[1]+1): # 5~10       
    ans = 0
    for j in range(2,(i//2)+1):
        if i%j == 0: ans += 1
    if ans == 0: total.append(i)
print(total)


# eve = []
# for i in range(10, 30):
#     for j in range(10, 30):
#         a = i * j
#         if str(a) == str(a)[::-1]:
#             eve.append(a)
# print(eve)
# print('*'*40)
# print(str(a)[::-1])


# 프로그래머스 - 크레인 인형뽑기

# [0,0,0,0,0]
# [0,0,1,0,3]
# [0,2,5,0,1]
# [4,2,4,4,2]
# [3,5,1,3,1]      moves = [1,5,3,5,1,2,1,4]	
'''
def solution(board,moves):
    stack = [0]
    ans = 0
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                stack.append(b[m-1])
                b[m-1] = 0
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    ans += 2
                break
    return ans

a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]
print(solution(a,b))
'''

# stack = [4, 3, 1, 1, 3, 2, 4]

# for i in range(0,6): #7  [4, 3, 1, 1, 3, 2, 4]
#     if stack[i] == stack[i+1]:
#         stack.pop(i)


# [stack.pop(i) for i in range()]

# 프로그래머스 - 음수양수 합
'''
ab = [4,7,12]
sig = [True,False,True]

def solution(ab,sig):
    a = list(zip(ab,sig))
    ans = 0
    for i in a :
        if i[1] == True:
            ans += i[0]
        else:
            ans -= i[0] 
    return ans
print(solution(ab,sig))

def sol(a,b):
    return sum(a if b else -a for a,b in zip(a,b))
    
print(sol(ab,sig))
'''

# 프로그래머스 - 짝지어 제거하기
'''
def solution(a):
    ans = []
    for i in a:
        if len(ans) == 0 :
            ans.append(i)
        elif i != ans[-1]:
            ans.append(i)
        else:
            ans.pop()
    if len(ans) == 0: return 1
    else: return 0

a = 'baabaa'
print(solution(a))
'''



