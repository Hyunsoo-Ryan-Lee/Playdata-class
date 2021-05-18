'''
v = []
values = ['v1 test', 'v2 test', 'v3 test', 'v4', 'v5']
for x in values:
    if len(x) > 2:
        v.append(x.upper());
print(v)

v = [x.upper() for x in values if len(x)>2]
print(v)
'''
'''
p = []
data = list(range(10))
p = [x for x in data if x%2!=0]
print(p)

print(data[1:len(data):2])


word = "letter"
print("value %s is %s letter" %(p,word))

data1 = "   oo  바람만 불면 외롭고 또 괴로워 슬픈 노래를 부르던 날이 많았는데  oo   "
print(data1.strip())
print(data1.lstrip())
print(data1.rstrip())
'''

s1 = ["사과","귤","오렌지"]
print(" ".join(s1))

data1 = "바람만 불면 외롭고 또 괴로워 슬픈 노래를 부르던 날이 많았는데"
print(data1.split(" ",4))
print(data1.split(" "))


s2 = "안녕세상!"
print(reversed(s2)) #존재하는 문자열을 역으로 변환된 객체가 저장된 메모리 주소값(아직 가공 X)
print("".join(reversed(s2)))
list(s2).reverse #reverse 함수는 list 형태에서 사용가능하며 단순히 섞어주는 기능만 한다.
print(s2)
print(s2[::-2])


def reversing_words_slice(word):
    a = list(str1.split(" "))
    return " ".join(reversed(a))

str1 = "엔코아 플레이데이터 openpose"
str2 = reversing_words_slice(str1)
print(str2)


def reversing_words_slice(word):
  new_word = []
  words = word.split(' ')

  for w in words[::-1]:
    new_word.append(w)
  
  return ' '.join(new_word)


str1 = "엔코아 플레이데이터 openpose"
str2 = reversing_words_slice(str1)
print(str2)