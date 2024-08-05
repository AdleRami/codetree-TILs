#클래스 선언
class bomb_code:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

#변수 선언 및 입력
user_code, line_color, time = tuple(input().split())

code1 = bomb_code(user_code, line_color, int(time))


print(f'code : {code1.code}')
print(f'color : {code1.color}')
print(f'second : {code1.second}')