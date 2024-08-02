class secret_code:
    def __init__(self, code, alphabet, location):
        self.c = code
        self.a = alphabet
        self.l = location

#변수 선언 및 입력
s_code, m_point, time = tuple(input().split())

#객체 생성
code1 = secret_code(s_code,m_point,int(time))

#출력
print('secret code :', code1.c)
print('meeting point :',code1.a)
print('time :', code1.l)