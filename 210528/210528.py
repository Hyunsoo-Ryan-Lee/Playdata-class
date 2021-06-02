# 정규표현식 복습 -> Programmers 신규 아이디 추천 문제
'''
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다. [^\w\d_.-]
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. re.sub('\.+','.',new_id)
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. re.sub(^[.]|[.]$,'',new_id)
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.

if len(new_id) == 0:
    new_id = 'a'
else: 
    new_id = new_id[:15]

new_id = 'a' if len(new_id) == 0 else new_id[:15]

     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다. re.sub([.]$,'',new_id)
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
''' 


import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^\w\d\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

p = "...!@BaT#*..y.abcdefghijklm"
print(solution(p))


print(re.match('[$(a-zA-Z0-9)]+', '$(document)'))
m = re.match('(?P<inye>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<yein>\w+)\)',
'print(1234)')

print(m.group('inye'))
print(m.group('yein'))
