'''1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다. # lower
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. # replace('..','.')
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. if, replace
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다. false
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.'''


# def solution(pw):
#      ans = ''
#      pw = pw.lower()
#      for i in pw:
#           if i.isalpha() or i.isdigit() or i in ['-','_','.']:
#                ans += i
#           else:
#                ans += ""
#      while '..' in ans :
#           ans = ans.replace('..','.')

#      if ans[0] == '.':
#         ans = ans[1:] if len(ans) > 1 else '.'
#      if ans[-1] == '.':
#         ans = ans[:-1]

#      if ans=='':
#           ans='a'

#      if len(ans) > 15:
#           ans = ans[:15]
#           if ans[-1]=='.':
#                ans = ans[:-1]

#      while len(ans) <3:
#           ans += ans[-1]
               
#      return ans


# a = "....!@BaT#*..y...abcdefghijklm..."
# b = 	"z-+.^."
# print(solution(b))


# 로또의 최고순위와 최저순위
'''
def solution(lotto,win):
     a = lotto.count(0)
     b = list(filter(lambda x:x>0,lotto))
     ans = 0
     for i in range(len(b)):
          if b[i] in win:
               ans += 1
     good = a+ans
     bad = ans
     rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
     final = [rank[good],rank[bad]]

     return final

lottos = [44, 1, 0, 0, 31, 25]
wins = 	[31, 10, 45, 1, 6, 19]
print(solution(lottos,wins))
'''


#비밀지도

def solution(n,arr1,arr2):
     b1 = []
     b2 = []
     b3 = []
     ans = []
     for i in arr1:
          b1.append(bin(i)[2:].zfill(n))
     for j in arr2:
          b2.append(bin(j)[2:].zfill(n))
     for k in range(n):
          b3.append(str(int(b1[k]) + int(b2[k])).zfill(n))
     
     for a in range(n):
          p=''
          for b in range(n):
               if b3[a][b] != '0':
                    p += '#'
               else:
                    p += ' '
          ans.append(p)

     return ans
n = 6
arr =[46, 33, 33 ,22, 31, 50]
brr =[27 ,56, 19, 14, 14, 10]
print(solution(n,arr,brr))
