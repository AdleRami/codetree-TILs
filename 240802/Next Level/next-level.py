#객체 선언
class status:
    def __init__(self, user_id="", level=0):
        self.user_id = user_id
        self.level = level

status1 = status('codetree',10)
status2 = status()
new_id, new_level = tuple(input().split())

status2.user_id = new_id
status2.level = int(new_level)

print(f"user {status1.user_id} lv {status1.level}")
print(f"user {status2.user_id} lv {status2.level}")