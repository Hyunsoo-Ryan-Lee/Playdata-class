from TVinfo import TV

class Test: # 멤버 변수가 없음

    # list에 TV 객체들 저장
    def tv_info():
        tv_all = [TV('슬림','LG'), TV('코어','SS')]
        return tv_all
    # 이미 list내에 저장된 TV객체들의 이름만 출력

    def tv_info_print(datas):
        for i in datas:
            print(i.getName())




    if __name__ == '__main__':
        # tv = TV('슬림','LG')
        # print(tv)

        print(tv_info()) 
        # [<TVinfo.TV object at 0x010F1FD0>, <TVinfo.TV object at 0x0110B0A0>]
        # TV class 객체들의 정보가 저장된 list가 출력

        tv_info_print(tv_info())